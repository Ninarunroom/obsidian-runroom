---
cssclasses:
  - rr-ancho
---
# Tareas — Spradling

Todo lo pendiente en un solo sitio: la estrategia 2026 y las tareas de Basecamp y de las reuniones, separadas entre lo nuestro y lo del cliente.

```dataviewjs
const _f = dv.current().file.folder; const base = _f.slice(0, _f.indexOf('Spradling') + 'Spradling'.length);
const nota = (n) => dv.pages(`"${base}"`).where((p) => p.file.name === n).first();
const D = nota('Datos panel - Spradling') ?? {};
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

// ───── Tareas: estrategia 2026 + Basecamp + actas ─────
const est = nota('Estrategia 2026 - Spradling');
const pen = nota('Pendientes - Spradling');
const tipo = (t) => t.status === 'x' || t.status === 'X' ? 'hecho' : t.status === '/' ? 'parcial' : t.status === '-' ? 'descartado' : t.status === '?' ? 'duda' : (String(t.pelota ?? '').toLowerCase() === 'runroom' ? 'runroom' : 'cliente');
const estTasks = est ? est.file.tasks.where((t) => !t.parent).array() : [];
const vivas = estTasks.filter((t) => tipo(t) !== 'descartado');
const peso = (t) => tipo(t) === 'hecho' ? 1 : tipo(t) === 'parcial' ? 0.5 : 0;
const estPct = vivas.length ? Math.round(100 * vivas.reduce((a, t) => a + peso(t), 0) / vivas.length) : 0;
const cuenta = (k) => estTasks.filter((t) => tipo(t) === k).length;
const ts = pen ? pen.file.tasks.where((t) => !t.parent && !t.completed && t.status !== '-').array() : [];
const hoy = dv.date('today');
const txtAll = (t) => (t.children ?? []).map((c) => c.text).join(' ') + ' ' + t.text;
const fechaDe = (t) => { const m = txtAll(t).match(/(?:Esperando desde|detectado)[:*\s]*?(\d{2})\/(\d{2})\/(\d{4})/i); return m ? dv.date(`${m[3]}-${m[2]}-${m[1]}`) : null; };
const linkDe = (t) => { const a = txtAll(t); const m = a.match(/\((https:\/\/basecamp\.com[^)\s]+)\)/) ?? a.match(/\((https?:\/\/[^)\s]+)\)/); return m ? m[1] : null; };
const limpia = (s) => String(s).replace(/\*\*\[[^\]]*\]\*\*\s*Spradling\s*—\s*/, '').replace(/\[(pelota|motivo|nuevo|basecamp|responsable)::[^\]]*\]/g, '').replace(/\[fuente::.*$/, '').replace(/\s*—\s*\[.*$/, '').trim();

// Status del día (sección "## Status" de Pendientes)
if (pen) {
  const txt = await dv.io.load(pen.file.path);
  const m = txt.match(/## Status[^\n]*\n([\s\S]*?)\n## /);
  if (m) { const card = el('div', 'card', null, root); el('div', 'eyebrow', 'Status de hoy', card); const ul = el('ul', 'list', null, card); for (const l of m[1].split('\n').filter((l) => l.trim().startsWith('- '))) { const li = el('li', null, null, ul); li.innerHTML = l.trim().slice(2).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>'); } }
}

// Tablero de tareas (vista común: 1. Cómo funciona/Vistas/tablero)
{ const f = dv.current().file.folder; const raiz = f.slice(0, f.indexOf('Proyectos/'));
  await dv.view(raiz + 'Proyectos/1. Cómo funciona/Vistas/tablero', { pendientes: 'Pendientes - Spradling', cliente: 'Spradling' }); }

// Avance de la estrategia
const g = el('div', 'card global', null, root);
const izq = el('div', null, null, g);
el('div', 'eyebrow', 'Estrategia 2026 · avance', izq);
const big = el('div', 'big', `${estPct}%`, izq); big.style.color = color(estPct);
el('div', 'muted', `${cuenta('hecho')} hechas · ${cuenta('parcial')} a medias · ${cuenta('cliente')} esperando al cliente · ${cuenta('runroom')} nuestras · ${cuenta('duda')} sin constancia · ${cuenta('descartado')} descartadas`, izq);
const waf = el('div', 'waffle', null, g);
for (const s of [...new Set(estTasks.map((t) => t.section?.subpath ?? ''))]) {
  const row = el('div', 'wrow', null, waf); el('div', 'wlabel', s, row); const cells = el('div', 'cells', null, row);
  for (const t of estTasks.filter((t) => (t.section?.subpath ?? '') === s)) { const c = el('span', `cell ${tipo(t)}`, null, cells); c.title = `${tipo(t)}\n${limpia(t.text)}${t.motivo ? '\n→ ' + t.motivo : ''}`; }
}
const leg = el('div', 'legend muted', null, waf);
for (const [k, txt] of [['hecho', 'hecho'], ['parcial', 'a medias'], ['cliente', 'cliente'], ['runroom', 'Runroom'], ['duda', 'no consta'], ['descartado', 'descartado']]) { const s = el('span', null, null, leg); el('span', `cell ${k}`, null, s); s.append(txt); }

// Referencias: de dónde sale cada acción
const ref = el('div', 'card', null, root);
el('div', 'eyebrow', 'De dónde sale cada cosa', ref);
const refTxt = el('div', 'muted', null, ref);
const link = (nombre, texto) => { const a = el('a', 'internal-link', texto, refTxt); a.setAttribute('data-href', nombre); a.setAttribute('href', nombre); return a; };
refTxt.append('Cada acción de la estrategia lleva su fuente (propuesta, acta o hilo) en ');
link('Estrategia 2026 - Spradling', 'Estrategia 2026');
refTxt.append('. Las propuestas y decisiones, con su porqué y su fuente, en ');
link('Propuestas y decisiones - Spradling', 'Propuestas y decisiones');
refTxt.append('. No hace falta marcar nada aquí: dile a Claude qué está hecho o sobra.');

```
