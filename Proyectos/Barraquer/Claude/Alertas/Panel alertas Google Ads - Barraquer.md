---
tipo: panel
cliente: "[[00 Ficha de cliente - Barraquer]]"
tags: [barraquer, google-ads, alertas, panel]
---
# Panel de alertas Google Ads — Barraquer

```dataviewjs
const _f = dv.current().file.folder; const base = _f.slice(0, _f.indexOf('Barraquer') + 'Barraquer'.length);
const root = dv.container; root.classList.add('rr-panel', 'rr-alertas');
const el = (tag, cls, txt, parent) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; if (parent) parent.appendChild(e); return e; };
let D;
try { D = JSON.parse(await dv.io.load(`${base}/Claude/Alertas/datos-alertas-google-ads.json`)); }
catch (e) { el('p', null, 'No se encuentran los datos (Claude/Alertas/datos-alertas-google-ads.json).', root); return; }
const NARANJA = 'hsl(32, 85%, 52%)', AZUL = 'hsl(210, 70%, 52%)', ROJO = 'hsl(0, 70%, 52%)', VERDE = 'hsl(125, 55%, 45%)', GRIS = 'var(--text-faint)';
const nf = (n, d = 0) => (n == null || isNaN(n)) ? '—' : Number(n).toLocaleString('es-ES', { minimumFractionDigits: d, maximumFractionDigits: d });
const eur = (n) => (n == null || isNaN(n) || !isFinite(n)) ? '—' : nf(n, 2) + ' €';
const pct = (n) => (n == null || isNaN(n) || !isFinite(n)) ? '—' : (n > 0 ? '+' : '') + Math.round(n) + ' %';
const fmtF = (s) => s.slice(8, 10) + '/' + s.slice(5, 7);
const sum = (rows, f) => rows.reduce((s, x) => s + (+x[f] || 0), 0);
el('style', null, `
.rr-alertas { --g: 12px; }
.rr-alertas .card { border: 1px solid var(--background-modifier-border); border-radius: 10px; padding: 14px 16px; background: var(--background-secondary); display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.rr-alertas .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 14px; margin-bottom: 18px; }
.rr-alertas .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 18px; }
.rr-alertas .kpi { border: 1px solid var(--background-modifier-border); border-radius: 8px; padding: 10px 12px; background: var(--background-primary); }
.rr-alertas .kpi .v { font-size: 1.6em; font-weight: 600; font-variant-numeric: tabular-nums; margin: 2px 0; }
.rr-alertas .eyebrow { font-size: var(--font-ui-smaller); text-transform: uppercase; letter-spacing: .05em; color: var(--text-muted); }
.rr-alertas .muted { color: var(--text-muted); font-size: var(--font-ui-small); }
.rr-alertas h3.sec { margin: 6px 0 4px; }
.rr-alertas .lead { font-size: var(--font-ui-medium); margin: 0 0 14px; }
.rr-alertas .alert { border-left: 4px solid ${ROJO}; }
.rr-alertas .alert.tend { border-left-color: ${NARANJA}; }
.rr-alertas .camp { font-weight: 600; overflow-wrap: anywhere; }
.rr-alertas ul.items { margin: 0; padding-left: 1.1em; font-size: var(--font-ui-small); display: flex; flex-direction: column; gap: 6px; }
.rr-alertas .chip { display: inline-block; margin-top: 3px; font-size: var(--font-ui-smaller); padding: 1px 8px; border-radius: 999px; border: 1px solid var(--background-modifier-border); color: var(--text-muted); }
.rr-alertas .chip.seas { border-color: ${NARANJA}; color: ${NARANJA}; }
.rr-alertas .chip.real { border-color: ${ROJO}; color: ${ROJO}; }
.rr-alertas .cpl { display: grid; grid-template-columns: auto 1fr auto; gap: 3px 8px; align-items: center; font-size: var(--font-ui-smaller); font-variant-numeric: tabular-nums; }
.rr-alertas .cpl .bar { height: 9px; border-radius: 3px; }
.rr-alertas svg text { fill: var(--text-muted); font-size: 10px; }
.rr-alertas .legend { display: flex; gap: 14px; flex-wrap: wrap; font-size: var(--font-ui-smaller); color: var(--text-muted); }
.rr-alertas .legend i { display: inline-block; width: 14px; height: 3px; vertical-align: middle; margin-right: 4px; }
.rr-alertas .scroll { overflow-x: auto; }
.rr-alertas table.t { display: table; width: 100% !important; border-collapse: collapse; font-size: var(--font-ui-small); font-variant-numeric: tabular-nums; margin: 0; }
.rr-alertas table.t th, .rr-alertas table.t td { border: none !important; border-bottom: 1px solid var(--background-modifier-border) !important; background: transparent !important; text-align: right; padding: 4px 8px; white-space: nowrap; }
.rr-alertas table.t th { color: var(--text-muted); font-weight: 500; font-size: var(--font-ui-smaller); }
.rr-alertas table.t th:first-child, .rr-alertas table.t td:first-child { text-align: left; }
.rr-alertas td.bad { color: ${ROJO}; font-weight: 600; }
`, root);

// ───── Cabecera ─────
const grupos = (b) => { const m = new Map(); D.alertas.filter((a) => a.bloque === b).forEach((a) => { if (!m.has(a.campana)) m.set(a.campana, []); m.get(a.campana).push(a); }); return [...m.entries()]; };
const gA = grupos('ayer'), gT = grupos('tendencia');
el('p', 'muted', `Datos hasta el ${fmtF(D.datos_hasta)}/${D.datos_hasta.slice(0, 4)} · script de Google Ads ejecutado el ${D.ultima_ejecucion} · detalle en texto: [[Alertas Google Ads - Barraquer]]`, root);
el('p', 'lead', `Ayer hubo ${gA.length} ${gA.length === 1 ? 'incidencia grave' : 'incidencias graves'} y hay ${gT.length} ${gT.length === 1 ? 'campaña' : 'campañas'} con tendencias a vigilar en los últimos 7 días.`, root);

// ───── KPIs ─────
const C = D.cuenta.slice().sort((a, b) => a.fecha < b.fecha ? -1 : 1), n = C.length;
const ayer = C[n - 1], prev7 = C.slice(n - 8, n - 1), u7 = C.slice(n - 7), r28 = C.slice(n - 35, n - 7);
const cpl7 = sum(u7, 'inversion') / sum(u7, 'conversiones'), cpl28 = sum(r28, 'inversion') / sum(r28, 'conversiones'), cplLY = sum(u7, 'inversion_ly') / sum(u7, 'conversiones_ly');
const kp = el('div', 'kpis', null, root);
const kpi = (l, v, sub, col) => { const k = el('div', 'kpi', null, kp); el('div', 'eyebrow', l, k); el('div', 'v', v, k); const s = el('div', 'muted', sub, k); if (col) s.style.color = col; };
const colVar = (v) => v > 10 ? ROJO : v < -10 ? VERDE : null;
kpi('Inversión ayer', eur(ayer.inversion), `media 7 días previos: ${eur(sum(prev7, 'inversion') / 7)}`);
kpi('Conversiones ayer', nf(ayer.conversiones), `media 7 días previos: ${nf(sum(prev7, 'conversiones') / 7, 1)}`);
const v28 = (cpl7 / cpl28 - 1) * 100, vLY = (cpl7 / cplLY - 1) * 100;
kpi('CPL últimos 7 días', eur(cpl7), `${pct(v28)} vs 4 semanas anteriores (${eur(cpl28)})`, colVar(v28));
kpi('CPL mismos 7 días año pasado', eur(cplLY), `el CPL de ahora es un ${pct(vLY)} vs el año pasado`, colVar(vLY));

// ───── SVG helpers ─────
const NS = 'http://www.w3.org/2000/svg';
const svgEl = (tag, attrs, parent) => { const e = document.createElementNS(NS, tag); for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v); if (parent) parent.appendChild(e); return e; };
function spark(parent, rows, f, col) {
  const w = 300, h = 50, m = 3, max = Math.max(...rows.map((r) => +r[f]), 1);
  const svg = svgEl('svg', { viewBox: `0 0 ${w} ${h}`, width: '100%', height: h, preserveAspectRatio: 'none' }, parent);
  const X = (i) => m + i * (w - 2 * m) / (rows.length - 1), Y = (v) => h - m - (h - 2 * m) * v / max;
  const pts = rows.map((r, i) => `${X(i)},${Y(+r[f])}`).join(' ');
  svgEl('polygon', { points: `${X(0)},${h - m} ${pts} ${X(rows.length - 1)},${h - m}`, style: `fill:${col};opacity:.12` }, svg);
  svgEl('polyline', { points: pts, style: `fill:none;stroke:${col};stroke-width:1.5`, 'vector-effect': 'non-scaling-stroke' }, svg);
}

// ───── Tarjetas ─────
function tarjetas(titulo, nota, g, tend) {
  el('h3', 'sec', titulo, root); el('div', 'muted', nota, root);
  const grid = el('div', 'grid', null, root); grid.style.marginTop = '8px';
  if (!g.length) { el('p', 'muted', tend ? 'Sin tendencias relevantes.' : 'Nada grave ayer.', grid); return; }
  for (const [camp, items] of g) {
    const c = el('div', 'card alert' + (tend ? ' tend' : ''), null, grid);
    el('div', 'camp', items[0].corto, c);
    const ul = el('ul', 'items', null, c);
    for (const it of items) {
      const li = el('li', null, it.texto, ul);
      if (it.contexto_ly) { el('br', null, null, li); el('span', 'chip ' + (/^Posible/.test(it.contexto_ly) ? 'seas' : /^No parece/.test(it.contexto_ly) ? 'real' : ''), it.contexto_ly, li); }
    }
    const ci = items.find((i) => i.regla === 'cpl');
    if (ci) {
      const vals = [['4 sem. antes', ci.cpl_4sem, GRIS], ['Últimos 7 días', ci.cpl_7d, AZUL], ['Año pasado · 4 sem.', ci.cpl_ly_4sem, GRIS], ['Año pasado · 7 días', ci.cpl_ly_7d, NARANJA]];
      const mx = Math.max(...vals.map((v) => v[1] || 0), 1), box = el('div', 'cpl', null, c);
      for (const [l, v, col] of vals) { el('span', null, l, box); const b = el('div', 'bar', null, box); b.style.width = `${(v || 0) / mx * 100}%`; b.style.background = col; el('span', null, eur(v), box); }
    }
    const rows = D.serie.filter((r) => r.campana === camp).sort((a, b) => a.fecha < b.fecha ? -1 : 1);
    if (rows.length) {
      const f = items.some((i) => ['racha', 'cpl', 'cr', 'nunca_convierte', 'gasto_sin_conv'].includes(i.regla)) ? 'conversiones' : items.some((i) => i.regla === 'sin_impresiones') ? 'impresiones' : 'inversion';
      spark(c, rows, f, f === 'conversiones' ? NARANJA : AZUL);
      el('div', 'muted', `${f === 'conversiones' ? 'Conversiones' : f === 'impresiones' ? 'Impresiones' : 'Inversión'} diarias · ${fmtF(rows[0].fecha)} – ${fmtF(rows[rows.length - 1].fecha)}`, c).style.fontSize = 'var(--font-ui-smaller)';
    }
  }
}
tarjetas('🔴 Ayer: incidencias graves', 'Campaña activa sin impresiones o con menos del 20 % de su gasto medio · gasto de más del doble de su media · 0 conversiones con un gasto de 3 veces su CPL.', gA, false);
tarjetas('📉 Tendencias: últimos 7 días frente a las 4 semanas anteriores', 'Cada tendencia se compara con las mismas fechas del año pasado para ver si es estacional. Las barras comparan el CPL de ahora con el del año pasado.', gT, true);

// ───── Gráficas de la cuenta ─────
el('h3', 'sec', 'La cuenta día a día: últimos 60 días frente al año pasado', root);
const lg = el('div', 'legend', null, root);
const li1 = el('span', null, null, lg); el('i', null, null, li1).style.background = AZUL; li1.append('2026');
const li2 = el('span', null, null, lg); el('i', null, null, li2).style.background = GRIS; li2.append('Mismo día de la semana, año pasado');
const gc = el('div', 'grid', null, root); gc.style.marginTop = '8px';
function lineas(titulo, f, fmt) {
  const c = el('div', 'card', null, gc); el('div', 'eyebrow', titulo, c);
  const w = 460, h = 200, m = { t: 8, r: 6, b: 18, l: 44 };
  const svg = svgEl('svg', { viewBox: `0 0 ${w} ${h}`, width: '100%' }, c);
  const max = Math.max(...C.map((r) => Math.max(+r[f], +r[f + '_ly']))) * 1.05;
  const X = (i) => m.l + i * (w - m.l - m.r) / (C.length - 1), Y = (v) => h - m.b - (h - m.t - m.b) * v / max;
  for (let k = 0; k <= 4; k++) { const v = max * k / 4; svgEl('line', { x1: m.l, x2: w - m.r, y1: Y(v), y2: Y(v), style: 'stroke:var(--background-modifier-border);stroke-width:1' }, svg); const t = svgEl('text', { x: m.l - 4, y: Y(v) + 3, 'text-anchor': 'end' }, svg); t.textContent = fmt(v); }
  for (let i = 0; i < C.length; i += 10) { const t = svgEl('text', { x: X(i), y: h - 4, 'text-anchor': 'middle' }, svg); t.textContent = fmtF(C[i].fecha); }
  svgEl('polyline', { points: C.map((r, i) => `${X(i)},${Y(+r[f + '_ly'])}`).join(' '), style: `fill:none;stroke:${GRIS};stroke-width:1.5;stroke-dasharray:4 3` }, svg);
  svgEl('polyline', { points: C.map((r, i) => `${X(i)},${Y(+r[f])}`).join(' '), style: `fill:none;stroke:${AZUL};stroke-width:2` }, svg);
  C.forEach((r, i) => { const hit = svgEl('rect', { x: X(i) - (w - m.l) / C.length / 2, y: m.t, width: (w - m.l) / C.length, height: h - m.t - m.b, style: 'fill:transparent' }, svg); const tt = svgEl('title', {}, hit); tt.textContent = `${fmtF(r.fecha)}: ${f === 'inversion' ? eur(r[f]) : nf(r[f])} (año pasado: ${f === 'inversion' ? eur(r[f + '_ly']) : nf(r[f + '_ly'])})`; });
  svgEl('circle', { cx: X(C.length - 1), cy: Y(+C[C.length - 1][f]), r: 3.5, style: `fill:${AZUL}` }, svg);
}
lineas('Inversión diaria', 'inversion', (v) => nf(v) + ' €');
lineas('Conversiones diarias', 'conversiones', (v) => nf(v));

// ───── Tabla ─────
el('h3', 'sec', 'Campañas', root);
el('div', 'muted', 'Ordenadas por inversión de los últimos 7 días. En rojo, rachas sin conversión más largas que la peor de los últimos 60 días.', root);
const w = el('div', 'scroll', null, root); const t = el('table', 't', null, w);
const hr = el('tr', null, null, el('thead', null, null, t));
for (const x of ['Campaña', 'Inversión ayer', 'Inversión 7 días', 'Conv. 7 días', 'CPL 7 días', 'CPL 4 sem.', 'CPL año pasado', 'Días sin conv.', 'Peor racha 60 días']) el('th', null, x, hr);
const tb = el('tbody', null, null, t);
const cpl = (i, c) => +c ? +i / +c : null;
for (const r of D.campanas.slice().sort((a, b) => b.inv_7d - a.inv_7d)) {
  const tr = el('tr', null, null, tb);
  const vals = [r.corto, eur(r.inv_ayer), eur(r.inv_7d), nf(r.conv_7d, r.conv_7d % 1 ? 1 : 0), eur(cpl(r.inv_7d, r.conv_7d)), eur(cpl(r.inv_4sem, r.conv_4sem)), eur(cpl(r.inv_ly_7d, r.conv_ly_7d)), r.dias_sin_conv ?? '—', r.peor_racha_60d ?? '—'];
  vals.forEach((v, i) => { const td = el('td', null, String(v), tr); if (i === 7 && r.dias_sin_conv >= 3 && r.dias_sin_conv > r.peor_racha_60d) td.className = 'bad'; });
}
```

> [!info] Cómo funciona
> El panel lee `Claude/Alertas/datos-alertas-google-ads.json`, que Claude genera a partir del Google Sheet «Barraquer - Google Ads diario». Necesita el plugin Dataview con JavaScript activado, igual que los paneles de 4. Seguimiento. El detalle en texto y las reglas están en [[Alertas Google Ads - Barraquer]].
