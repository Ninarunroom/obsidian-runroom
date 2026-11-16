"""Barraquer · informe único de alertas de Google Ads para Obsidian (se sobrescribe cada día).
Uso: python3 -I informe_alertas.py <ads.xlsx> <carpeta_salida> [AAAA-MM-DD]
Lee la hoja "Barraquer - Google Ads diario" (Diario_Campañas, Campañas, Info) y escribe
"<carpeta_salida>/Alertas Google Ads - Barraquer.md" con dos bloques:
  · Ayer: solo incidencias graves del día D (por defecto "Campañas hasta" de Info).
  · Tendencias: últimos 7 días (D-6..D) frente a las 4 semanas anteriores (D-34..D-7),
    y rachas sin conversiones frente a la peor racha de los 60 días anteriores.
Imprime: ruta, nº alertas de ayer (🔴), nº tendencias, fecha de datos, última ejecución."""
import sys, os, datetime as dt
import openpyxl

U = dict(
    MIN_INV_DIA=10,        # media diaria mínima (€) para vigilar una campaña
    CASI_SIN_GASTO=0.2,    # ayer < 20 % de la media de 7 días
    GASTO_DISPARADO=2.0,   # ayer > 2× la media de 7 días...
    MIN_GASTO_DISP=20,     # ...y al menos 20 €
    GASTO_SIN_CONV=3.0,    # ayer 0 conv. con gasto ≥ 3× CPL de 4 semanas
    MIN_CONV_REF=3,        # conversiones mínimas en el periodo de referencia
    MIN_CONV_ESPERADAS=3,  # CPL/CR: el gasto de 7 días debería haber dado ≥ 3 conversiones al CPL de referencia
    RACHA_MIN=3,           # días seguidos con gasto y sin conversiones
    RACHA_GASTO_CPL=2.0,   # gasto de la racha ≥ 2× CPL de referencia
    SIN_CONV_NUNCA=100,    # campaña sin ninguna conversión en 60 días con ≥ 100 € de gasto
    CAIDA_CTR=0.7, MIN_IMP_7D=1000,
    SUBIDA_CPL=1.3,
    CAIDA_CR=0.7, MIN_CLICS_7D=50,
    DIAS_HIST=60,
)
SIN_CONV_TIPOS = {'VIDEO', 'DEMAND_GEN'}  # awareness / consideración: sin reglas de conversión


def fecha(v):
    if isinstance(v, (dt.datetime, dt.date)):
        return v.strftime('%Y-%m-%d')
    return str(v)[:10]


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


def eur(n): return fmt(n, 2) + ' €' if n else '—'
def pct(n): return fmt(n * 100, 2) + ' %' if n else '—'
def ent(n): return fmt(round(n), 0)
def dec(n): return fmt(n, 1 if n % 1 else 0)
def r(a, b): return a / b if b else 0


def var(a, b):
    if not b:
        return '—'
    v = round((a / b - 1) * 100)
    return ('+' if v > 0 else '') + f'{v} %'


def vacio(): return dict(inv=0.0, imp=0.0, cl=0.0, conv=0.0, views=0.0)


def acum(a, b):
    for k in a:
        a[k] += b[k]


def main():
    xlsx, salida = sys.argv[1], sys.argv[2]
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    info = {row[0]: row[1] for row in wb['Info'].iter_rows(min_row=2, values_only=True) if row and row[0]}
    D = sys.argv[3] if len(sys.argv) > 3 else fecha(info.get('Campañas hasta'))
    d0 = dt.date.fromisoformat(D)
    dia = lambda n: (d0 + dt.timedelta(n)).isoformat()
    ult7 = [dia(-k) for k in range(0, 7)]            # D-6..D
    prev7 = [dia(-k) for k in range(1, 8)]           # D-7..D-1 (media diaria para "ayer")
    ref28 = [dia(-k) for k in range(7, 35)]          # D-34..D-7
    hist = [dia(-k) for k in range(U['DIAS_HIST'] - 1, -1, -1)]  # 60 días, ascendente
    yoy7 = [dia(-k - 364) for k in range(0, 7)]
    utiles = set(hist + ref28 + yoy7)

    meta = {}
    for row in wb['Campañas'].iter_rows(min_row=2, values_only=True):
        if row and row[0] is not None:
            meta[ident(row[1]) + '|' + ident(row[3])] = dict(estado=row[4], tipo=row[5], ppto=num(row[7]))

    camp = {}
    for row in wb['Diario_Campañas'].iter_rows(min_row=2, values_only=True):
        if not row or row[0] is None:
            continue
        f = fecha(row[0])
        if f not in utiles:
            continue
        key = ident(row[2]) + '|' + ident(row[4])
        c = camp.setdefault(key, dict(key=key, cuenta=row[1], nombre=row[3], estado=row[5], tipo=row[6], f={}))
        c['f'][f] = dict(inv=num(row[7]), imp=num(row[8]), cl=num(row[9]), conv=num(row[10]), views=num(row[11]))

    def suma(c, fechas):
        t = vacio()
        for f in fechas:
            if f in c['f']:
                acum(t, c['f'][f])
        return t

    varias = len({c['cuenta'] for c in camp.values()}) > 1
    ayer, tend, filas = [], [], []
    tot = dict(hoy=vacio(), prev7=vacio(), u7=vacio(), r28=vacio(), y7=vacio())
    for c in camp.values():
        hoy, p7, u7, r28 = suma(c, [D]), suma(c, prev7), suma(c, ult7), suma(c, ref28)
        acum(tot['hoy'], hoy); acum(tot['prev7'], p7); acum(tot['u7'], u7); acum(tot['r28'], r28)
        acum(tot['y7'], suma(c, yoy7))
        h60 = suma(c, hist)
        if not h60['inv']:
            continue
        m = meta.get(c['key'], {})
        estado, tipo, ppto = m.get('estado', c['estado']), m.get('tipo', c['tipo']), m.get('ppto', 0)
        nom = str((c['cuenta'] + ' · ' if varias else '') + str(c['nombre'])).replace('|', '/')
        conv_ok = tipo not in SIN_CONV_TIPOS
        media = p7['inv'] / 7
        cpl28 = r(r28['inv'], r28['conv']) if r28['conv'] >= U['MIN_CONV_REF'] else 0
        cpl60 = r(h60['inv'], h60['conv']) if h60['conv'] >= U['MIN_CONV_REF'] else 0

        # racha actual de días con gasto y sin conversiones, y peor racha anterior (60 días)
        rachas, racha, g_racha = [], 0, 0.0
        for f in hist:
            x = c['f'].get(f)
            if not x or not x['inv']:
                continue
            if x['conv']:
                if racha:
                    rachas.append(racha)
                racha, g_racha = 0, 0.0
            else:
                racha += 1; g_racha += x['inv']
        peor = max(rachas) if rachas else 0

        if u7['inv'] or hoy['inv']:
            filas.append((nom, hoy, u7, r28, racha if conv_ok else None))

        # ---------- AYER (solo graves) ----------
        if estado == 'ENABLED' and media >= U['MIN_INV_DIA']:
            if not hoy['imp']:
                ayer.append((nom, f"Activa y sin impresiones ayer (gastaba {eur(media)}/día de media)"))
            elif hoy['inv'] < media * U['CASI_SIN_GASTO']:
                ayer.append((nom, f"Casi sin gasto ayer: {eur(hoy['inv'])} frente a {eur(media)}/día de media ({var(hoy['inv'], media)})"))
        if hoy['inv'] >= U['MIN_GASTO_DISP'] and media and hoy['inv'] > media * U['GASTO_DISPARADO']:
            extra = f"; presupuesto diario {eur(ppto)}" if ppto else ''
            ayer.append((nom, f"Gasto disparado: {eur(hoy['inv'])} frente a {eur(media)}/día de media ({var(hoy['inv'], media)}{extra})"))
        if conv_ok and cpl28 and not hoy['conv'] and hoy['inv'] >= cpl28 * U['GASTO_SIN_CONV']:
            ayer.append((nom, f"{eur(hoy['inv'])} en un día sin ninguna conversión ({fmt(hoy['inv'] / cpl28, 1)} veces su CPL de 4 semanas, {eur(cpl28)})"))

        # ---------- TENDENCIAS (7 días vs 4 semanas anteriores) ----------
        if conv_ok:
            if not h60['conv'] and h60['inv'] >= U['SIN_CONV_NUNCA']:
                tend.append((nom, f"Ninguna conversión en {U['DIAS_HIST']} días con {eur(h60['inv'])} de gasto"))
            elif cpl60 and racha >= U['RACHA_MIN'] and racha > peor and g_racha >= cpl60 * U['RACHA_GASTO_CPL']:
                tend.append((nom, f"{racha} días seguidos sin conversiones ({eur(g_racha)}); su peor racha anterior en {U['DIAS_HIST']} días era de {peor}"))
            esperadas = r(u7['inv'], cpl28)
            if cpl28 and u7['conv'] and esperadas >= U['MIN_CONV_ESPERADAS']:
                cpl7 = u7['inv'] / u7['conv']
                if cpl7 > cpl28 * U['SUBIDA_CPL']:
                    tend.append((nom, f"CPL {eur(cpl7)} frente a {eur(cpl28)} ({var(cpl7, cpl28)}; {dec(u7['conv'])} conv. en 7 días)"))
            crU, crR = r(u7['conv'], u7['cl']), r(r28['conv'], r28['cl'])
            if (u7['cl'] >= U['MIN_CLICS_7D'] and u7['conv'] and cpl28 and esperadas >= U['MIN_CONV_ESPERADAS']
                    and crR and crU < crR * U['CAIDA_CR']):
                tend.append((nom, f"CR {pct(crU)} frente a {pct(crR)} ({var(crU, crR)})"))
        ctrU, ctrR = r(u7['cl'], u7['imp']), r(r28['cl'], r28['imp'])
        if u7['imp'] >= U['MIN_IMP_7D'] and ctrR and ctrU < ctrR * U['CAIDA_CTR']:
            tend.append((nom, f"CTR {pct(ctrU)} frente a {pct(ctrR)} ({var(ctrU, ctrR)})"))

    agr = {}
    for a, b in tend:
        agr.setdefault(a, []).append(b)
    tend = [(a, ' · '.join(bs)) for a, bs in agr.items()]
    agr = {}
    for a, b in ayer:
        agr.setdefault(a, []).append(b)
    ayer = [(a, ' · '.join(bs)) for a, bs in agr.items()]

    if not tot['hoy']['imp']:
        ayer.insert(0, ('Cuenta', 'Sin datos de ayer en ninguna campaña: revisar la cuenta o el script de Google Ads'))

    ahora = dt.datetime.now(dt.timezone(dt.timedelta(hours=1))).strftime('%Y-%m-%dT%H:%M')
    hoy_txt = d0.strftime('%d/%m/%Y')
    L = ['---', 'tipo: alertas-google-ads', 'cliente: Barraquer', f'datos-hasta: {D}', f'actualizado: {ahora}',
         f'alertas-ayer: {len(ayer)}', f'tendencias: {len(tend)}',
         f"inversion-ayer: {round(tot['hoy']['inv'], 2)}", f"conversiones-ayer: {round(tot['hoy']['conv'], 2)}",
         'tags: [barraquer, google-ads, alertas]', '---', '',
         '# Alertas Google Ads · Barraquer', '',
         f"> [!{'danger' if ayer else 'success'}] Datos hasta el {hoy_txt}: "
         f"{len(ayer)} {'alerta' if len(ayer) == 1 else 'alertas'} de ayer y "
         f"{len(tend)} {'tendencia' if len(tend) == 1 else 'tendencias'} a vigilar", '',
         f'## 🔴 Ayer ({len(ayer)})', '']
    L += [f'- **{a}** — {b}' for a, b in ayer] or ['Nada grave ayer.']
    L += ['', f'## 📉 Tendencias · últimos 7 días frente a las 4 semanas anteriores ({len(tend)})', '']
    L += [f'- **{a}** — {b}' for a, b in tend] or ['Sin cambios relevantes.']

    # resumen de cuenta
    sem28 = {k: v / 4 for k, v in tot['r28'].items()}
    med7 = {k: v / 7 for k, v in tot['prev7'].items()}
    L += ['', '## Resumen de la cuenta', '',
          '| Métrica | Ayer | Media diaria 7 días previos | vs | Últimos 7 días | Media semanal 4 sem. anteriores | vs | Mismos 7 días año pasado | vs |',
          '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    met = [('Inversión', lambda t: t['inv'], eur, 0), ('Impresiones', lambda t: t['imp'], ent, 0),
           ('Clics', lambda t: t['cl'], ent, 0), ('Conversiones', lambda t: t['conv'], dec, 0),
           ('CTR', lambda t: r(t['cl'], t['imp']), pct, 1), ('CPC', lambda t: r(t['inv'], t['cl']), eur, 1),
           ('CPL', lambda t: r(t['inv'], t['conv']), eur, 1), ('CR', lambda t: r(t['conv'], t['cl']), pct, 1)]
    for nombre, f, fm, ratio in met:
        h, b, u, s, y = f(tot['hoy']), f(med7), f(tot['u7']), f(sem28), f(tot['y7'])
        vh = '—' if ratio and not h else var(h, b)
        vu = '—' if ratio and not u else var(u, s)
        vy = '—' if ratio and not u else var(u, y)
        L.append(f'| {nombre} | {fm(h)} | {fm(b)} | {vh} | {fm(u)} | {fm(s)} | {vu} | {fm(y)} | {vy} |')

    L += ['', '## Campañas · últimos 7 días', '',
          '| Campaña | Inversión ayer | Inversión 7 días | vs 4 sem. | Conv. 7 días | CPL 7 días | CPL 4 sem. | CTR 7 días | Días sin conv. |',
          '|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for nom, h, u, s, rach in sorted(filas, key=lambda x: -x[2]['inv']):
        L.append(f"| {nom} | {eur(h['inv'])} | {eur(u['inv'])} | {var(u['inv'], s['inv'] / 4)} | {dec(u['conv'])} | "
                 f"{eur(r(u['inv'], u['conv']))} | {eur(r(s['inv'], s['conv']))} | {pct(r(u['cl'], u['imp']))} | "
                 f"{'—' if rach is None else rach} |")

    L += ['', '---',
          f"*Informe único que Claude reescribe cada mañana a partir de la hoja «Barraquer - Google Ads diario» "
          f"(última ejecución del script: {info.get('Última ejecución')}). "
          f"**Ayer**: campaña activa sin impresiones o con gasto <{round(U['CASI_SIN_GASTO'] * 100)} % de su media de 7 días; "
          f"gasto >{fmt(U['GASTO_DISPARADO'], 0)}× la media (mín. {U['MIN_GASTO_DISP']} €); "
          f"0 conversiones con gasto ≥{fmt(U['GASTO_SIN_CONV'], 0)}× el CPL de 4 semanas. "
          f"**Tendencias** (7 días frente a 4 semanas): racha sin conversiones más larga que la peor de los últimos {U['DIAS_HIST']} días "
          f"(mín. {U['RACHA_MIN']} días y gasto ≥{fmt(U['RACHA_GASTO_CPL'], 0)}× CPL); CPL >+{round((U['SUBIDA_CPL'] - 1) * 100)} %; "
          f"CR y CTR <−{round((1 - U['CAIDA_CR']) * 100)} % (CPL y CR solo si el gasto daba para ≥{U['MIN_CONV_ESPERADAS']} conversiones). Las campañas de vídeo y Demand Gen no tienen reglas de conversión.*"]

    os.makedirs(salida, exist_ok=True)
    ruta = os.path.join(salida, 'Alertas Google Ads - Barraquer.md')
    with open(ruta, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L) + '\n')
    print(f'{ruta}\t{len(ayer)} alertas ayer\t{len(tend)} tendencias\tdatos hasta {D}\túltima ejecución script {info.get("Última ejecución")}')


if __name__ == '__main__':
    main()
