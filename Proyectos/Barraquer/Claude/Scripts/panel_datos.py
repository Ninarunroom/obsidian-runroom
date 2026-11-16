"""Barraquer · datos del panel de alertas de Google Ads (Obsidian).
Uso: python3 -I panel_datos.py <ads.xlsx> <salida.json>
Lee la hoja "Barraquer - Google Ads diario" y escribe el JSON que lee
"Panel alertas Google Ads - Barraquer.md" (alertas con contexto del año pasado,
campañas, serie diaria y semanal de las campañas con alerta, y totales de la cuenta)."""
import openpyxl, datetime as dt, json, sys
from collections import defaultdict
wb=openpyxl.load_workbook(sys.argv[1],read_only=True,data_only=True)
info={r[0]:r[1] for r in wb['Info'].iter_rows(min_row=2,values_only=True) if r and r[0]}
D=info['Campañas hasta'].date()
day=lambda n:D+dt.timedelta(n)
ult7=[day(-k) for k in range(7)]; prev7=[day(-k) for k in range(1,8)]; ref28=[day(-k) for k in range(7,35)]
hist=[day(-k) for k in range(59,-1,-1)]
ly=lambda ds:[x-dt.timedelta(364) for x in ds]
meta={}
for r in wb['Campañas'].iter_rows(min_row=2,values_only=True):
    if r and r[0]: meta[int(float(r[3]))]=dict(estado=r[4],tipo=r[5],ppto=float(r[7] or 0))
c=defaultdict(dict); nom={}; tipo={}
for r in wb['Diario_Campañas'].iter_rows(min_row=2,values_only=True):
    if not r or not r[0]: continue
    f=r[0].date(); k=int(float(r[4])); nom[k]=r[3]; tipo[k]=r[6]
    c[k][f]=[float(r[i] or 0) for i in (7,8,9,10)]
def S(k,ds):
    t=[0,0,0,0]
    for x in ds:
        v=c[k].get(x)
        if v: t=[a+b for a,b in zip(t,v)]
    return dict(inv=t[0],imp=t[1],cl=t[2],conv=t[3])
R=lambda a,b:a/b if b else None
def pc(a,b): return None if not a or not b else round((a/b-1)*100)
eur=lambda n:f"{n:,.2f} €".replace(',','X').replace('.',',').replace('X','.')
camps=[]; alertas=[]; serie=[]
for k in nom:
    h60=S(k,hist)
    if not h60['inv']: continue
    m=meta.get(k,{}); est=m.get('estado'); tp=m.get('tipo',tipo[k]); conv_ok=tp not in('VIDEO','DEMAND_GEN')
    hoy,p7,u7,r28,l7,l28=S(k,[D]),S(k,prev7),S(k,ult7),S(k,ref28),S(k,ly(ult7)),S(k,ly(ref28))
    media=p7['inv']/7
    cpl28=R(r28['inv'],r28['conv']) if r28['conv']>=3 else None
    cpl60=R(h60['inv'],h60['conv']) if h60['conv']>=3 else None
    rachas=[];racha=0;g=0
    for x in hist:
        v=c[k].get(x)
        if not v or not v[0]: continue
        if v[3]:
            if racha: rachas.append(racha)
            racha=0;g=0
        else: racha+=1;g+=v[0]
    peor=max(rachas) if rachas else 0
    n=nom[k]; corto=n.replace('google_clinica_','').replace('search_conversion_','search · ').replace('pmax_conversion_','pmax · ').replace('youtube_awareness_','youtube · ').replace('demand-gen_consideracion_','demand gen · ')
    A=[]
    if est=='ENABLED' and media>=10:
        if not hoy['imp']: A.append(('ayer','sin_impresiones',f"Activa y sin impresiones ayer (gastaba {eur(media)}/día de media)"))
        elif hoy['inv']<media*0.2: A.append(('ayer','casi_sin_gasto',f"Casi sin gasto ayer: {eur(hoy['inv'])} frente a {eur(media)}/día de media"))
    if hoy['inv']>=20 and media and hoy['inv']>media*2: A.append(('ayer','gasto_disparado',f"Gasto disparado: {eur(hoy['inv'])} frente a {eur(media)}/día de media"))
    if conv_ok and cpl28 and not hoy['conv'] and hoy['inv']>=cpl28*3: A.append(('ayer','gasto_sin_conv',f"{eur(hoy['inv'])} en un día sin conversiones ({hoy['inv']/cpl28:.1f} veces su CPL)"))
    cpl7=R(u7['inv'],u7['conv']); cplL7=R(l7['inv'],l7['conv']); cplL28=R(l28['inv'],l28['conv'])
    crU,crR=R(u7['conv'],u7['cl']),R(r28['conv'],r28['cl']); crL7,crL28=R(l7['conv'],l7['cl']),R(l28['conv'],l28['cl'])
    def estac(now,ref,lnow,lref,sube=True):
        if lnow is None or lref is None or not l28['inv'] or not l7['inv']: return 'Sin datos del año pasado'
        ch=(lnow/lref-1)*100
        if (sube and ch>=20) or (not sube and ch<=-20): return f"Posible estacionalidad: el año pasado también {'subió' if sube else 'bajó'} ({ch:+.0f} %)"
        return f"No parece estacional: el año pasado {'subió' if ch>0 else 'bajó'} un {abs(ch):.0f} % en las mismas fechas"
    if conv_ok:
        if not h60['conv'] and h60['inv']>=100: A.append(('tendencia','nunca_convierte',f"Ninguna conversión en 60 días con {eur(h60['inv'])} de gasto",'Campaña sin histórico del año pasado' if not l28['inv'] else ''))
        elif cpl60 and racha>=3 and racha>peor and g>=cpl60*2:
            A.append(('tendencia','racha',f"{racha} días seguidos sin conversiones ({eur(g)}); su peor racha en 60 días era de {peor}",
                      'Sin datos del año pasado' if not l7['inv'] else f"Mismas fechas del año pasado: {l7['conv']:.0f} conv. en 7 días con {eur(l7['inv'])}"))
        esp=R(u7['inv'],cpl28) or 0
        if cpl28 and u7['conv'] and esp>=3 and cpl7>cpl28*1.3:
            A.append(('tendencia','cpl',f"CPL {eur(cpl7)} frente a {eur(cpl28)} ({pc(cpl7,cpl28):+d} %)",estac(cpl7,cpl28,cplL7,cplL28,True)))
        if u7['cl']>=50 and u7['conv'] and cpl28 and esp>=3 and crR and crU<crR*0.7:
            A.append(('tendencia','cr',f"CR {crU*100:.2f} % frente a {crR*100:.2f} % ({pc(crU,crR):+d} %)".replace('.',','),estac(crU,crR,crL7,crL28,False)))
    ctrU,ctrR=R(u7['cl'],u7['imp']),R(r28['cl'],r28['imp'])
    if u7['imp']>=1000 and ctrR and ctrU<ctrR*0.7:
        A.append(('tendencia','ctr',f"CTR {ctrU*100:.2f} % frente a {ctrR*100:.2f} % ({pc(ctrU,ctrR):+d} %)".replace('.',','),estac(ctrU,ctrR,R(l7['cl'],l7['imp']),R(l28['cl'],l28['imp']),False)))
    for a in A:
        alertas.append(dict(campana=n,corto=corto,bloque=a[0],regla=a[1],texto=a[2],contexto_ly=(a[3] if len(a)>3 else ''),
            cpl_7d=round(cpl7,2) if cpl7 else None, cpl_4sem=round(R(r28['inv'],r28['conv']),2) if r28['conv'] else None,
            cpl_ly_7d=round(cplL7,2) if cplL7 else None, cpl_ly_4sem=round(cplL28,2) if cplL28 else None))
    if u7['inv'] or hoy['inv']:
        camps.append(dict(campana=n,corto=corto,tipo=tp,estado=est,ppto_diario=m.get('ppto'),inv_ayer=round(hoy['inv'],2),imp_ayer=int(hoy['imp']),conv_ayer=hoy['conv'],
          media_7d_previos=round(media,2),inv_7d=round(u7['inv'],2),conv_7d=u7['conv'],clics_7d=int(u7['cl']),imp_7d=int(u7['imp']),
          inv_4sem=round(r28['inv'],2),conv_4sem=r28['conv'],clics_4sem=int(r28['cl']),imp_4sem=int(r28['imp']),
          inv_ly_7d=round(l7['inv'],2),conv_ly_7d=l7['conv'],inv_ly_4sem=round(l28['inv'],2),conv_ly_4sem=l28['conv'],
          dias_sin_conv=racha if conv_ok else None,peor_racha_60d=peor if conv_ok else None))
flag={a['campana'] for a in alertas}
semanas=[]
for k in nom:
    if nom[k] not in flag: continue
    for w in range(7,-1,-1):
        ds=[day(-(w*7+i)) for i in range(7)]
        a=S(k,ds); b=S(k,ly(ds))
        semanas.append(dict(campana=nom[k],semana_fin=ds[0].isoformat(),inversion=round(a['inv'],2),conversiones=a['conv'],clics=int(a['cl']),
            inversion_ly=round(b['inv'],2),conversiones_ly=b['conv'],clics_ly=int(b['cl'])))
veredictos={}
for a in alertas:
    if a['bloque']!='tendencia': continue
    v=veredictos.setdefault(a['campana'],set())
    t=a['contexto_ly']
    v.add('real' if t.startswith('No parece') else 'estacional' if t.startswith('Posible') else 'sin_ly' if t.startswith(('Sin datos','Campaña sin')) else 'contexto')
for a in alertas:
    v=veredictos.get(a['campana'],set())
    a['veredicto']='real' if 'real' in v else 'estacional' if 'estacional' in v else 'sin_ly' if 'sin_ly' in v else 'contexto'
for k in nom:
    if nom[k] in flag:
        for x in [day(-i) for i in range(27,-1,-1)]:
            v=c[k].get(x,[0,0,0,0]); serie.append(dict(campana=nom[k],fecha=x.isoformat(),inversion=round(v[0],2),impresiones=int(v[1]),conversiones=v[3]))
cuenta=[]
for x in hist:
    t=[0]*4; tl=[0]*4
    for k in c:
        v=c[k].get(x); vl=c[k].get(x-dt.timedelta(364))
        if v: t=[a+b for a,b in zip(t,v)]
        if vl: tl=[a+b for a,b in zip(tl,vl)]
    cuenta.append(dict(fecha=x.isoformat(),inversion=round(t[0],2),clics=int(t[2]),impresiones=int(t[1]),conversiones=round(t[3],2),
        inversion_ly=round(tl[0],2),conversiones_ly=round(tl[3],2)))
out={'datos_hasta':D.isoformat(),'ultima_ejecucion':str(info.get('Última ejecución'))[:16],'generado':dt.date.today().isoformat(),
     'alertas':alertas,'campanas':camps,'serie':serie,'cuenta':cuenta,'semanas':semanas}
import os
os.makedirs(os.path.dirname(sys.argv[2]) or '.', exist_ok=True)
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False)
print(f"{sys.argv[2]}\t{len(alertas)} alertas\t{len(semanas)} filas semanales\tdatos hasta {D}")
