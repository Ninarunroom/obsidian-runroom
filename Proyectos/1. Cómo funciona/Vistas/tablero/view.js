// Tablero de tareas común a todos los clientes (formato Kanbanize).
// Uso en una nota:  await dv.view(<ruta a esta carpeta>, { pendientes: "Pendientes - <Cliente>", cliente: "<Cliente>" })
// Columnas: 📥 Backlog · 🟦 Pendiente Runroom · 🟧 Pendiente cliente, y ✅ Done plegado debajo.
// Lee las secciones "## …" del Pendientes: Backlog → Backlog; Runroom → Pendiente Runroom; Cliente → Pendiente cliente;
// Done → Done. Las tareas [x] o [-] van siempre a Done. Otras secciones caen en Pendiente Runroom con su nombre como etiqueta.
const { pendientes, cliente } = input;
const root = dv.container; root.classList.add('rr-tablero');
const pen = dv.pages().where((p) => p.file.name === pendientes).first();
if (!pen) { dv.paragraph(`No encuentro la nota «${pendientes}».`); return; }
const txt = await dv.io.load(pen.file.path);
const secc = []; let act = null;
for (const l of txt.split('\n')) {
  const h = l.match(/^##+ (.*)/); if (h) { act = h[1].trim(); continue; }
  if (!act || /^Status/i.test(act)) continue;
  const m = l.match(/^- \[(.)\] (.*)/);
  if (m) { secc.push({ s: act, st: m[1], head: m[2], body: [] }); continue; }
  if (/^\s{2,}- /.test(l) && secc.length) secc[secc.length - 1].body.push(l.trim().slice(2));
}
const col = (c) => {
  if (['x', 'X', '-'].includes(c.st) || /done|hecho/i.test(c.s)) return 'done';
  if (/backlog/i.test(c.s)) return 'backlog';
  if (/cliente/i.test(c.s)) return 'cliente';
  return 'runroom';
};
const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const md = (s) => esc(s)
  .replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, '<a class="internal-link" data-href="$1" href="$1">$2</a>')
  .replace(/\[\[([^\]]+)\]\]/g, '<a class="internal-link" data-href="$1" href="$1">$1</a>')
  .replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g, '<a class="external-link" href="$2" target="_blank" rel="noopener">$1</a>')
  .replace(/\*\*(.+?)\*\*/g, '<b>$1</b>').replace(/`([^`]+)`/g, '<code>$1</code>');
const dias = (c) => { const m = (c.head + ' ' + c.body.join(' ')).match(/(?:Esperando desde|detectado)[:*\s]*?(\d{2})\/(\d{2})\/(\d{4})/i); return m ? Math.round(dv.date('today').diff(dv.date(`${m[3]}-${m[2]}-${m[1]}`), 'days').days) : null; };
const COLS = [
  { k: 'backlog', t: '📥 Backlog', c: 'var(--text-faint)' },
  { k: 'runroom', t: '🟦 Pendiente Runroom', c: 'hsl(210, 70%, 52%)' },
  { k: 'cliente', t: '🟧 Pendiente cliente', c: 'hsl(32, 85%, 52%)' },
];
const tarjeta = (parent, c, color, hecha) => {
  const d = parent.createEl('details', { cls: 'kcard' + (hecha ? ' kdone' : '') }); d.style.setProperty('--kc', color);
  let head = c.head; const etiquetas = [];
  let m; while ((m = head.match(/^\*\*\[([^\]]+)\]\*\*\s*/))) { etiquetas.push(m[1]); head = head.slice(m[0].length); }
  if (cliente) head = head.replace(new RegExp('^' + cliente.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\s*—\\s*'), '');
  if (col(c) === 'runroom' && !/runroom/i.test(c.s)) etiquetas.push(c.s.replace(/^[^\p{L}]+/u, ''));
  if (c.st === '/') etiquetas.push('en curso');
  const n = hecha ? null : dias(c);
  d.createEl('summary').innerHTML = (n != null ? `<span class="kdays">${n} d</span>` : '') + etiquetas.map((e) => `<span class="ktype">${esc(e)}</span>`).join('') + md(head);
  if (c.body.length) { const ul = d.createEl('ul'); for (const b of c.body) ul.createEl('li').innerHTML = md(b); }
};
const kb = root.createEl('div', { cls: 'kboard' });
for (const C of COLS) {
  const lista = secc.filter((c) => col(c) === C.k);
  const box = kb.createEl('div', { cls: 'kcol' }); box.style.setProperty('--kc', C.c);
  const h = box.createEl('h4'); h.createEl('span', { text: C.t }); h.createEl('span', { cls: 'kn', text: String(lista.length) });
  if (!lista.length) box.createEl('div', { cls: 'kvacio', text: 'Nada por aquí' });
  for (const c of lista) tarjeta(box, c, C.c, false);
}
const hechas = secc.filter((c) => col(c) === 'done');
const db = root.createEl('details', { cls: 'kdonebox' });
db.createEl('summary', { text: `✅ Done · ${hechas.length}` });
const dg = db.createEl('div', { cls: 'kdonegrid' });
for (const c of hechas.slice().reverse()) tarjeta(dg, c, 'hsl(125, 55%, 45%)', true);
