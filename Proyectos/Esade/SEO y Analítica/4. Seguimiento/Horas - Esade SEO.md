# Horas — Esade SEO y Analítica

Horas consumidas frente a vendidas (**50 h/mes**: ~45 de la agencia SEO + ~5 de Nina). Las horas se acumulan o se adelantan según la necesidad del proyecto, idealmente con un **±20 %** de variación mensual como máximo. El curso va de septiembre a agosto.

```dataviewjs
const _f = dv.current().file.folder; const base = _f.slice(0, _f.indexOf('SEO y Analítica') + 'SEO y Analítica'.length);
const nota = (n) => dv.pages(`"${base}"`).where((p) => p.file.name === n).first();
const D = nota('Datos panel - Esade SEO') ?? {};
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
// ───── Horas: bolsa del curso (sep-ago) ─────
const hoy = dv.date('today');
const ini = fecha(String(D.curso_inicio ?? '2026-09') + '-01');
const MES = Array.from({ length: 12 }, (_, i) => ini.plus({ months: i }));
const cursoTxt = `${String(ini.year).slice(2)}/${String(ini.year + 1).slice(2)}`;
const cods = D.paprika_codigos ?? {}; const cod = cods[cursoTxt] ?? Object.values(cods)[0];
const precio = Number(D.precio_hora) || 0;
const varMax = Number(D.variacion_max_pct ?? 20);
const plan = Array.from(D.horas_plan ?? []).map((x) => Array.from(x)).sort((a, b) => String(a[0]).localeCompare(String(b[0])));
const vend = (d) => { const k = d.toFormat('yyyy-MM'); let p = [0, 0]; for (const x of plan) if (String(x[0]) <= k) p = x.slice(1).map(Number); return p; };
const tot = (r) => r ? r.reduce((a, b) => a + b, 0) : 0;
const reg = Array(12).fill(null);
for (const l of dv.current().file.lists.where((l) => l.mes != null).array()) {
  const d = fecha(l.mes); if (!d) continue; const i = Math.round(d.startOf('month').diff(ini, 'months').months); if (i < 0 || i > 11) continue;
  const ag = l.agencia != null && l.agencia !== '' ? Number(l.agencia) : null, km = l.kam != null && l.kam !== '' ? Number(l.kam) : null;
  const total = l.total != null && l.total !== '' ? Number(l.total) : (ag ?? 0) + (km ?? 0);
  reg[i] = { ag, km, total, completo: l.total != null || (ag != null && km != null), act: fecha(l.actualizado), notas: l.notas ? String(l.notas) : '' };
}
// bolsa mes a mes
let rem = Number(D.remanente_inicial) || 0; const rows = [];
for (let i = 0; i < 12; i++) { const v = tot(vend(MES[i])); const disp = rem + v; const c = reg[i] ? reg[i].total : null; if (c != null) rem = disp - c; rows.push({ i, v, disp, c, rem: c != null ? rem : null }); }
const ult = [...rows].reverse().find((r) => r.c != null);
const mi = MES.findIndex((m) => m.year === hoy.year && m.month === hoy.month);
// KPIs
const k = el('div', 'kpis', null, root); k.style.marginBottom = '16px';
if (cod) kpi(k, `Código Paprika ${cursoTxt}`, String(cod), 'para imputar las horas de Nina');
kpi(k, 'Horas vendidas', `${tot(vend(hoy))} h/mes`, `~${vend(hoy)[0]} agencia + ~${vend(hoy)[1]} KAM`);
if (ult) { const pct = 100 * ult.rem / Math.max(1, ult.v); kpi(k, `Remanente a cierre de ${MESES[MES[ult.i].month - 1]}${reg[ult.i].completo ? '' : ' (provisional)'}`, `${hh(ult.rem)} h`, `${eur(ult.rem * precio)} · ${Math.round(pct)} % de un mes${reg[ult.i].completo ? '' : ' · faltan horas por registrar'}`, Math.abs(pct) > varMax ? NARANJA : VERDE); }
// 1. Este mes
const grid = el('div', 'grid', null, root);
const c1 = el('div', 'card', null, grid);
if (mi >= 0) {
  const r = reg[mi], v = vend(hoy); const iniM = hoy.startOf('month'), fin = hoy.endOf('month').startOf('day'); const da = (r && r.act) ?? hoy;
  const frac = laborables(iniM, da) / Math.max(1, laborables(iniM, fin));
  cabecera(c1, null, `Este mes · ${MESES[hoy.month - 1]}`, r ? `${hh(r.total)} de ${tot(v)} h vendidas` : `Sin datos de ${MESES[hoy.month - 1]} todavía`, r ? `Datos a ${da.toFormat('dd/MM')} · previsto a esa fecha: ${hh(tot(v) * frac)} h` : 'Se registran a cierre de mes, cuando la agencia vuelca sus horas', r ? (r.total > tot(v) * frac * 1.1 ? 'Por encima de lo previsto' : 'Dentro de lo previsto') : null, r && r.total > tot(v) * frac * 1.1 ? ROJO : VERDE);
  const rw = el('div', 'rows', null, c1);
  barra(rw, 'Agencia (SEO + analítica)', r && r.ag != null ? `${hh(r.ag)} / ${v[0]} h` : `— / ${v[0]} h`, r && r.ag != null ? 100 * r.ag / v[0] : 0, AZUL, 100 * frac);
  barra(rw, 'KAM · Nina', r && r.km != null ? `${hh(r.km)} / ${v[1]} h` : `— / ${v[1]} h`, r && r.km != null ? 100 * r.km / v[1] : 0, NARANJA, 100 * frac);
}
// 2. Bolsa del curso
const c2 = el('div', 'card', null, grid);
const cerr = rows.filter((r) => r.c != null), VT = cerr.reduce((a, r) => a + r.v, 0), HT = cerr.reduce((a, r) => a + r.c, 0);
cabecera(c2, null, `Curso ${cursoTxt} · meses registrados`, `${hh(HT)} de ${VT} h vendidas`, `Remanente del curso anterior: ${hh(Number(D.remanente_inicial) || 0)} h`, ult ? `Bolsa: ${hh(ult.rem)} h (${ult.rem >= 0 ? 'a favor del cliente' : 'adelantadas'})` : 'Sin meses registrados', ult && Math.abs(100 * ult.rem / Math.max(1, ult.v)) > varMax ? NARANJA : VERDE);
const rw2 = el('div', 'rows', null, c2);
for (const r of cerr) { const d = r.v ? 100 * (r.c - r.v) / r.v : 0; barra(rw2, MESES[MES[r.i].month - 1], `${hh(r.c)} h · ${d >= 0 ? '+' : '−'}${Math.abs(Math.round(d))} %`, r.v ? 100 * r.c / (r.v * 1.5) : 0, Math.abs(d) > varMax ? NARANJA : VERDE, 100 / 1.5); }
el('div', 'muted', `La línea marca las ${tot(vend(hoy))} h del mes. Naranja: variación de más de un ±${varMax} % (lo pactado como máximo ideal).`, c2);
// 3. Gráfico
const c3 = el('div', 'card', null, root);
el('div', 'eyebrow', `Horas consumidas por mes · curso ${cursoTxt}`, c3);
const mx = Math.max(1, ...rows.map((r) => (r.c ?? 0)), ...rows.map((r) => r.v * (1 + varMax / 100))), H = 120;
const ch = el('div', 'chart', null, c3);
for (const r of rows) {
  const col = el('div', 'col', null, ch), area = el('div', 'area', null, col); area.style.height = `${H}px`;
  const st = el('div', 'stk', null, area); const g = reg[r.i];
  if (g) { if (g.ag != null || g.km != null) { if (g.ag) { const s = el('div', null, null, st); s.style.cssText = `height:${H * g.ag / mx}px;background:${AZUL}`; } if (g.km) { const s = el('div', null, null, st); s.style.cssText = `height:${H * g.km / mx}px;background:${NARANJA}`; } } else { const s = el('div', null, null, st); s.style.cssText = `height:${H * g.total / mx}px;background:hsl(210, 12%, 58%)`; } }
  const ref = el('div', 'ref', null, area); ref.style.bottom = `${H * r.v / mx}px`;
  col.title = `${MESES[MES[r.i].month - 1]}: ${g ? hh(g.total) + ' h' : 'sin datos'} (vendidas ${r.v} h)`;
  el('div', 'l', MC[MES[r.i].month - 1], col);
}
leyenda(c3, [['Agencia', AZUL], ['KAM · Nina', NARANJA], ['Total sin desglose', 'hsl(210, 12%, 58%)'], ['Horas vendidas', 'var(--text-muted)', true]]);
const tb = tabla(c3, ['Mes', 'Agencia', 'KAM', 'Total', 'Vendidas', 'Disponibles', 'Remanente', 'Var.']);
for (const r of rows) { const g = reg[r.i]; if (!g) continue; const d = r.v ? Math.round(100 * (r.c - r.v) / r.v) : 0; fila(tb, [MC[MES[r.i].month - 1] + (g.completo ? '' : ' *'), g.ag != null ? hh(g.ag) : '—', g.km != null ? hh(g.km) : '—', hh(g.total), String(r.v), hh(r.disp), [hh(r.rem), r.rem < 0 ? 'neg' : null], [`${d > 0 ? '+' : ''}${d} %`, Math.abs(d) > varMax ? 'neg' : null]], g.completo ? null : 'prev'); }
el('div', 'muted', '* Mes incompleto (falta una de las dos partes: agencia o Paprika de Nina). Remanente = horas disponibles (remanente anterior + vendidas) − consumidas.', c3);
const notas = rows.filter((r) => reg[r.i] && reg[r.i].notas); if (notas.length) { const ul = el('ul', 'list', null, c3); for (const r of notas) el('li', null, `${MC[MES[r.i].month - 1]}: ${reg[r.i].notas}`, ul); }

```

## Registro mensual
Una línea por mes. A cierre de mes, la agencia vuelca sus horas en la [Bolsa de horas](https://docs.google.com/spreadsheets/d/1F2KfWNbXZaOp2sEN8ZtMgchEtRdHLS3hkFEeoXoKWTk) (pestaña ESADE, filas "Fee SEO&Analítica") y Nina las pasa, junto con las suyas de Paprika, al [Seguimiento del fee](https://docs.google.com/spreadsheets/d/1o_2qc46-s4txCu9g0rA1S_Q1jHP5T-0G9DjAy21_vG0) (pestaña Curso 26/27). Claude actualiza aquí la línea del mes.
`- [mes:: AAAA-MM] [agencia:: h] [kam:: h] [total:: h (solo si no hay desglose)] [actualizado:: AAAA-MM-DD] [notas:: …]`

- [mes:: 2026-09] [total:: 29] [actualizado:: 2026-11-12] [notas:: cifra del Seguimiento del fee, sin desglose por perfil. La Bolsa de horas de la agencia imputa 42,5 h a septiembre (Fer 36 + Marta 6,5), pero las 36 h de Fer incluyen la Estrategia 26/27, que el Seguimiento ya cargó en agosto (curso 25/26). Por confirmar con Nina]
- [mes:: 2026-10] [agencia:: 37.5] [actualizado:: 2026-11-12] [notas:: Bolsa de horas: Fer 29 + Marta 7 + Olga 1,5. Faltan las horas de Nina (Paprika) y volcarlo al Seguimiento]

Remanente del curso 25/26 que pasa al 26/27: 16,92 h (Seguimiento del fee, cierre de agosto).
