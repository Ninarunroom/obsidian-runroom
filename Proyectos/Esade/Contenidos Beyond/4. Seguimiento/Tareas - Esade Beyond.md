# Tareas — Esade Contenidos Beyond

Todo lo pendiente en un solo sitio: la estrategia de Beyond 26/27 (contenidos y link building) y las tareas de Basecamp, correo y reuniones, separadas entre lo nuestro (Olga, Fer y Nina) y lo del cliente.

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

// ───── Tareas: estrategia 26/27 + Basecamp + correo + actas ─────
const est = nota('Estrategia 26-27 - seguimiento Esade Beyond');
const pen = nota('Pendientes - Esade Beyond');
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
const linksDe = (t) => { const c = (t.children ?? []).find((c) => /^Fuente:/.test(String(c.text).trim())); const src = c ? String(c.text) : String(t.text); return [...src.matchAll(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g)].map((m) => ({ label: m[1], url: m[2] })); };
const icono = (u) => u.includes('mail.google') ? '📧' : u.includes('basecamp.com') ? '🏕️' : u.includes('docs.google.com/spreadsheets') ? '📊' : u.includes('drive.google') || u.includes('docs.google') ? '📄' : '🔗';
const etiqueta = (l) => { const x = l.label.replace(/^📧\s*/, '').replace(/^Basecamp:\s*/, ''); return `${icono(l.url)} ${x.length > 60 ? x.slice(0, 58) + '…' : x}`; };
const limpia = (s) => String(s).replace(/\*\*\[[^\]]*\]\*\*\s*Esade\s*—\s*/, '').replace(/\[(pelota|motivo|nuevo|basecamp|fuente|plan|inicio|fin|kanbanize)::[^\]]*\]/g, '').replace(/\s*—\s*\[.*$/, '').trim();

// Status del día (sección "## Status" de Pendientes)
if (pen) {
  const txt = await dv.io.load(pen.file.path);
  const m = txt.match(/## Status[^\n]*\n([\s\S]*?)\n## /);
  if (m) { const card = el('div', 'card', null, root); el('div', 'eyebrow', 'Status de hoy', card); const ul = el('ul', 'list', null, card); for (const l of m[1].split('\n').filter((l) => l.trim().startsWith('- '))) { const li = el('li', null, null, ul); li.innerHTML = l.trim().slice(2).replace(/\*\*(.+?)\*\*/g, '<b>$1</b>'); } }
}

// Avance de la estrategia
const g = el('div', 'card global', null, root);
const izq = el('div', null, null, g);
el('div', 'eyebrow', 'Estrategia Beyond 26/27 · avance', izq);
const big = el('div', 'big', `${estPct}%`, izq); big.style.color = color(estPct);
el('div', 'muted', `${cuenta('hecho')} hechas · ${cuenta('parcial')} a medias · ${cuenta('cliente')} esperando al cliente · ${cuenta('runroom')} nuestras · ${cuenta('duda')} sin confirmar · ${cuenta('descartado')} descartadas`, izq);
const waf = el('div', 'waffle', null, g);
for (const s of [...new Set(estTasks.map((t) => t.section?.subpath ?? ''))]) {
  const row = el('div', 'wrow', null, waf); el('div', 'wlabel', s, row); const cells = el('div', 'cells', null, row);
  for (const t of estTasks.filter((t) => (t.section?.subpath ?? '') === s)) { const c = el('span', `cell ${tipo(t)}`, null, cells); c.title = `${tipo(t)}\n${limpia(t.text)}${t.motivo ? '\n→ ' + t.motivo : ''}`; }
}
const leg = el('div', 'legend muted', null, waf);
for (const [k, txt] of [['hecho', 'hecho'], ['parcial', 'a medias'], ['cliente', 'cliente'], ['runroom', 'Runroom'], ['duda', 'sin confirmar'], ['descartado', 'descartado']]) { const s = el('span', null, null, leg); el('span', `cell ${k}`, null, s); s.append(txt); }

// Tablero (tipo Kanban): esperando al cliente · en curso · backlog · hecho
const kst = el('style', null, `.rr-panel .kb { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; align-items: start; }
.rr-panel .kcol { background: var(--background-primary); border: 1px solid var(--background-modifier-border); border-radius: 10px; padding: 10px; display: flex; flex-direction: column; gap: 8px; min-width: 0; }
.rr-panel .khead { display: flex; justify-content: space-between; align-items: baseline; font-weight: 600; padding-bottom: 6px; border-bottom: 3px solid var(--kc); }
.rr-panel .kcard { border: 1px solid var(--background-modifier-border); border-left: 4px solid var(--kc); border-radius: 8px; padding: 8px 10px; background: var(--background-secondary); display: flex; flex-direction: column; gap: 4px; font-size: var(--font-ui-small); overflow-wrap: anywhere; min-width: 0; }
.rr-panel .kcard .kmeta { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; color: var(--text-muted); font-size: var(--font-ui-smaller); }
.rr-panel .kcard.old { border-left-color: hsl(4, 70%, 52%); }
.rr-panel details.kdet > summary { cursor: pointer; color: var(--text-muted); font-size: var(--font-ui-smaller); padding: 4px 0; }
.rr-panel details.kdet[open] > summary { margin-bottom: 8px; }
.rr-panel details.kdet .kcard { margin-bottom: 8px; }
.rr-panel .klinks { display: flex; flex-direction: column; gap: 2px; font-size: var(--font-ui-smaller); }
.rr-panel .klinks a { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.rr-panel .khecho { margin-top: 12px; }
.rr-panel .klane { border-left: 4px solid var(--lc); padding-left: 10px; margin-top: 14px; }
.rr-panel .klanehead { display: flex; justify-content: space-between; align-items: baseline; font-weight: 700; color: var(--lc); margin-bottom: 8px; }
.rr-panel .kbl { font-weight: 600; }
.rr-panel details.kmore > summary { cursor: pointer; font-size: var(--font-ui-smaller); color: var(--text-accent, hsl(210,70%,52%)); }
.rr-panel details.kmore ul { margin: 6px 0 2px; padding-left: 16px; font-size: var(--font-ui-smaller); line-height: 1.45; }
.rr-panel details.kmore li { margin-bottom: 4px; }
.rr-panel .kplan { font-size: var(--font-ui-smaller); color: var(--text-muted); font-weight: 600; }
.rr-panel .khecho .kgrid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px; }`, root);
const campoDe = (t, k) => { const c = (t.children ?? []).find((c) => new RegExp('^\\*\\*' + k + ':\\*\\*').test(String(c.text).trim())); return c ? String(c.text).replace(new RegExp('^\\s*\\*\\*' + k + ':\\*\\*\\s*'), '').trim() : null; };
const LINEAS = ['Contenidos', 'Link building', 'Gestión'];
const lineaDe = (t, resp) => { const l = campoDe(t, 'Línea'); if (l) return LINEAS.find((x) => x.toLowerCase() === l.toLowerCase()) ?? l; return /Nina/.test(resp ?? '') ? 'Gestión' : 'Contenidos'; };
const kanbanDe = (t) => { const v = campoDe(t, 'Kanbanize'); if (!v) return null; const m = v.match(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/) ?? v.match(/(https?:\/\/\S+)/); return m ? { label: m[2] ? m[1] : 'Kanbanize', url: m[2] ?? m[1] } : null; };
const detalleDe = (t) => (t.children ?? []).map((c) => String(c.text).trim()).filter((x) => !/^(\*\*(Línea|Responsable|Kanbanize):\*\*|Fuente:)/.test(x));
const mdHtml = (x) => x.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a class="external-link" href="$2" target="_blank" rel="noopener">$1</a>').replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (m, a, b) => `<a class="internal-link" data-href="${a}" href="${a}">${b ?? a}</a>`);
const respDe = (t) => { const c = (t.children ?? []).find((c) => /^\*\*Responsable:\*\*/.test(String(c.text).trim())); return c ? String(c.text).replace(/^\s*\*\*Responsable:\*\*\s*/, '').replace(/\s*\(.*\)\s*$/, '').trim() : null; };
const urlsTareas = new Set(ts.flatMap((t) => txtAll(t).match(/https?:\/\/[^)\s\]]+/g) ?? []));
const K = { cliente: [], curso: [], backlog: [], hecho: [] };
for (const t of ts) {
  const sec = t.section?.subpath ?? ''; const quien = sec.includes('Cliente') ? 'cliente' : sec.includes('Runroom') ? 'runroom' : null; if (!quien) continue;
  const f = fechaDe(t); const it = { origen: 'Tarea', txt: limpia(t.text), dias: f ? Math.round(hoy.diff(f, 'days').days) : null, links: linksDe(t), motivo: null, resp: respDe(t), kb: kanbanDe(t), det: detalleDe(t) }; it.linea = lineaDe(t, it.resp);
  (quien === 'cliente' ? K.cliente : t.status === '/' ? K.curso : K.backlog).push(it);
}
const hechasPen = pen ? pen.file.tasks.where((t) => !t.parent && t.completed && /Runroom|Cliente/.test(t.section?.subpath ?? '')).array() : [];
for (const t of hechasPen) { const r = respDe(t); K.hecho.push({ origen: 'Tarea', txt: limpia(t.text), dias: null, links: linksDe(t), motivo: null, resp: r, kb: kanbanDe(t), linea: lineaDe(t, r), det: detalleDe(t) }); }
for (const t of estTasks) {
  const k = tipo(t); if (k === 'descartado') continue;
  if (t.basecamp && urlsTareas.has(String(t.basecamp).trim()) && k !== 'hecho') continue;
  const pel = String(t.pelota ?? '').toLowerCase();
  const it = { origen: k === 'duda' ? 'Sin confirmar' : 'Estrategia', txt: limpia(t.text), dias: null, links: [t.basecamp ? { label: 'Basecamp', url: String(t.basecamp) } : null, t.fuente ? { label: /drive\.google/.test(String(t.fuente)) ? (/1XG4Q4Ua9j3D/.test(String(t.fuente)) ? 'Estrategia Beyond 26/27' : 'Documento de Drive') : (/spreadsheets/.test(String(t.fuente)) ? 'Sheet' : 'Fuente'), url: String(t.fuente) } : null].filter(Boolean), motivo: t.motivo ? String(t.motivo) : null, resp: null, sec: t.section?.subpath ?? '', kb: t.kanbanize ? { label: 'Kanbanize', url: String(t.kanbanize) } : null, plan: t.plan ? String(t.plan) : null, ini: t.inicio ? fecha(String(t.inicio).slice(0, 7) + '-01') : null, fin: t.fin ? fecha(String(t.fin).slice(0, 7) + '-01')?.endOf('month') : null, est: k, linea: /link/i.test(t.section?.subpath ?? '') ? 'Link building' : /gesti/i.test(t.section?.subpath ?? '') ? 'Gestión' : 'Contenidos' };
  if (k === 'hecho') K.hecho.push(it); else if (k === 'cliente' || (k === 'parcial' && pel === 'cliente')) K.cliente.push(it); else if (k === 'parcial') K.curso.push(it); else K.backlog.push(it);
}
const tarjeta = (i, cont, kc) => {
  const c = el('div', 'kcard' + (i.dias != null && i.dias > 30 ? ' old' : ''), null, cont); c.style.setProperty('--kc', kc);
  const tt = el('div', null, null, c); el('span', `tag ${i.origen === 'Tarea' ? 'bc' : 'est'}`, i.origen, tt); tt.append(' ' + i.txt);
  if (i.det && i.det.length) { const dd = el('details', 'kmore', null, c); el('summary', null, 'Ver contexto', dd); const ul = el('ul', null, null, dd); for (const x of i.det) { const li = el('li', null, null, ul); li.innerHTML = mdHtml(x); } }
  if (i.motivo) el('div', 'muted sub', i.motivo, c);
  if (i.plan) { const p = el('div', 'kplan', `📅 ${i.plan}`, c); const hecho = i.est === 'hecho'; if (!hecho && i.fin && hoy > i.fin) { p.style.color = ROJO; p.textContent += ' · fuera de plazo'; } else if (!hecho && i.est !== 'parcial' && i.ini && hoy >= i.ini) { p.style.color = NARANJA; p.textContent += ' · debería estar en marcha'; } }
  const meta = el('div', 'kmeta', null, c);
  if (i.resp) el('span', null, '👤 ' + i.resp, meta);
  if (i.dias != null) { const d = el('span', null, `⏱ ${i.dias} d`, meta); if (i.dias > 7) d.style.color = i.dias > 30 ? ROJO : NARANJA; }
  if (i.sec && i.origen !== 'Tarea') el('span', null, i.sec, meta);
  if (i.kb) { const a = el('a', 'external-link kbl', `🗂️ ${i.kb.label}`, el('div', 'klinks', null, c)); a.href = i.kb.url; a.target = '_blank'; a.rel = 'noopener'; a.title = 'Card en Kanbanize (contexto completo)'; }
  if (i.links && i.links.length) { const lk = el('div', 'klinks', null, c); for (const l of i.links) { const a = el('a', 'external-link', etiqueta(l), lk); a.href = l.url; a.target = '_blank'; a.rel = 'noopener'; a.title = l.label; } } else el('div', 'kmeta', '⚠️ sin enlace de referencia', c);
};
const nViejas = K.cliente.filter((i) => (i.dias ?? 0) > 7).length;
const card = el('div', 'card', null, root);
cabecera(card, null, 'Estrategia + Basecamp, correo y actas', 'Tablero de tareas', `${K.cliente.length} esperando al cliente · ${K.curso.length} en curso · ${K.backlog.length} en backlog · ${K.hecho.length} hechas`, `${nViejas} del cliente con más de 7 días`, nViejas ? NARANJA : VERDE);
const COLS = [['backlog', '⬜ Backlog (sin empezar)', 'hsl(210, 12%, 58%)'], ['cliente', '🟧 Esperando al cliente', NARANJA], ['curso', '🟦 En curso (nosotros)', AZUL]];
const LCOL = { 'Contenidos': 'hsl(265, 45%, 55%)', 'Link building': 'hsl(180, 55%, 38%)', 'Gestión': 'hsl(32, 20%, 50%)' };
const LQUIEN = { 'Contenidos': 'Olga', 'Link building': 'Olga', 'Gestión': 'Nina' };
const lineas = [...LINEAS, ...new Set([...K.backlog, ...K.cliente, ...K.curso].map((i) => i.linea).filter((l) => !LINEAS.includes(l)))];
for (const lin of lineas) {
  const enLin = (k) => K[k].filter((i) => i.linea === lin);
  const tot = COLS.reduce((a, [k]) => a + enLin(k).length, 0); if (!tot) continue;
  const lane = el('div', 'klane', null, card); lane.style.setProperty('--lc', LCOL[lin] ?? 'var(--text-muted)');
  const lh = el('div', 'klanehead', null, lane); el('span', null, `${lin}${LQUIEN[lin] ? ' · ' + LQUIEN[lin] : ''}`, lh); el('span', 'muted', `${tot} pendientes`, lh);
  const kb = el('div', 'kb', null, lane);
  for (const [k, titulo, kc] of COLS) {
    const lista = enLin(k);
    const col = el('div', 'kcol', null, kb); col.style.setProperty('--kc', kc);
    const h = el('div', 'khead', null, col); el('span', null, titulo, h); el('span', 'muted', String(lista.length), h);
    const tareas = lista.filter((i) => i.origen === 'Tarea').sort((a, b) => (b.dias ?? -1) - (a.dias ?? -1));
    const est2 = lista.filter((i) => i.origen !== 'Tarea').sort((a, b) => (a.ini ? a.ini.toMillis() : 9e15) - (b.ini ? b.ini.toMillis() : 9e15));
    for (const i of tareas) tarjeta(i, col, kc);
    if (est2.length) { if (k === 'backlog') { const d = el('details', 'kdet', null, col); el('summary', null, `Estrategia Beyond 26/27 · ${est2.length}`, d); for (const i of est2) tarjeta(i, d, kc); } else for (const i of est2) tarjeta(i, col, kc); }
    if (!lista.length) el('div', 'muted', 'Nada por aquí', col);
  }
}
{ const dh = el('details', 'kdet khecho', null, card); el('summary', null, `✅ Hecho · ${K.hecho.length}`, dh); const gh = el('div', 'kgrid', null, dh); for (const i of K.hecho) tarjeta(i, gh, VERDE); }
el('div', 'muted', 'En el Pendientes, las tareas nuestras van con [ ] si están en backlog y con [/] si están en curso. En la estrategia, [/] es en curso y [ ] es backlog. Lo del cliente va siempre a su columna.', card);

// Marcar tareas (casillas reales: al marcar aquí se marca en la nota de origen)
const det = el('div', 'card', null, root);
el('div', 'eyebrow', 'Marcar como hecho', det);
el('div', 'muted', 'Marca la casilla cuando una tarea esté hecha. Se guarda en la nota de origen (Claude/Datos).', det);

dv.header(4, '🟦 Nuestro (en curso y backlog)');
dv.taskList(pen ? pen.file.tasks.where((t) => !t.parent && !t.completed && t.status !== '-' && (t.section?.subpath ?? '').includes('Runroom')) : [], false);
dv.header(4, '🟧 Esperando al cliente');
dv.taskList(pen ? pen.file.tasks.where((t) => !t.parent && !t.completed && t.status !== '-' && (t.section?.subpath ?? '').includes('Cliente')) : [], false);

```
