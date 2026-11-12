# Facturación y fee — Esade Contenidos Beyond

Presupuesto del curso 26/27: **48.390,20 €** (máximo = curso 25/26), validado por Helen el 22/10/2026. Fee mensual por partida + one-shots + compra de medios. Se pide en dos pedidos (sep–dic y ene–ago). Lo que no se empieza no se factura.

```dataviewjs
const _f = dv.current().file.folder; const base = _f.slice(0, _f.indexOf('Contenidos Beyond') + 'Contenidos Beyond'.length);
const nota = (n) => dv.pages(`"${base}"`).where((p) => p.file.name === n).first();
const D = nota('Datos panel - Esade Beyond') ?? {};
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
// ───── Facturación, presupuesto y medios ─────
const hoy = dv.date('today');
const pres = Number(D.presupuesto_curso) || 0, precio = Number(D.precio_hora) || 0;
const fs = dv.current().file.tasks.where((t) => t.mes != null).array();
const imp = (t) => Number(t.importe) || 0;
const emit = fs.filter((t) => t.completed), pedido = fs.reduce((a, t) => a + imp(t), 0);
const k = el('div', 'kpis', null, root); k.style.marginBottom = '16px';
kpi(k, 'Presupuesto del curso', eur(pres), D.presupuesto_nota ? String(D.presupuesto_nota) : null);
kpi(k, 'Precio/hora', `${String(precio).replace('.', ',')} €/h`, D.precio_hora_nota ? String(D.precio_hora_nota) : null);
kpi(k, 'Facturas emitidas', `${emit.length} de ${fs.length}`, `Emitido: ${eur(emit.reduce((a, t) => a + imp(t), 0))} de ${eur(pedido)}`, emit.length ? VERDE : NARANJA);
// Facturas / pedidos
const card = el('div', 'card', null, root);
cabecera(card, null, 'Pedidos y facturas del curso', `${emit.length} de ${fs.length} emitidas`, `Total previsto: ${eur(pedido)}${pres && Math.round(pedido) !== Math.round(pres) ? ' · ⚠️ no cuadra con el presupuesto (' + eur(pres) + ')' : ''}`, D.facturacion_cuadra === true ? 'Cuadra' : D.facturacion_cuadra === false ? 'No cuadra' : 'Al día', D.facturacion_cuadra === false ? NARANJA : VERDE);
if (D.facturacion_nota) el('div', 'note', String(D.facturacion_nota), card);
const tb = tabla(card, ['Periodo', 'OC / pedido', 'Importe', 'Estado']);
for (const t of fs) { const d = fecha(t.mes), h2 = fecha(t.hasta); fila(tb, [d ? `${MC[d.month - 1]}${h2 ? '–' + MC[h2.month - 1] : ''} ${String((h2 ?? d).year).slice(2)}` : String(t.mes), t.oc ? String(t.oc) : '—', t.importe != null ? eur(imp(t)) : '—', t.completed ? 'Emitida' : 'Pendiente']); }
el('div', 'muted', 'Nina marca la casilla de la lista de abajo cuando la factura esté emitida.', card);
// Compra de medios
const ms = dv.current().file.lists.where((l) => l.medios != null).array().map((l) => ({ d: fecha(String(l.medios).slice(0, 7) + '-01'), plan: Number(l.plan) || 0, fac: l.facturado != null && l.facturado !== '' ? Number(l.facturado) : null, con: l.consumido != null && l.consumido !== '' ? Number(l.consumido) : null, notas: l.notas ? String(l.notas) : '' })).filter((m) => m.d).sort((a, b) => a.d.toMillis() - b.d.toMillis());
const mp = Number(D.medios_presupuesto) || 0, ly = Number(D.medios_remanente_ly) || 0, nm = Number(D.medios_meses) || 11;
for (const m of ms) m.pas = m.d <= hoy.startOf('month');
const con = ms.reduce((a, m) => a + (m.con ?? 0), 0), fac = ms.filter((m) => m.pas).reduce((a, m) => a + (m.fac ?? 0), 0);
const total = mp + ly, pct = total ? Math.round(100 * con / total) : 0;
const ini = fecha(String(D.curso_inicio ?? '2026-09') + '-01');
const transc = Math.max(0, Math.min(nm, Math.round(hoy.startOf('month').diff(ini, 'months').months)));
const pctT = Math.round(100 * transc / nm);
const cm = el('div', 'card', null, root);
cabecera(cm, anillo(pct, `${pct}%`, Math.abs(pct - pctT) > 10 ? NARANJA : VERDE), 'Compra de medios de link building', `${eur(con)} comprometidos de ${eur(total)}`, `Presupuesto ${eur(mp)} + bolsa del curso anterior ${eur(ly)} · ${transc} de ${nm} meses cerrados (${pctT} %)`, pct > pctT + 10 ? 'Por encima del ritmo' : pct < pctT - 10 ? 'Por debajo del ritmo' : 'Al ritmo previsto', Math.abs(pct - pctT) > 10 ? NARANJA : VERDE);
if (D.medios_nota) el('div', 'note', String(D.medios_nota), cm);
const tm = tabla(cm, ['Mes', 'Presupuesto', 'Facturado', 'Comprometido', 'Disponible acum.']);
let disp = ly; fila(tm, ['Bolsa 25/26', '—', eur(ly), '—', eur(ly)], 'prev');
for (const m of ms) { if (m.pas) disp += (m.fac ?? 0) - (m.con ?? 0); fila(tm, [`${MC[m.d.month - 1]} ${String(m.d.year).slice(2)}`, eur(m.plan), m.fac != null ? eur(m.fac) + (m.pas ? '' : ' (prev.)') : '—', m.con != null ? eur(m.con) : '—', m.pas ? [eur(disp), disp < 0 ? 'neg' : null] : '—'], m.pas ? null : 'prev'); }
fila(tm, ['Total a hoy', eur(ms.reduce((a, m) => a + m.plan, 0)), eur(fac), eur(con), [eur(ly + fac - con), ly + fac - con < 0 ? 'neg' : null]], 'total');
el('div', 'muted', '"Comprometido" = medios aprobados del mes (el Sheet lo llama "consumido"), aunque el medio aún no haya publicado. Disponible = bolsa anterior + facturado − comprometido, hasta el mes en curso. Los meses futuros muestran lo previsto en el Sheet de control (prev.).', cm);
const nts = ms.filter((m) => m.notas); if (nts.length) { const ul = el('ul', 'list', null, cm); for (const m of nts) el('li', null, `${MC[m.d.month - 1]}: ${m.notas}`, ul); }

```

## Calendario del presupuesto (cuándo hacemos qué)
Del [Presupuesto 26/27](https://docs.google.com/spreadsheets/d/1QD3-GrH86NubIWE_TiCnsSGnl-cPop78EnnIZzTYRz4). PV 77,6 €/h sep–dic y 79,93 €/h (estimado) ene–ago.

| Partida | Horas | Total | Sep | Oct | Nov | Dic | Ene | Feb | Mar | Abr | May | Jun | Jul | Ago |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Estrategia de contenidos (KWR 2 art./mes, revisión SEO, mejoras) | 7 h/mes | 6.089,37 € | 543,20 | 543,20 | 543,20 | 543,20 | 559,51 | 559,51 | 559,51 | 559,51 | 559,51 | 559,51 | 559,51 | — |
| Link building (medios, brief, revisión) | 16 h/mes | 13.918,56 € | 1.241,60 | 1.241,60 | 1.241,60 | 1.241,60 | 1.278,88 | 1.278,88 | 1.278,88 | 1.278,88 | 1.278,88 | 1.278,88 | 1.278,88 | — |
| Análisis de toxicidad | 7 h | 543,20 € | | 543,20 | | | | | | | | | | |
| Estudio de enlazado de la competencia | 15 h × 2 | 2.397,90 € | | | | | 1.198,95 | | | | | 1.198,95 | | |
| Compra de medios | — | 25.441,17 € | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | 2.312,83 | — |
| **Total** | | **48.390,20 €** | | | | | | | | | | | | |

Además, **2.079,47 €** de bolsa de medios del curso 25/26.

## Pedidos y facturas 26/27
**Nina marca la casilla** cuando la factura está emitida.
`- [ ] <periodo> [mes:: AAAA-MM de inicio] [hasta:: AAAA-MM de fin] [importe:: €] [oc:: …] [notas:: …]`

- [ ] Pedido sep–dic 2026 (fee, toxicidad y medios) [mes:: 2026-09] [hasta:: 2026-12] [importe:: 16933.73] [oc:: OC012688 (horas) · OC012689 (medios), según la Bolsa de horas; por confirmar] [notas:: Helen, 22/10: "Hago pedidos esta semana"]
- [ ] Pedido ene–ago 2027 [mes:: 2027-01] [hasta:: 2027-08] [importe:: 31456.47] [notas:: con PV estimado de 79,93 €/h; pendiente de compras]

## Compra de medios por mes
Del Sheet [Estrategia Link Building 2026-27](https://docs.google.com/spreadsheets/d/1HIEkVbraRA5NiC_XNK7axsa1Gjqp3D-sr1MAilQioHM), pestaña "Control presupuesto medios" y pestañas mensuales. Claude actualiza la línea del mes.
`- [medios:: AAAA-MM] [plan:: € del presupuesto] [facturado:: € del Sheet de control] [consumido:: € comprometidos] [notas:: …]`

- [medios:: 2026-09] [plan:: 2312.83] [facturado:: 2450] [consumido:: 2509] [notas:: 6 medios publicados; der-bank-blog.de (410 €) pendiente del medio]
- [medios:: 2026-10] [plan:: 2312.83] [facturado:: 3745.47] [consumido:: 3334] [notas:: digitalfernsehen.de 1.334 € (en revisión de Astrid) + ibtimes.co.uk 2.000 € (pendiente del medio)]
- [medios:: 2026-11] [plan:: 2312.83] [facturado:: 2861.47] [notas:: aprobados azonline.de 846 € y diariopalentino.es 1.200 € (2.046 €)]
- [medios:: 2026-12] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-01] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-02] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-03] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-04] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-05] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-06] [plan:: 2312.83] [facturado:: 2450]
- [medios:: 2027-07] [plan:: 2312.83]
