# Horas — Hispano Suiza

Horas hechas frente a vendidas. Hasta agosto: Head 0,47 h, KAM 2,66 h y Performance Media 5,86 h (8,99 h/mes). Desde septiembre: **Head (Ari) 13 h** y **KAM (Nina) 1,5 h** (14,5 h/mes). Código de Paprika: **HIS010010** (2026) · HIS010011 (2027).

```dataviewjs
const _f = dv.current().file.folder; const base = _f.slice(0, _f.indexOf('Hispano Suiza') + 'Hispano Suiza'.length);
const nota = (n) => dv.pages(`"${base}"`).where((p) => p.file.name === n).first();
const D = nota('Datos panel - Hispano Suiza') ?? {};
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
// ───── Horas ─────
const hoy = dv.date('today');
const cods = D.paprika_codigos ?? {}; const cod = cods[hoy.year] ?? cods[String(hoy.year)];
if (cod) { const b = el('div', 'kpis', null, root); b.style.marginBottom = '16px'; kpi(b, `Código Paprika ${hoy.year}`, String(cod), 'para imputar las horas de Hispano Suiza'); const nx = cods[hoy.year + 1] ?? cods[String(hoy.year + 1)]; if (nx) kpi(b, `Código Paprika ${hoy.year + 1}`, String(nx), 'a partir del 1 de enero'); }
const plan = Array.from(D.horas_plan ?? []).map((x) => Array.from(x)).sort((a, b) => String(a[0]).localeCompare(String(b[0])));
const vend = (i) => { const k = `${hoy.year}-${String(i + 1).padStart(2, '0')}`; let p = [0, 0, 0]; for (const x of plan) { const d0 = fecha(x[0]); const k0 = d0 ? d0.toFormat('yyyy-MM') : String(x[0]).slice(0, 7); if (k0 <= k) p = x.slice(1).map(Number); } return p; };
const P = [['Head · Ari', AZUL, 'head'], ['KAM · Nina', NARANJA, 'kam'], ['Performance Media', VERDE, 'performance'], ['Otros (UX, becario…)', 'hsl(210, 12%, 58%)', 'otros']];
const reg = Array(12).fill(null), act = Array(12).fill(null);
for (const l of dv.current().file.lists.where((l) => l.mes != null).array()) { const d = fecha(l.mes); if (!d || d.year !== hoy.year) continue; reg[d.month - 1] = P.map(([, , k]) => Number(l[k]) || 0); act[d.month - 1] = fecha(l.actualizado); }
const mi = hoy.month - 1, tot = (r) => r ? r.reduce((a, b) => a + b, 0) : 0;
// 1. Este mes
const ini = hoy.startOf('month'), finM = hoy.endOf('month').startOf('day'), da = act[mi] ?? hoy;
const frac = laborables(ini, da) / Math.max(1, laborables(ini, finM));
const grid = el('div', 'grid', null, root);
const c1 = el('div', 'card', null, grid);
const v = vend(mi), r = reg[mi] ?? [0, 0, 0, 0];
let pasado = false;
const rows1 = el('div', 'rows', null, c1);
for (let j = 0; j < 3; j++) { if (!v[j] && !r[j]) continue; const prev = v[j] * frac, mal = r[j] > prev * 1.1 && r[j] > 1; pasado = pasado || mal; barra(rows1, P[j][0], `${hh(r[j])} / ${hh(v[j])} h`, v[j] ? 100 * r[j] / v[j] : 100, mal ? ROJO : P[j][1], 100 * frac); }
const top1 = el('div', null, null, c1); c1.insertBefore(top1, rows1);
cabecera(top1, null, `Este mes · ${MESES[mi]}`, `${hh(tot(r))} de ${hh(tot(v))} h vendidas`, `Datos a ${da.toFormat('dd/MM')} · previsto a esa fecha: ${hh(tot(v) * frac)} h`, pasado ? 'Alguien va por encima de lo previsto' : 'Dentro de lo previsto', pasado ? ROJO : VERDE);
el('div', 'muted', 'La línea vertical marca lo que tocaría llevar a la fecha de los datos.', c1);
// 2. Acumulado año (meses cerrados)
const c2 = el('div', 'card', null, grid);
const cerr = Array.from({ length: mi }, (_, i) => i).filter((i) => reg[i]);
const vA = [0, 1, 2, 3].map((j) => cerr.reduce((a, i) => a + (vend(i)[j] ?? 0), 0)), hA = [0, 1, 2, 3].map((j) => cerr.reduce((a, i) => a + reg[i][j], 0));
const VT = tot(vA), HT = tot(hA);
cabecera(c2, null, `Acumulado ${hoy.year} · ene-${MC[Math.max(0, mi - 1)]}`, `${hh(HT)} de ${hh(VT)} h vendidas (${VT ? Math.round(100 * HT / VT) : 0} %)`, `${HT <= VT ? 'Faltan' : 'Sobran'} ${hh(Math.abs(VT - HT))} h`, HT > VT ? 'Por encima de lo vendido' : 'Por debajo de lo vendido', HT > VT ? ROJO : VERDE);
const rows2 = el('div', 'rows', null, c2);
for (let j = 0; j < 4; j++) if (vA[j] || hA[j]) barra(rows2, P[j][0], `${hh(hA[j])} / ${hh(vA[j])} h`, vA[j] ? 100 * hA[j] / vA[j] : 100, hA[j] > vA[j] * 1.05 && vA[j] ? ROJO : P[j][1]);
el('div', 'muted', 'Otros no tiene horas vendidas: cuenta como horas de más.', c2);
// 3. Gráfico mes a mes
const c3 = el('div', 'card', null, root);
el('div', 'eyebrow', 'Horas hechas por mes, por perfil', c3);
const mx = Math.max(1, ...reg.map(tot), ...Array.from({ length: 12 }, (_, i) => tot(vend(i)))), H = 120;
const ch = el('div', 'chart', null, c3);
for (let i = 0; i < 12; i++) {
  const col = el('div', 'col', null, ch), area = el('div', 'area', null, col); area.style.height = `${H}px`;
  const st = el('div', 'stk', null, area);
  if (reg[i]) reg[i].forEach((h, j) => { if (h) { const s = el('div', null, null, st); s.style.cssText = `height:${H * h / mx}px;background:${P[j][1]}`; } });
  const ref = el('div', 'ref', null, area); ref.style.bottom = `${H * tot(vend(i)) / mx}px`;
  col.title = `${MESES[i]}: ${reg[i] ? reg[i].map((h, j) => `${P[j][0]} ${hh(h)}`).join(' · ') + ` · total ${hh(tot(reg[i]))} h` : 'sin datos'} (vendidas ${hh(tot(vend(i)))} h)`;
  el('div', 'l', MC[i], col);
}
leyenda(c3, P.map(([t, c]) => [t, c]).concat([['Horas vendidas', 'var(--text-muted)', true]]));
// 4. Tabla
const tb = tabla(c3, ['Mes', 'Head', 'KAM', 'Perf.', 'Otros', 'Total', 'Vendidas', 'Dif.']);
for (let i = 0; i < 12; i++) { if (!reg[i]) continue; const d = tot(reg[i]) - tot(vend(i)); fila(tb, [MC[i] + (i === mi ? ' (en curso)' : ''), ...reg[i].map((h) => h ? hh(h) : '—'), hh(tot(reg[i])), hh(tot(vend(i))), i === mi ? '—' : [`${d > 0 ? '+' : ''}${hh(d)}`, d > 0 ? 'neg' : null]], i === mi ? 'prev' : null); }
el('div', 'muted', plan.length ? 'Horas vendidas según horas_plan (Claude/Datos panel).' : 'Aún no hay horas vendidas cargadas (horas_plan en Claude/Datos panel).', c3);

```

## Registro mensual
Una línea por mes, con las horas por perfil de la herramienta de horas. Pásale una captura a Claude (idealmente cada viernes) y actualiza el mes en curso. `otros` = UX/UI, becario y otros perfiles sin horas vendidas.
`- [mes:: AAAA-MM] [head:: h] [kam:: h] [performance:: h] [otros:: h] [actualizado:: AAAA-MM-DD] [notas:: …]`

Todavía no hay horas registradas de 2026: pásale a Claude las capturas de la herramienta de horas (de enero al mes en curso) y las vuelca aquí. En la herramienta de horas, "KAMPO" = KAM.
