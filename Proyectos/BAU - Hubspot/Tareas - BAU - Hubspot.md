---
cssclasses:
  - rr-ancho
---
# Tareas — BAU - Hubspot

Tablero de tareas (mismo formato que Kanbanize). Los datos están en [[Pendientes - BAU - Hubspot]].

```dataviewjs
const f = dv.current().file.folder; const raiz = f.slice(0, f.indexOf('Proyectos/'));
await dv.view(raiz + 'Proyectos/1. Cómo funciona/Vistas/tablero', { pendientes: 'Pendientes - BAU - Hubspot', cliente: 'BAU - Hubspot' });
```
