"""Barraquer · datos del panel de alertas de Google Ads (Obsidian).
Uso: python3 -I datos_panel_alertas.py <ads.xlsx> <salida.json> [AAAA-MM-DD]
Lee la hoja "Barraquer - Google Ads diario" (Info, Campañas, Diario_Campañas) y escribe el JSON
que lee el panel 4. Seguimiento/Alertas Google Ads - Barraquer.md:
  datos_hasta, ultima_ejecucion, generado, alertas, campanas, serie, cuenta, semanas.
Reglas:
  · Ayer (graves, día D): activa sin impresiones o con gasto < 20 % de su media de 7 días;
    gasto > 2× la media (mín. 20 €); 0 conversiones con gasto ≥ 3× su CPL de 4 semanas.
  · Tendencias (D-6..D frente a D-34..D-7): racha sin conversiones más larga que la peor de
    60 días; sin conversiones en 60 días con ≥ 100 €; CPL +30 %; CR −30 %; CTR −30 %.
    Cada tendencia se compara con las mismas fechas del año pasado (−364 días) para decir si
    es probablemente estacional.
Imprime: ruta, nº de campañas con alerta de ayer, nº con tendencias, fecha de datos, última ejecución.
"""
import sys, os, json, datetime as dt
import openpyxl

U = dict(MIN_INV_DIA=10, CASI_SIN_GASTO=0.2, GASTO_DISPARADO=2.0, MIN_GASTO_DISP=20, GASTO_SIN_CONV=3.0,
         MIN_CONV_REF=3, MIN_CONV_ESPERADAS=3, RACHA_MIN=3, RACHA_GASTO_CPL=2.0, SIN_CONV_NUNCA=100,
         CAIDA_CTR=0.7, MIN_IMP_7D=1000, SUBIDA_CPL=1.3, CAIDA_CR=0.7, MIN_CLICS_7D=50, DIAS_HIST=60,
         ESTACIONAL=0.3)  # el año pasado empeoró al menos un 30 % en el mismo sentido → estacional
SIN_CONV_TIPOS = {'VIDEO', 'DEMAND_GEN'}


def fecha(v):
    return v.strftime('%Y-%m-%d') if isinstance(v, (dt.datetime, dt.date)) else str(v)[:10]


def ident(v):
    try:
        return str(int(float(v)))
    except (TypeError, ValueError):
        return str(v)


def num(v):
    try:
        return float(v or 0)
    except (TypeError, ValueError):
        return 0.0


def fmt(n, d):
    s = f"{abs(n):,.{d}f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    return ('-' if n < 0 else '') + s


def eur(n): return fmt(n, 2) + ' €'
def pct(n): return fmt(n * 100, 2) + ' %' if n else '—'
def r(a, b): return a / b if b else 0
def r2(x): return round(x, 2) if x else (0 if x == 0 else None)
def cpl(t): return round(t['inv'] / t['conv'], 2) if t['conv'] else None


def var(a, b):
    if not b:
        return '—'
    v = round((a / b - 1) * 100)
    return ('+' if v > 0 else '') + f'{v} %'


def vacio(): return dict(inv=0.0, imp=0.0, cl=0.0, conv=0.0)


def acum(a, b):
    for k in a:
        a[k] += b[k]


def corto(nombre):
    p = str(nombre).split('_')
    if len(p) >= 5 and p[0] in ('google', 'meta', 'dv360'):
        canal = p[2].replace('-', ' ')
        linea = '' if p[1] == 'clinica' else p[1] + ' · '
        return f"{linea}{canal} · {'_'.join(p[4:])}"
    return str(nombre)


def main():
    xlsx, salida = sys.argv[1], sys.argv[2]
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    info = {row[0]: row[1] for row in wb['Info'].iter_rows(min_row=2, values_only=True) if row and row[0]}
    D = sys.argv[3] if len(sys.argv) > 3 else fecha(info.get('Campañas hasta'))
    ult = info.get('Última ejecución')
    ult = ult.strftime('%Y-%m-%d %H:%M') if isinstance(ult, dt.datetime) else str(ult)
    d0 = dt.date.fromisoformat(D)
    dia = lambda n: (d0 + dt.timedelta(n)).isoformat()
    ly = lambda f: (dt.date.fromisoformat(f) - dt.timedelta(364)).isoformat()
    ult7 = [dia(-k) for k in range(0, 7)]
    prev7 = [dia(-k) for k in range(1, 8)]
    ref28 = [dia(-k) for k in range(7, 35)]
    hist = [dia(-k) for k in range(U['DIAS_HIST'] - 1, -1, -1)]
    serie28 = [dia(-k) for k in range(27, -1, -1)]
    semanas = [[dia(-7 * s - k) for k in range(0, 7)] for s in range(7, -1, -1)]  # 8 bloques de 7 días hasta D
    utiles = set(hist + ref28)
    utiles |= {ly(f) for f in list(utiles)}

    meta = {}
    for row in wb['Campañas'].iter_rows(min_row=2, values_only=True):
        if row and row[0] is not None:
            meta[ident(row[1]) + '|' + ident(row[3])] = dict(estado=row[4], tipo=row[5], ppto=num(row[7]))

    camp, cuenta = {}, {}
    for row in wb['Diario_Campañas'].iter_rows(min_row=2, values_only=True):
        if not row or row[0] is None:
            continue
        f = fecha(row[0])
        if f not in utiles:
            continue
        x = dict(inv=num(row[7]), imp=num(row[8]), cl=num(row[9]), conv=num(row[10]))
        acum(cuenta.setdefault(f, vacio()), x)
        key = ident(row[2]) + '|' + ident(row[4])
        c = camp.setdefault(key, dict(key=key, nombre=str(row[3]), estado=row[5], tipo=row[6], f={}))
        acum(c['f'].setdefault(f, vacio()), x)

    # el año pasado se busca por nombre de campaña (los ID pueden cambiar)
    por_nombre = {}
    for c in camp.values():
        for f, x in c['f'].items():
            acum(por_nombre.setdefault(c['nombre'], {}).setdefault(f, vacio()), x)

    def suma(fs, fechas):
        t = vacio()
        for f in fechas:
            if f in fs:
                acum(t, fs[f])
        return t

    alertas, campanas, con_alerta = [], [], []
    for c in camp.values():
        fs, fl = c['f'], por_nombre[c['nombre']]
        hoy, p7, u7, r28, h60 = suma(fs, [D]), suma(fs, prev7), suma(fs, ult7), suma(fs, ref28), suma(fs, hist)
        ly7, ly28 = suma(fl, [ly(f) for f in ult7]), suma(fl, [ly(f) for f in ref28])
        if not h60['inv']:
            continue
        m = meta.get(c['key'], {})
        estado, tipo, ppto = m.get('estado', c['estado']), m.get('tipo', c['tipo']), m.get('ppto', 0)
        nom, cor = c['nombre'], corto(c['nombre'])
        conv_ok = tipo not in SIN_CONV_TIPOS
        media = p7['inv'] / 7
        cpl28 = r(r28['inv'], r28['conv']) if r28['conv'] >= U['MIN_CONV_REF'] else 0
        cpl60 = r(h60['inv'], h60['conv']) if h60['conv'] >= U['MIN_CONV_REF'] else 0

        rachas, racha, g_racha = [], 0, 0.0
        for f in hist:
            x = fs.get(f)
            if not x or not x['inv']:
                continue
            if x['conv']:
                if racha:
                    rachas.append(racha)
                racha, g_racha = 0, 0.0
            else:
                racha += 1; g_racha += x['inv']
        peor = max(rachas) if rachas else 0

        base = dict(campana=nom, corto=cor, cpl_7d=cpl(u7), cpl_4sem=cpl(r28), cpl_ly_7d=cpl(ly7), cpl_ly_4sem=cpl(ly28))
        hay_ly = bool(ly7['inv'] or ly28['inv'])

        def add(bloque, regla, texto, contexto='', veredicto='contexto'):
            alertas.append(dict(base, bloque=bloque, regla=regla, texto=texto, contexto_ly=contexto, veredicto=veredicto))

        def comparar_ly(ahora_ly, antes_ly, sube_es_malo):
            if not (ahora_ly and antes_ly):
                return 'Sin datos del año pasado para comparar', 'sin_ly'
            v = ahora_ly / antes_ly - 1
            peor_ly = v >= U['ESTACIONAL'] if sube_es_malo else v <= -U['ESTACIONAL']
            pv = round(v * 100)
            if peor_ly:
                return f"Posible estacionalidad: el año pasado también {'subió' if v > 0 else 'bajó'} ({'+' if pv > 0 else ''}{pv} %)", 'estacional'
            return f"No parece estacional: el año pasado {'subió' if v > 0 else 'bajó'} un {abs(pv)} % en las mismas fechas", 'real'

        # ---------- AYER ----------
        if estado == 'ENABLED' and media >= U['MIN_INV_DIA']:
            if not hoy['imp']:
                add('ayer', 'sin_impresiones', f"Activa y sin impresiones ayer (gastaba {eur(media)}/día de media)")
            elif hoy['inv'] < media * U['CASI_SIN_GASTO']:
                add('ayer', 'casi_sin_gasto', f"Casi sin gasto ayer: {eur(hoy['inv'])} frente a {eur(media)}/día de media")
        if hoy['inv'] >= U['MIN_GASTO_DISP'] and media and hoy['inv'] > media * U['GASTO_DISPARADO']:
            extra = f"; presupuesto diario {eur(ppto)}" if ppto else ''
            add('ayer', 'gasto_disparado', f"Gasto disparado: {eur(hoy['inv'])} frente a {eur(media)}/día de media ({var(hoy['inv'], media)}{extra})")
        if conv_ok and cpl28 and not hoy['conv'] and hoy['inv'] >= cpl28 * U['GASTO_SIN_CONV']:
            add('ayer', 'gasto_sin_conv', f"{eur(hoy['inv'])} en un día sin ninguna conversión ({fmt(hoy['inv'] / cpl28, 1)} veces su CPL de 4 semanas, {eur(cpl28)})")

        # ---------- TENDENCIAS ----------
        if conv_ok:
            ctx_ly = (f"Mismas fechas del año pasado: {fmt(ly7['conv'], 0)} conv. en 7 días con {eur(ly7['inv'])}"
                      if hay_ly else 'Sin datos del año pasado')
            if not h60['conv'] and h60['inv'] >= U['SIN_CONV_NUNCA']:
                add('tendencia', 'nunca_convierte', f"Ninguna conversión en {U['DIAS_HIST']} días con {eur(h60['inv'])} de gasto",
                    ctx_ly, 'contexto' if hay_ly else 'sin_ly')
            elif cpl60 and racha >= U['RACHA_MIN'] and racha > peor and g_racha >= cpl60 * U['RACHA_GASTO_CPL']:
                add('tendencia', 'racha', f"{racha} días seguidos sin conversiones ({eur(g_racha)}); su peor racha en {U['DIAS_HIST']} días era de {peor}",
                    ctx_ly, 'contexto' if hay_ly else 'sin_ly')
            esperadas = r(u7['inv'], cpl28)
            if cpl28 and u7['conv'] and esperadas >= U['MIN_CONV_ESPERADAS']:
                cpl7 = u7['inv'] / u7['conv']
                if cpl7 > cpl28 * U['SUBIDA_CPL']:
                    add('tendencia', 'cpl', f"CPL {eur(cpl7)} frente a {eur(cpl28)} ({var(cpl7, cpl28)})",
                        *comparar_ly(r(ly7['inv'], ly7['conv']), r(ly28['inv'], ly28['conv']), True))
            crU, crR = r(u7['conv'], u7['cl']), r(r28['conv'], r28['cl'])
            if (u7['cl'] >= U['MIN_CLICS_7D'] and u7['conv'] and cpl28 and esperadas >= U['MIN_CONV_ESPERADAS']
                    and crR and crU < crR * U['CAIDA_CR']):
                add('tendencia', 'cr', f"CR {pct(crU)} frente a {pct(crR)} ({var(crU, crR)})",
                    *comparar_ly(r(ly7['conv'], ly7['cl']), r(ly28['conv'], ly28['cl']), False))
        ctrU, ctrR = r(u7['cl'], u7['imp']), r(r28['cl'], r28['imp'])
        if u7['imp'] >= U['MIN_IMP_7D'] and ctrR and ctrU < ctrR * U['CAIDA_CTR']:
            add('tendencia', 'ctr', f"CTR {pct(ctrU)} frente a {pct(ctrR)} ({var(ctrU, ctrR)})",
                *comparar_ly(r(ly7['cl'], ly7['imp']), r(ly28['cl'], ly28['imp']), False))

        if alertas and alertas[-1]['campana'] == nom and nom not in [x[0] for x in con_alerta]:
            con_alerta.append((nom, fs, fl))
        if u7['inv'] or hoy['inv']:
            campanas.append(dict(campana=nom, corto=cor, tipo=tipo, estado=estado, ppto_diario=ppto,
                                 inv_ayer=r2(hoy['inv']), imp_ayer=int(hoy['imp']), conv_ayer=r2(hoy['conv']),
                                 media_7d_previos=r2(media), inv_7d=r2(u7['inv']), conv_7d=r2(u7['conv']),
                                 clics_7d=int(u7['cl']), imp_7d=int(u7['imp']), inv_4sem=r2(r28['inv']),
                                 conv_4sem=r2(r28['conv']), clics_4sem=int(r28['cl']), imp_4sem=int(r28['imp']),
                                 inv_ly_7d=r2(ly7['inv']), conv_ly_7d=r2(ly7['conv']), inv_ly_4sem=r2(ly28['inv']),
                                 conv_ly_4sem=r2(ly28['conv']), dias_sin_conv=racha if conv_ok else None,
                                 peor_racha_60d=peor if conv_ok else None))

    serie, sem = [], []
    for nom, fs, fl in con_alerta:
        for f in serie28:
            x = fs.get(f, vacio())
            serie.append(dict(campana=nom, fecha=f, inversion=r2(x['inv']), impresiones=int(x['imp']), conversiones=r2(x['conv'])))
        for bloque in semanas:
            x, y = suma(fs, bloque), suma(fl, [ly(f) for f in bloque])
            sem.append(dict(campana=nom, semana_fin=bloque[0], inversion=r2(x['inv']), conversiones=r2(x['conv']), clics=int(x['cl']),
                            inversion_ly=r2(y['inv']), conversiones_ly=r2(y['conv']), clics_ly=int(y['cl'])))

    cta = []
    for f in hist:
        x, y = cuenta.get(f, vacio()), cuenta.get(ly(f), vacio())
        cta.append(dict(fecha=f, inversion=r2(x['inv']), clics=int(x['cl']), impresiones=int(x['imp']),
                        conversiones=r2(x['conv']), inversion_ly=r2(y['inv']), conversiones_ly=r2(y['conv'])))

    out = dict(datos_hasta=D, ultima_ejecucion=ult, generado=dt.date.today().isoformat(),
               alertas=alertas, campanas=campanas, serie=serie, cuenta=cta, semanas=sem)
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with open(salida, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False)
    n_ayer = len({a['campana'] for a in alertas if a['bloque'] == 'ayer'})
    n_tend = len({a['campana'] for a in alertas if a['bloque'] == 'tendencia'})
    print(f'{salida}\t{n_ayer} campañas con alerta de ayer\t{n_tend} campañas con tendencias\tdatos hasta {D}\túltima ejecución script {ult}')


if __name__ == '__main__':
    main()
