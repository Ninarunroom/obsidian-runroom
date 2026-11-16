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
el('p', 'muted', `Datos hasta el ${fmtF(D.datos_hasta)}/${D.datos_hasta.slice(0, 4)} · script de Google Ads ejecutado el ${D.ultima_ejecucion}`, root);
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
const pend = [];
const campInfo = new Map(D.campanas.map((r) => [r.campana, r]));
const mini = (parent, items) => { const k = el('div', 'minis', null, parent); for (const [l, v, col] of items) { const b = el('div', 'mini', null, k); el('div', 'eyebrow', l, b); const x = el('div', 'mv', v, b); if (col) x.style.color = col; } };
function barrasGasto(parent, rows, ppto, media) {
  const w = Math.max(260, parent.clientWidth || 420), h = 130, m = { t: 12, r: 4, b: 16, l: 34 };
  const max = Math.max(...rows.map((r) => +r.inversion), ppto || 0, media || 0, 1) * 1.1;
  const svg = svgEl('svg', { viewBox: `0 0 ${w} ${h}`, width: '100%' }, parent);
  const bw = (w - m.l - m.r) / rows.length, Y = (v) => h - m.b - (h - m.t - m.b) * v / max;
  for (const v of [0, max / 2]) { svgEl('line', { x1: m.l, x2: w - m.r, y1: Y(v), y2: Y(v), style: 'stroke:var(--background-modifier-border)' }, svg); const t = svgEl('text', { x: m.l - 4, y: Y(v) + 3, 'text-anchor': 'end' }, svg); t.textContent = nf(v) + ' €'; }
  rows.forEach((r, i) => {
    const last = i === rows.length - 1, v = +r.inversion;
    const b = svgEl('rect', { x: m.l + i * bw + 1, y: Y(v), width: Math.max(1, bw - 2), height: Math.max(0.5, h - m.b - Y(v)), rx: 1.5, style: `fill:${last ? ROJO : AZUL};opacity:${last ? 1 : .55}` }, svg);
    svgEl('title', {}, b).textContent = `${fmtF(r.fecha)}: ${eur(v)} · ${nf(r.impresiones)} impresiones · ${nf(r.conversiones)} conv.`;
    if (i % 7 === 0 || last) { const t = svgEl('text', { x: last ? w - m.r : m.l + i * bw + bw / 2, y: h - 3, 'text-anchor': last ? 'end' : 'middle' }, svg); t.textContent = last ? 'ayer ' + fmtF(r.fecha) : fmtF(r.fecha); }
  });
  const ref = (v, col, lab, left) => { if (!v) return; svgEl('line', { x1: m.l, x2: w - m.r, y1: Y(v), y2: Y(v), style: `stroke:${col};stroke-width:1.2;stroke-dasharray:4 3` }, svg); const t = svgEl('text', { x: left ? m.l + 2 : w - m.r, y: Y(v) - 3, 'text-anchor': left ? 'start' : 'end' }, svg); t.textContent = lab; t.style.fill = col; t.style.fontWeight = '600'; t.style.paintOrder = 'stroke'; t.style.stroke = 'var(--background-secondary)'; t.style.strokeWidth = '3px'; };
  ref(ppto, NARANJA, `presupuesto ${nf(ppto)} €/día`, true);
  ref(media, 'var(--text-muted)', `media 7 días ${nf(media, 1)} €`, false);
}
function cplSemanal(parent, rows, modo = 'cpl') {
  const w = Math.max(260, parent.clientWidth || 420), h = 150, m = { t: 16, r: 18, b: 18, l: 40 };
  const esC = modo === 'conv', u = esC ? '' : ' €', fv = (v) => esC ? nf(v, v % 1 ? 1 : 0) : nf(v) + ' €';
  const pts = rows.map((r) => ({ f: r.semana_fin, cpl: esC ? +r.conversiones : (+r.conversiones ? r.inversion / r.conversiones : null), ly: esC ? +r.conversiones_ly : (+r.conversiones_ly ? r.inversion_ly / r.conversiones_ly : null), inv: +r.inversion, conv: +r.conversiones, invLy: +r.inversion_ly, convLy: +r.conversiones_ly }));
  const vals = pts.flatMap((p) => [p.cpl, p.ly]).filter((v) => v != null).sort((a, b) => a - b);
  const med = vals.length ? vals[Math.floor(vals.length / 2)] : 1;
  const tope = Math.max(med * 2.5, pts[pts.length - 1].cpl || 0, pts[pts.length - 1].ly || 0);
  const max = Math.min(Math.max(...vals, 1), tope) * 1.15;
  const cl = (v) => Math.min(v, max / 1.15);
  const svg = svgEl('svg', { viewBox: `0 0 ${w} ${h}`, width: '100%' }, parent);
  const X = (i) => m.l + i * (w - m.l - m.r) / (pts.length - 1), Y = (v) => h - m.b - (h - m.t - m.b) * v / max;
  svgEl('rect', { x: X(pts.length - 1.5), y: m.t - 10, width: X(pts.length - 1) - X(pts.length - 1.5) + 6, height: h - m.b - m.t + 10, style: 'fill:var(--background-modifier-border);opacity:.5' }, svg);
  for (const v of [0, max / 2, max]) { svgEl('line', { x1: m.l, x2: w - m.r, y1: Y(v), y2: Y(v), style: 'stroke:var(--background-modifier-border)' }, svg); const t = svgEl('text', { x: m.l - 4, y: Y(v) + 3, 'text-anchor': 'end' }, svg); t.textContent = nf(v) + u; }
  const line = (k, col, dash) => { let seg = []; const flush = () => { if (seg.length > 1) svgEl('polyline', { points: seg.join(' '), style: `fill:none;stroke:${col};stroke-width:${dash ? 1.5 : 2.2};${dash ? 'stroke-dasharray:4 3' : ''}` }, svg); seg = []; }; pts.forEach((p, i) => { if (p[k] == null) flush(); else seg.push(`${X(i)},${Y(cl(p[k]))}`); }); flush(); };
  line('ly', GRIS, true); line('cpl', AZUL, false);
  pts.forEach((p, i) => {
    const g = svgEl('g', {}, svg);
    if (p.cpl != null) { svgEl('circle', { cx: X(i), cy: Y(cl(p.cpl)), r: i === pts.length - 1 ? 4.5 : 2.5, style: `fill:${AZUL}` }, g); if (p.cpl > max / 1.15) { const t = svgEl('text', { x: X(i) + 5, y: Y(cl(p.cpl)) + 3 }, g); t.textContent = '↑ ' + fv(p.cpl); t.style.fill = AZUL; } }
    else if (!esC && p.inv > 0) { const t = svgEl('text', { x: X(i), y: m.t - 2, 'text-anchor': 'middle' }, g); t.textContent = '0 conv'; t.style.fill = ROJO; t.style.fontWeight = '600'; }
    if (p.ly != null) svgEl('circle', { cx: X(i), cy: Y(cl(p.ly)), r: 2, style: `fill:${GRIS}` }, g);
    if (i === pts.length - 1) { const lab = (v, col, dy) => { if (v == null) return; const t = svgEl('text', { x: X(i) - 7, y: Y(cl(v)) + dy, 'text-anchor': 'end' }, g); t.textContent = fv(v); t.style.fill = col; t.style.fontWeight = '600'; t.style.paintOrder = 'stroke'; t.style.stroke = 'var(--background-secondary)'; t.style.strokeWidth = '3px'; }; const up = (p.cpl ?? 0) >= (p.ly ?? 0); lab(p.cpl, AZUL, up ? -6 : 12); lab(p.ly, 'var(--text-muted)', up ? 12 : -6); }
    const hit = svgEl('rect', { x: X(i) - 12, y: 0, width: 24, height: h, style: 'fill:transparent' }, g);
    svgEl('title', {}, hit).textContent = `Semana hasta el ${fmtF(p.f)}\n2026: ${eur(p.inv)} · ${nf(p.conv, p.conv % 1 ? 1 : 0)} conv. · CPL ${eur(p.cpl)}\nAño pasado: ${eur(p.invLy)} · ${nf(p.convLy, p.convLy % 1 ? 1 : 0)} conv. · CPL ${eur(p.ly)}`;
    if ((pts.length - 1 - i) % 3 === 0) { const t = svgEl('text', { x: X(i), y: h - 3, 'text-anchor': i === pts.length - 1 ? 'end' : 'middle' }, svg); t.textContent = fmtF(p.f); }
  });
}
const VERED = {
  real: ['Empeora y no es estacional', ROJO],
  estacional: ['Posiblemente estacional: el año pasado pasó lo mismo', NARANJA],
  sin_ly: ['Sin año pasado para comparar', GRIS],
  contexto: ['Racha anómala para esta campaña', ROJO],
};
function tarjetasAyer(g) {
  el('h3', 'sec', '🔴 Ayer: incidencias graves', root);
  el('div', 'muted', 'Barras: gasto diario de las últimas 4 semanas (en rojo, ayer). Línea naranja: presupuesto diario configurado en Google Ads. Línea gris: media de los 7 días anteriores. Pasa el ratón por una barra para ver el día.', root);
  const grid = el('div', 'grid', null, root); grid.style.marginTop = '8px';
  if (!g.length) { el('p', 'muted', 'Nada grave ayer.', grid); return; }
  for (const [camp, items] of g) {
    const c = el('div', 'card alert', null, grid), info = campInfo.get(camp) || {};
    el('div', 'camp', items[0].corto, c);
    for (const it of items) el('div', 'what', it.texto, c);
    const rows = D.serie.filter((r) => r.campana === camp).sort((a, b) => a.fecha < b.fecha ? -1 : 1);
    const tot28 = sum(rows, 'inversion');
    mini(c, [['Gasto ayer', eur(info.inv_ayer), ROJO], ['Media 7 días previos', eur(info.media_7d_previos)], ['Presupuesto diario', eur(info.ppto_diario)], ['Gastado en 28 días', eur(tot28)]]);
    const holder = el('div', null, null, c); pend.push(() => barrasGasto(holder, rows, info.ppto_diario, info.media_7d_previos));
  }
}
function tarjetasTend(g) {
  el('h3', 'sec', '📉 Tendencias: últimos 7 días frente a las 4 semanas anteriores', root);
  const how = el('div', 'how', null, root);
  el('div', null, 'Cómo leer cada tarjeta:', how).style.fontWeight = '600';
  const ul = el('ul', null, null, how);
  el('li', null, 'Arriba, la etiqueta te dice si hay que actuar: rojo = empeora y no pasó lo mismo el año pasado; naranja = el año pasado en estas fechas también empeoró (probablemente estacional).', ul);
  el('li', null, 'Las tres cifras comparan el CPL de la última semana con el de las 4 semanas anteriores y con el de la misma semana del año pasado.', ul);
  el('li', null, 'Con el botón CPL / Conversiones cambias la gráfica. Por defecto es el CPL de cada semana (azul: 2026; gris discontinuo: mismas semanas del año pasado), con el valor de la última semana escrito al lado. La franja sombreada es la última semana. «0 conv» marca semanas con gasto y sin ninguna conversión (sin CPL). Un CPL fuera de escala se marca con ↑ y su valor.', ul);
  const grid = el('div', 'grid', null, root); grid.style.marginTop = '8px';
  if (!g.length) { el('p', 'muted', 'Sin tendencias relevantes.', grid); return; }
  const orden = { real: 0, contexto: 1, sin_ly: 2, estacional: 3 };
  g.sort((a, b) => orden[a[1][0].veredicto] - orden[b[1][0].veredicto]);
  for (const [camp, items] of g) {
    const v = VERED[items[0].veredicto] || VERED.contexto, info = campInfo.get(camp) || {};
    const c = el('div', 'card alert tend', null, grid); c.style.borderLeftColor = v[1];
    const badge = el('span', 'badge', v[0], c); badge.style.color = v[1]; badge.style.borderColor = v[1];
    el('div', 'camp', items[0].corto, c);
    for (const it of items) { const w = el('div', 'what', it.texto, c); if (it.contexto_ly) el('div', 'muted', '↳ ' + it.contexto_ly, w).style.fontSize = 'var(--font-ui-smaller)'; }
    const cpl = (i, n) => +n ? +i / +n : null;
    mini(c, [['CPL última semana', eur(cpl(info.inv_7d, info.conv_7d)), v[1]], ['CPL 4 semanas antes', eur(cpl(info.inv_4sem, info.conv_4sem))], ['CPL misma semana año pasado', eur(cpl(info.inv_ly_7d, info.conv_ly_7d))]]);
    const rows = D.semanas.filter((r) => r.campana === camp).sort((a, b) => a.semana_fin < b.semana_fin ? -1 : 1);
    if (rows.length) {
      const sw = el('div', 'switch', null, c);
      const bC = el('button', 'on', 'CPL', sw), bV = el('button', null, 'Conversiones', sw);
      const tit = el('div', 'eyebrow', 'CPL por semana (€), últimas 8 semanas', c);
      const lg2 = el('div', 'legend', null, c);
      const a1 = el('span', null, null, lg2); el('i', null, null, a1).style.background = AZUL; a1.append('2026');
      const a2 = el('span', null, null, lg2); el('i', null, null, a2).style.background = GRIS; a2.append('mismas semanas del año pasado');
      const holder = el('div', null, null, c); pend.push(() => cplSemanal(holder, rows));
      const ver = (modo) => { holder.replaceChildren(); cplSemanal(holder, rows, modo); bC.classList.toggle('on', modo === 'cpl'); bV.classList.toggle('on', modo === 'conv'); tit.textContent = modo === 'cpl' ? 'CPL por semana (€), últimas 8 semanas' : 'Conversiones por semana, últimas 8 semanas'; };
      bC.onclick = () => ver('cpl'); bV.onclick = () => ver('conv');
    }
    el('div', 'muted', `CPL = inversión ÷ conversiones de cada semana (bloques de 7 días hasta ayer). Última semana: ${eur(info.inv_7d)} ÷ ${nf(info.conv_7d, info.conv_7d % 1 ? 1 : 0)} conversiones. Lleva ${info.dias_sin_conv ?? 0} días seguidos sin conversión (su peor racha en 60 días: ${info.peor_racha_60d ?? '—'}).`, c).style.fontSize = 'var(--font-ui-smaller)';
  }
}
el('style', null, `
.rr-alertas .minis { display: grid; grid-template-columns: repeat(auto-fit, minmax(90px, 1fr)); gap: 8px; }
.rr-alertas .mini { background: var(--background-primary); border: 1px solid var(--background-modifier-border); border-radius: 6px; padding: 6px 8px; }
.rr-alertas .mini .mv { font-weight: 600; font-variant-numeric: tabular-nums; }
.rr-alertas .what { font-size: var(--font-ui-small); }
.rr-alertas .badge { align-self: flex-start; font-size: var(--font-ui-smaller); font-weight: 600; padding: 1px 8px; border-radius: 999px; border: 1px solid; }
.rr-alertas .switch { display: inline-flex; align-self: flex-start; border: 1px solid var(--background-modifier-border); border-radius: 6px; overflow: hidden; margin-top: 4px; }
.rr-alertas .switch button { all: unset; cursor: pointer; font-size: var(--font-ui-smaller); padding: 3px 10px; color: var(--text-muted); }
.rr-alertas .switch button.on { background: ${AZUL}; color: white; font-weight: 600; }
.rr-alertas .how { font-size: var(--font-ui-small); border-left: 3px solid var(--background-modifier-border); padding: 4px 10px; margin: 4px 0 6px; }
.rr-alertas .how ul { margin: 4px 0 0; padding-left: 1.1em; }
`, root);
tarjetasAyer(gA);
tarjetasTend(gT);
pend.forEach((f) => f());

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
  vals.forEach((v, i) => { const td = el('td', null, String(v), tr); if (i === 7 && r.dias_sin_conv >= 3 && r.peor_racha_60d > 0 && r.dias_sin_conv > r.peor_racha_60d) td.className = 'bad'; });
}
```

> [!info] Cómo funciona
> Cada mañana laborable (9:45) Claude lee el Google Sheet «Barraquer - Google Ads diario» y regenera `Claude/Alertas/datos-alertas-google-ads.json`, que es lo que pinta este panel (script: `Claude/Scripts/datos_panel_alertas.py`). Necesita el plugin Dataview con JavaScript activado.
> **Ayer**: campaña activa sin impresiones o con gasto < 20 % de su media de 7 días · gasto > 2× la media (mín. 20 €) · 0 conversiones con gasto ≥ 3× su CPL de 4 semanas.
> **Tendencias** (últimos 7 días frente a las 4 semanas anteriores): racha sin conversiones más larga que la peor de los últimos 60 días · sin conversiones en 60 días con ≥ 100 € · CPL +30 % · CR −30 % · CTR −30 %. Cada una se compara con las mismas fechas del año pasado para ver si es estacional. Vídeo y Demand Gen no tienen reglas de conversión.
