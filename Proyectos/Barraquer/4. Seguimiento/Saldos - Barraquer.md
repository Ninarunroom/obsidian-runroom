# Saldos — Barraquer

Saldo de la cuenta general de Google Ads: **una sola recarga cubre Clínica y Estética**. La recarga la hace Cristian. Te llega un email si el saldo baja del umbral o dura menos de los días indicados.

```dataviewjs
const _f = dv.current().file.folder; const base = _f.slice(0, _f.indexOf('Barraquer') + 'Barraquer'.length);
const nota = (n) => dv.pages(`"${base}"`).where((p) => p.file.name === n).first();
const D = nota('Datos panel - Barraquer') ?? {};
const eur = (n) => (n == null || isNaN(n)) ? '—' : (n < 0 ? '−' : '') + String(Math.round(Math.abs(n))).replace(/\B(?=(\d{3})+(?!\d))/g, '.') + ' €';
const sgn = (n) => `${n >= 0 ? '+' : '−'}${eur(Math.abs(n))}`;
const color = (p) => p <= 0 ? 'var(--background-modifier-border)' : `hsl(${Math.round(Math.min(p, 100) * 1.25)}, 62%, 46%)`;
const NARANJA = 'hsl(32, 85%, 52%)', AZUL = 'hsl(210, 70%, 52%)', ROJO = 'hsl(0, 70%, 52%)', VERDE = 'hsl(125, 55%, 45%)';
const MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
const arr = (k) => Array.from(D[k] ?? []).map(Number);
const root = dv.container; root.classList.add('rr-panel');
const el = (tag, cls, txt, parent) => { const e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; if (parent) parent.appendChild(e); return e; };
el('style', null, `
.rr-panel { --g: 12px; }
.rr-panel .card { border: 1px solid var(--background-modifier-border); border-radius: 10px; padding: 16px; background: var(--background-secondary); display: flex; flex-direction: column; gap: var(--g); min-width: 0; margin-bottom: 16px; }
.rr-panel .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px; }
.rr-panel .grid { margin-bottom: 16px; }
.rr-panel .grid > .card { margin-bottom: 0; }
.rr-panel .global { flex-direction: row; flex-wrap: wrap; gap: 24px; align-items: center; }
.rr-panel .big { font-size: 3em; line-height: 1; font-weight: 600; font-variant-numeric: tabular-nums; }
.rr-panel .muted { color: var(--text-muted); font-size: var(--font-ui-small); }
.rr-panel .eyebrow { font-size: var(--font-ui-smaller); text-transform: uppercase; letter-spacing: .05em; color: var(--text-muted); }
.rr-panel h3 { margin: 2px 0; font-size: 1.1em; }
.rr-panel .top { display: flex; gap: 14px; align-items: center; }
.rr-panel .pill { display: inline-block; margin-top: 4px; font-size: var(--font-ui-smaller); padding: 1px 8px; border-radius: 999px; border: 1px solid currentColor; }
.rr-panel .waffle { display: flex; flex-direction: column; gap: 6px; flex: 1; min-width: 260px; }
.rr-panel .wrow { display: flex; gap: 10px; align-items: center; }
.rr-panel .wlabel { width: 11em; flex: none; color: var(--text-muted); font-size: var(--font-ui-small); }
.rr-panel .cells { display: flex; flex-wrap: wrap; gap: 3px; }
.rr-panel .cell { width: 14px; height: 14px; border-radius: 3px; border: 1.5px solid var(--background-modifier-border); box-sizing: border-box; }
.rr-panel .cell.hecho { background: ${VERDE}; border-color: ${VERDE}; }
.rr-panel .cell.parcial { background: linear-gradient(135deg, ${NARANJA} 50%, transparent 50%); border-color: ${NARANJA}; }
.rr-panel .cell.cliente { border-color: ${NARANJA}; }
.rr-panel .cell.runroom { border-color: ${AZUL}; }
.rr-panel .cell.duda { border-style: dashed; }
.rr-panel .cell.descartado { background: var(--background-modifier-border); }
.rr-panel .legend { display: flex; flex-wrap: wrap; gap: 4px 14px; align-items: center; }
.rr-panel .legend span.cell { display: inline-block; vertical-align: middle; margin-right: 4px; }
.rr-panel .cols { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 16px; }
.rr-panel .rows { display: flex; flex-direction: column; gap: 8px; }
.rr-panel .row { display: grid; grid-template-columns: 1fr auto; gap: 2px 8px; font-size: var(--font-ui-small); }
.rr-panel .sub { grid-column: 1 / -1; font-size: var(--font-ui-smaller); }
.rr-panel .track { grid-column: 1 / -1; height: 6px; border-radius: 3px; background: var(--background-modifier-border); overflow: hidden; position: relative; }
.rr-panel .fill { height: 100%; border-radius: 3px; }
.rr-panel .mark { position: absolute; top: -3px; width: 2px; height: 12px; background: var(--text-normal); }
.rr-panel .tag { display: inline-block; font-size: 10px; padding: 0 6px; border-radius: 999px; border: 1px solid var(--background-modifier-border); color: var(--text-muted); vertical-align: middle; }
.rr-panel .tag.est { border-color: ${VERDE}; color: ${VERDE}; }
.rr-panel .tag.bc { border-color: ${AZUL}; color: ${AZUL}; }
.rr-panel a.external-link { font-size: var(--font-ui-smaller); }
.rr-panel .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; }
.rr-panel .kpi { border: 1px solid var(--background-modifier-border); border-radius: 8px; padding: 10px 12px; background: var(--background-primary); }
.rr-panel .kpi .v { font-size: 1.5em; font-weight: 600; font-variant-numeric: tabular-nums; margin-top: 2px; }
.rr-panel table.t { width: 100%; border-collapse: collapse; font-size: var(--font-ui-small); font-variant-numeric: tabular-nums; }
.rr-panel table.t th { text-align: right; font-weight: 500; color: var(--text-muted); font-size: var(--font-ui-smaller); padding: 4px 8px; border-bottom: 1px solid var(--background-modifier-border); }
.rr-panel table.t td { text-align: right; padding: 5px 8px; border-bottom: 1px solid var(--background-modifier-border); }
.rr-panel table.t th:first-child, .rr-panel table.t td:first-child { text-align: left; }
.rr-panel table.t tr.total td { font-weight: 600; border-bottom: none; }
.rr-panel table.t tr.prev td { color: var(--text-muted); }
.rr-panel .note { font-size: var(--font-ui-small); border-left: 3px solid ${NARANJA}; padding-left: 10px; line-height: 1.45; }
.rr-panel .note.ok { border-color: ${VERDE}; }
.rr-panel ul.list { margin: 0; padding-left: 1.2em; font-size: var(--font-ui-small); }
.rr-panel .bars { display: flex; align-items: flex-end; gap: 6px; height: 120px; }
.rr-panel .bar { flex: 1; display: flex; flex-direction: column; align-items: center; gap: 3px; height: 100%; justify-content: flex-end; }
.rr-panel .bar .stack { width: 100%; display: flex; flex-direction: column-reverse; height: 95px; justify-content: flex-start; position: relative; }
.rr-panel .bar .l { font-size: 10px; color: var(--text-muted); }

.rr-panel table.t { display: table; width: 100% !important; margin: 0; table-layout: auto; }
.rr-panel table.t th, .rr-panel table.t td { border: none !important; border-bottom: 1px solid var(--background-modifier-border) !important; background: transparent !important; white-space: nowrap; }
.rr-panel table.t td.neg { color: ${NARANJA}; } .rr-panel table.t td.pos { color: ${VERDE}; }
.rr-panel .scroll { overflow-x: auto; }
.rr-panel .chart { display: flex; align-items: flex-end; gap: 4px; position: relative; }
.rr-panel .chart .col { flex: 1; display: flex; flex-direction: column; align-items: center; min-width: 0; }
.rr-panel .chart .area { width: 100%; display: flex; align-items: flex-end; justify-content: center; gap: 2px; position: relative; }
.rr-panel .chart .b { flex: 1; max-width: 16px; border-radius: 3px 3px 0 0; box-sizing: border-box; }
.rr-panel .chart .stk { width: 70%; max-width: 26px; display: flex; flex-direction: column-reverse; }
.rr-panel .chart .stk > div:last-child { border-radius: 3px 3px 0 0; }
.rr-panel .chart .l { font-size: 10px; color: var(--text-muted); margin-top: 4px; white-space: nowrap; }
.rr-panel .chart .ref { position: absolute; left: 0; right: 0; border-top: 1px dashed var(--text-muted); pointer-events: none; }
.rr-panel .chart .reflbl { position: absolute; right: 0; font-size: 10px; color: var(--text-muted); transform: translateY(-100%); }
.rr-panel .legend .sw { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 5px; vertical-align: middle; }
.rr-panel .legend { font-size: var(--font-ui-smaller); color: var(--text-muted); }
`, root);
function anillo(p, txt, col) {
  const ns = 'http://www.w3.org/2000/svg', r = 40, c = 2 * Math.PI * r;
  const svg = document.createElementNS(ns, 'svg'); svg.setAttribute('viewBox', '0 0 100 100'); svg.setAttribute('width', '88'); svg.setAttribute('height', '88'); svg.style.flex = 'none';
  const circ = (stroke, dash) => { const k = document.createElementNS(ns, 'circle'); k.setAttribute('cx', '50'); k.setAttribute('cy', '50'); k.setAttribute('r', String(r)); k.setAttribute('fill', 'none'); k.setAttribute('stroke-width', '10'); k.style.stroke = stroke; if (dash) { k.setAttribute('stroke-dasharray', dash); k.setAttribute('stroke-linecap', 'round'); k.setAttribute('transform', 'rotate(-90 50 50)'); } svg.appendChild(k); };
  circ('var(--background-modifier-border)'); if (p > 0) circ(col ?? color(p), `${(c * Math.min(p, 100) / 100).toFixed(1)} ${c.toFixed(1)}`);
  const tx = document.createElementNS(ns, 'text'); tx.setAttribute('x', '50'); tx.setAttribute('y', '50'); tx.setAttribute('text-anchor', 'middle'); tx.setAttribute('dominant-baseline', 'central'); tx.setAttribute('font-size', '18'); tx.setAttribute('font-weight', '600'); tx.style.fill = 'var(--text-normal)'; tx.textContent = txt ?? `${p}%`; svg.appendChild(tx);
  return svg;
}
const barra = (parent, label, right, pct, col, markPct) => { const row = el('div', 'row', null, parent); el('span', null, label, row); el('span', 'muted', right, row); const tr = el('div', 'track', null, row); const f = el('div', 'fill', null, tr); f.style.width = `${Math.max(0, Math.min(pct, 100))}%`; f.style.background = col ?? color(pct); if (markPct != null) { const m = el('div', 'mark', null, tr); m.style.left = `${Math.max(0, Math.min(markPct, 100))}%`; } return row; };
const cabecera = (card, svg, eyebrow, titulo, sub, pillTxt, pillCol) => { const top = el('div', 'top', null, card); if (svg) top.appendChild(svg); const info = el('div', null, null, top); el('div', 'eyebrow', eyebrow, info); const h = el('h3', null, titulo, info); if (sub) el('div', 'muted', sub, info); if (pillTxt) { const p = el('span', 'pill', pillTxt, info); p.style.color = pillCol ?? 'var(--text-muted)'; } return h; };
const kpi = (parent, label, valor, sub, col) => { const k = el('div', 'kpi', null, parent); el('div', 'eyebrow', label, k); const v = el('div', 'v', valor, k); if (col) v.style.color = col; if (sub) el('div', 'muted', sub, k); return k; };
const fecha = (x) => { if (x == null || x === '') return null; if (typeof x.toFormat === 'function') return x; const d = dv.luxon.DateTime.fromISO(String(x).trim().slice(0, 10)); return d.isValid ? d : null; };
const laborables = (d0, d1) => { let n = 0; for (let d = d0; d <= d1; d = d.plus({ days: 1 })) if (d.weekday <= 5) n++; return n; };
const MC = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
const hh = (n) => (Math.round(n * 10) / 10).toLocaleString('es-ES', { maximumFractionDigits: 1 });
const leyenda = (parent, items) => { const lg = el('div', 'legend', null, parent); for (const [txt, col, borde] of items) { const sp = el('span', null, null, lg); const sw = el('span', 'sw', null, sp); sw.style.background = borde ? 'transparent' : col; if (borde) sw.style.border = `1.5px dashed ${col}`; sp.appendChild(document.createTextNode(txt)); } return lg; };
const tabla = (parent, cols) => { const w = el('div', 'scroll', null, parent); const t = el('table', 't', null, w); const h = el('tr', null, null, el('thead', null, null, t)); for (const x of cols) el('th', null, x, h); return el('tbody', null, null, t); };
const fila = (tb, vals, cls) => { const tr = el('tr', cls, null, tb); return vals.map((v) => { const td = el('td', null, null, tr); if (Array.isArray(v)) { td.textContent = v[0]; if (v[1]) td.className = v[1]; } else td.textContent = v; return td; }); };
// ───── Saldos ─────
const s = Number(D.google_ads_saldo_estimado ?? 0), gd = Number(D.google_ads_gasto_diario ?? 0);
const umbD = Number(D.umbral_alerta_dias ?? 5);
const dias = gd ? Math.floor(s / gd) : null;
const fd = fecha(D.google_ads_fecha_datos);
const fin = (fd && dias != null) ? fd.plus({ days: dias }) : null;
const avisar = (fd && dias != null) ? fd.plus({ days: Math.max(0, dias - umbD) }) : null;
const alerta = s <= 0 || (dias != null && dias < umbD);
const card = el('div', 'card', null, root);
cabecera(card, null, 'Saldo Google Ads · Clínica + Estética (una sola recarga)', s <= 0 ? 'Sin saldo' : (dias != null ? `Queda saldo para ≈ ${dias} días` : eur(s)), `${eur(s)} disponibles a ${fd ? fd.toFormat('dd/MM/yyyy') : '—'} · gasto medio ${eur(gd)}/día`, alerta ? 'Hay que pedir recarga ya' : (avisar ? `Pedir recarga hacia el ${avisar.toFormat('dd/MM')}` : 'OK'), alerta ? ROJO : VERDE);
const k = el('div', 'kpis', null, card);
kpi(k, 'Saldo disponible', eur(s), fd ? `dato del ${fd.toFormat('dd/MM')}` : null, alerta ? ROJO : null);
kpi(k, 'Gasto medio diario', eur(gd), 'Clínica + Estética');
kpi(k, 'Se agotaría', fin ? fin.toFormat('dd/MM') : '—', dias != null ? `≈ ${dias} días` : null, alerta ? ROJO : null);
kpi(k, 'Pedir recarga', avisar ? avisar.toFormat('dd/MM') : '—', `${umbD} días antes de agotarse (te llega un email)`);
// Proyección día a día
if (dias != null && fd && s > 0) {
  const c = el('div', 'card', null, root);
  el('div', 'eyebrow', 'Proyección del saldo, día a día', c);
  const N = Math.min(dias + 2, 31), H = 100, ch = el('div', 'chart', null, c);
  for (let i = 0; i < N; i++) {
    const d = fd.plus({ days: i }), v = Math.max(0, s - gd * i), col = el('div', 'col', null, ch), area = el('div', 'area', null, col); area.style.height = `${H}px`;
    const b = el('div', 'b', null, area); b.style.height = `${Math.max(2, H * v / s)}px`; b.style.maxWidth = '22px';
    b.style.background = v <= 0 ? 'var(--background-modifier-border)' : (dias - i < umbD ? ROJO : VERDE);
    col.title = `${d.toFormat('dd/MM')}: ≈ ${eur(v)}`;
    el('div', 'l', (i % 2 === 0 || N <= 12) ? d.toFormat('dd') : '·', col);
  }
  leyenda(c, [['Saldo suficiente', VERDE], [`Menos de ${umbD} días: pedir recarga`, ROJO]]);
  el('div', 'muted', `Calculado al ritmo de ${eur(gd)}/día. Si el gasto sube (por ejemplo, al plan de noviembre), se acaba antes.`, c);
}
if (D.google_ads_nota) el('div', alerta ? 'note' : 'note ok', String(D.google_ads_nota), card);
// Historial
const rec = dv.current().file.lists.where((l) => l.fecha != null).array();
if (rec.length) {
  const c2 = el('div', 'card', null, root); el('div', 'eyebrow', 'Recargas y saldos informados', c2);
  const tb = tabla(c2, ['Fecha', 'Recarga', 'Saldo antes', 'Disponible', 'Notas']);
  for (const l of rec.sort((a, b) => (fecha(b.fecha) ?? 0) - (fecha(a.fecha) ?? 0))) { const d = fecha(l.fecha); const tds = fila(tb, [d ? d.toFormat('dd/MM/yy') : String(l.fecha), isNaN(Number(l.importe)) ? '—' : eur(Number(l.importe)), l.saldo_previo ? eur(Number(l.saldo_previo)) : '—', l.saldo_disponible ? eur(Number(l.saldo_disponible)) : '—', String(l.notas ?? '')]); tds[4].style.whiteSpace = 'normal'; tds[4].style.textAlign = 'left'; }
}

```

## Recargas
Cuando Cristian recargue, añade una línea o díselo a Claude. Si solo sabes el saldo disponible, usa `saldo_disponible`.
`- [fecha:: AAAA-MM-DD] [cuenta:: google-ads] [importe:: 15000] [saldo_previo:: 0] [saldo_disponible:: ] [notas:: …]`

- [fecha:: 2026-09-08] [cuenta:: google-ads] [importe:: ?] [saldo_previo:: 4500] [notas:: Cristian "listo!", sin importe]
- [fecha:: 2026-11-05] [cuenta:: google-ads] [importe:: ?] [saldo_previo:: ] [saldo_disponible:: 7736.68] [notas:: saldo disponible informado por Nina; punto de partida del cálculo]
- [fecha:: 2026-10-09] [cuenta:: google-ads] [importe:: ?] [saldo_previo:: 12672] [notas:: saldo informado por Ari: Clínica 12.338 € + Estética 334 €]
