---
cssclasses:
  - rr-ancho
---
# Tareas — Esade

Tablero de tareas (mismo formato que Kanbanize). Los datos están en [[Pendientes - Esade]].

```dataviewjs
const f = dv.current().file.folder; const raiz = f.slice(0, f.indexOf('Proyectos/'));
await dv.view(raiz + 'Proyectos/1. Cómo funciona/Vistas/tablero', { pendientes: 'Pendientes - Esade', cliente: 'Esade' });
```
