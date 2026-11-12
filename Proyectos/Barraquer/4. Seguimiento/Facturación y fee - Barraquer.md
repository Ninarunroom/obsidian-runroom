# Facturación y fee — Barraquer

Fee facturado frente a invertido, inversión en medios frente a lo aprobado y escalado de fee. La facturación es automática (cada mes la misma cuota).

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
// ───── Facturación y fee ─────
const n = Number(D.meses_reales ?? 12);
const medios = arr('medios_mes'), fee = arr('fee_consumido_mes'), tasa = arr('tasa_mes');
const facts = dv.current().file.tasks.where((t) => t.mes != null).array();
const facturadoMes = Array(12).fill(0), marcado = Array(12).fill(null);
for (const t of facts) { const d = fecha(t.mes); if (!d) continue; const i = d.month - 1; marcado[i] = t.completed; if (t.completed) facturadoMes[i] += Number(t.importe) || 0; }
const sum = (a, k = 12) => a.slice(0, k).reduce((x, y) => x + (Number(y) || 0), 0);
const facturado = sum(facturadoMes);
const mesesFact = marcado.filter((x) => x === true).length;
const feeApr = Number(D.fee_aprobado), medApr = Number(D.medios_aprobado), tasaApr = Number(D.tasa_aprobado);
const feeInv = sum(fee, n), medInv = sum(medios, n);
const feeInvHastaFact = sum(fee, mesesFact);
const dif = facturado - feeInvHastaFact;
// 1. Resumen fee
const c1 = el('div', 'card', null, root);
cabecera(c1, null, `Fee Runroom 2026 · facturado hasta ${MESES[mesesFact - 1] ?? '—'}`, Math.abs(dif) <= 100 ? 'Facturado en línea con lo invertido' : (dif > 0 ? `Facturado ${eur(dif)} por encima de lo invertido` : `Facturado ${eur(-dif)} por debajo de lo invertido`), 'Invertido = fee del 18 % sobre la inversión real de los meses ya facturados', null);
const k1 = el('div', 'kpis', null, c1);
kpi(k1, 'Aprobado', eur(feeApr), 'fee anual');
kpi(k1, 'Facturado', eur(facturado), `${mesesFact} de 12 facturas`);
kpi(k1, 'Invertido', eur(feeInvHastaFact), `fee consumido ene-${(MESES[mesesFact - 1] ?? '').slice(0, 3)}`);
kpi(k1, 'Diferencia', sgn(dif), 'facturado − invertido', Math.abs(dif) <= 100 ? VERDE : NARANJA);
kpi(k1, 'Pendiente de facturar', eur(feeApr - facturado), `${12 - mesesFact} cuotas`);
// 2. Resumen inversión anual
const c2 = el('div', 'card', null, root);
const medPend = sum(medios) - medInv;
const difMed = medInv + medPend - medApr;
cabecera(c2, null, 'Inversión en medios 2026', Math.abs(difMed) <= 100 ? 'Cuadra con lo aprobado' : `Previsión ${sgn(difMed)} frente a lo aprobado`, `Real hasta ${MESES[n - 1] ?? '—'} + previsión del resto (Detalle_Mensual)`, null);
const k2 = el('div', 'kpis', null, c2);
kpi(k2, 'Aprobado', eur(medApr)); kpi(k2, 'Invertido', eur(medInv), `ene-${(MESES[n - 1] ?? '').slice(0, 3)}`); kpi(k2, 'Pendiente de invertir', eur(medPend), `${12 - n} meses`); kpi(k2, 'Diferencia', sgn(difMed), 'invertido + pendiente − aprobado', Math.abs(difMed) <= 100 ? VERDE : NARANJA);
// 3. Mes a mes
const c3 = el('div', 'card', null, root);
el('div', 'eyebrow', 'Mes a mes · fee facturado frente a fee invertido', c3);
const cuota = (i) => { const t = facts.find((x) => { const d = fecha(x.mes); return d && d.month - 1 === i; }); return t ? Number(t.importe) || 0 : 0; };
const mxB = Math.max(1, ...fee, ...Array.from({ length: 12 }, (_, i) => cuota(i)));
const GRIS = 'hsl(210, 12%, 58%)', H = 110;
const ch = el('div', 'chart', null, c3);
for (let i = 0; i < 12; i++) {
  const real = i < n, col = el('div', 'col', null, ch), area = el('div', 'area', null, col); area.style.height = `${H}px`;
  const b1 = el('div', 'b', null, area); b1.style.height = `${H * cuota(i) / mxB}px`;
  if (marcado[i] === true) b1.style.background = AZUL; else b1.style.border = `1.5px dashed ${AZUL}`;
  const b2 = el('div', 'b', null, area); b2.style.height = `${H * (fee[i] || 0) / mxB}px`;
  if (real) b2.style.background = GRIS; else b2.style.border = `1.5px dashed ${GRIS}`;
  col.title = `${MESES[i]}: facturado ${marcado[i] === true ? eur(facturadoMes[i]) : 'pendiente (' + eur(cuota(i)) + ')'} · fee invertido ${eur(fee[i])}${real ? '' : ' (previsto)'} · medios ${eur(medios[i])}`;
  el('div', 'l', MC[i], col);
}
leyenda(c3, [['Facturado', AZUL], ['Por facturar', AZUL, true], ['Fee invertido', GRIS], ['Fee previsto', GRIS, true]]);
const tb = tabla(c3, ['Mes', 'Facturado', 'Fee invertido', 'Diferencia', 'Acumulada']);
let acc = 0;
for (let i = 0; i < 12; i++) {
  const real = i < n, f = marcado[i] === true;
  const d = (f ? facturadoMes[i] : 0) - (real ? fee[i] : 0); if (f || real) acc += d;
  const show = f || real, cl = (x) => Math.abs(x) <= 100 ? 'pos' : 'neg';
  fila(tb, [MC[i] + (real ? '' : ' (prev.)'), f ? eur(facturadoMes[i]) : 'pendiente', eur(fee[i]), show ? [sgn(d), cl(d)] : '—', show ? [sgn(acc), cl(acc)] : '—'], real ? null : 'prev');
}
fila(tb, ['Total', eur(facturado), eur(sum(fee)), '', ''], 'total');
el('div', 'muted', 'Diferencia = facturado − fee invertido (18 % de la inversión real). Pasa el ratón por una barra para ver la inversión en medios del mes.', c3);
if (D.facturacion_nota) el('div', D.facturacion_cuadra ? 'note ok' : 'note', String(D.facturacion_nota), c3);
// 4. Escalado de fee
const c4 = el('div', 'card', null, root);
const inv = Number(D.inversion_anual_prevista ?? 0);
const tramos = Array.from(D.fee_tramos ?? []).map((x) => Array.from(x).map(Number));
const tr0 = tramos.find(([a, b]) => inv >= a && inv < b) ?? [0, 1, 0];
const pos = Math.round(100 * (inv - tr0[0]) / (tr0[1] - tr0[0]));
const cerca = Math.min(inv - tr0[0], tr0[1] - inv) < inv * 0.05;
const sig = tramos.find(([a]) => a === tr0[1]);
cabecera(c4, anillo(pos, `${tr0[2]}%`, cerca ? NARANJA : VERDE), 'Escalado de fee', `Tramo ${Math.round(tr0[0] / 1000)}k – ${Math.round(tr0[1] / 1000)}k → ${tr0[2]} %`, `Inversión anual prevista ${eur(inv)} (clínica + estética + Instituto)`, cerca ? `A ${eur(tr0[1] - inv)} del siguiente tramo${sig ? ' (' + sig[2] + ' %)' : ''}` : 'Lejos de los umbrales', cerca ? NARANJA : VERDE);
const rows = el('div', 'rows', null, c4);
for (const [a, b, p] of tramos.filter(([a]) => a < 600000)) barra(rows, `${Math.round(a / 1000)}k – ${b > 9e7 ? '+' : Math.round(b / 1000) + 'k'} · ${p} %`, a === tr0[0] ? 'actual' : '', a === tr0[0] ? pos : (inv >= b ? 100 : 0), a === tr0[0] ? (cerca ? NARANJA : VERDE) : 'var(--text-faint)');

```

## Facturas 2026
Marca la casilla cuando emitas la factura del mes (o díselo a Claude). Si un mes cambia el importe, cámbialo en la línea.

- [x] Factura de enero [mes:: 2026-01] [importe:: 2628]
- [x] Factura de febrero [mes:: 2026-02] [importe:: 3972]
- [x] Factura de marzo [mes:: 2026-03] [importe:: 3972]
- [x] Factura de abril [mes:: 2026-04] [importe:: 3972]
- [x] Factura de mayo [mes:: 2026-05] [importe:: 4594]
- [x] Factura de junio [mes:: 2026-06] [importe:: 4594]
- [x] Factura de julio [mes:: 2026-07] [importe:: 4594]
- [x] Factura de agosto [mes:: 2026-08] [importe:: 4594]
- [x] Factura de septiembre [mes:: 2026-09] [importe:: 4594]
- [x] Factura de octubre [mes:: 2026-10] [importe:: 4594]
- [ ] Factura de noviembre [mes:: 2026-11] [importe:: 4594]
- [ ] Factura de diciembre [mes:: 2026-12] [importe:: 4594]
