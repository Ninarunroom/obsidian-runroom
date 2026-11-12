---
tipo: sistema
tipologia: performance
actualizado: 2026-11-12
clientes: [Barraquer, Spradling, Hispano Suiza]
---
# Sistema — Performance (Barraquer, Spradling, Hispano Suiza)

← [[Sistema de gestión]]

Qué automatizaciones y reglas hay para **Barraquer, Spradling e Hispano Suiza**, dónde vive cada cosa y qué queda pendiente. El detalle de cada cliente está en su `Claude/Instrucciones - <Cliente>.md`, que **manda** sobre las tareas y las skills.

- [[Instrucciones - Barraquer]] · [[Instrucciones - Spradling]] · [[Instrucciones - Hispano Suiza]]

## 1. Reglas
Las reglas comunes están en [[Sistema de gestión]]. Aquí solo lo propio de performance.

## 2. Tareas programadas
| Tarea                                               | Cuándo     | Qué hace                                                                                                                                                                            | Ordenador |
| --------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **Kanbanize - Cards recurrentes performance**       | Lunes 8:47 | Crea las cards del planning (ver punto 4) y notifica lo creado                                                                                                                      | No        |
| **Preparación de reuniones de cliente (día antes)** | L-V 16:13  | Prepara las reuniones del día laborable siguiente con Barraquer, Spradling e Hispano Suiza (status e informe): nota en `Reuniones/Preparación/` + notificación con "En 30 segundos" | Sí        |
| **Barraquer - Actas de reunión**                    | L-V 17:43  | Notas de Gemini → acta, KB y Pendientes; mueve las notas a la carpeta de actas                                                                                                      | Sí        |
| **Spradling - Actas de reunión**                    | L-V 17:52  | Igual, para Spradling                                                                                                                                                               | Sí        |
| **Alertas Barraquer → Obsidian**                    | L-V 9:45   | Copia las alertas diarias de Google Ads de Barraquer                                                                                                                                | Sí        |

La tarea diaria de Basecamp (común a todos los clientes) está en [[Sistema de gestión]].

Hispano Suiza **no** tiene tarea de actas: su acta se procesa al lanzar la skill de después de reunión.

## 3. Skills (se lanzan a mano)
- **preparar-reunion-cliente** — "prepárame la reunión de X": acta previa con lo último hablado, estado de tareas, temas abiertos, orden del día y qué pedir. Es la misma lógica que usa la tarea de las 16:13.
- **despues-reunion-cliente** — tras una reunión: procesa las notas de Gemini (si la tarea de actas no lo ha hecho ya; el registro "Actas procesadas" evita duplicados), prepara el acta y los next steps para Basecamp (se publican con OK) y crea las cards de Kanbanize de nuestras tareas, con descripción, **contexto previo** con enlaces, fecha si aplica, Paprika y parent card. Antes de crear, dice cómo y dónde, y espera el OK.

## 4. Kanbanize
**Dónde**: tablero **Sky** → workflow Performance → carril Transversal. Cards hijas de la parent card del cliente. Título `<Cliente> - <tarea>`.
**Reglas**: **nunca responsable** · **tipo siempre** · fecha solo si aplica · antes de crear una card a mano, Claude dice cómo y dónde.

| | Barraquer | Spradling | Hispano Suiza |
|---|---|---|---|
| Parent card | 51536 · Barraquer campañas 2026 | 52124 · Spradling Campañas 2026 | 51523 · Hispano Suiza Campañas 2026 |
| Columna Backlog | Barraquer (y Barraquer Dubai) | Spradling | Hispano Suiza |
| Paprika 2026 | BAR020061 | SPR010023 | HIS010010 |
| Paprika 2027 | BAR020066 | SPR010024 | pendiente |
| Color | verde | amarillo | rojo |

**Cards recurrentes** (las crea la tarea de los lunes):
| Card | Cuándo se crea | Columna | Tipo | Fecha | Otros |
|---|---|---|---|---|---|
| `<Cliente> - Presupuestos` (los 3) | Cada lunes | Ready | Control presupuestario | Viernes de la semana | — |
| `<Cliente> - Facturación` (los 3) | Lunes de la semana en que vence | Ready | Control presupuestario | 2º día laborable del mes | Subtask "Review Nina" (Barraquer, también las suyas) |
| `Barraquer - Informe mensual` | Semana antes de la "Status barraquer / RR" (calendario) | Ready | Informes | Día de la reunión | Sticker Fixed-date |
| `Spradling - Informe trimestral Qn` | Lunes de la semana del 15 de mar, jun, sep y dic | Backlog Spradling | Informes | Sin fecha | Recordatorio para escribir al cliente y fijar la reunión |
| `Hispano Suiza - Informe mensual <mes>` | Semana del primer día laborable del mes | Ready | Informes | Sin fecha | La fecha la cierra Nina con Ari |

Ninguna se duplica. Si falta el Paprika del año, la tarea no crea la card y avisa. También avisa si la parent card no es del año.

## 5. Reuniones
| Cliente | Reuniones | Preparación | Después |
|---|---|---|---|
| Barraquer | "Status barraquer" (30 min, quincenal, martes) y "Status barraquer / RR" (1,5 h, informe mensual, jueves) | Día antes, 16:13 | Tarea de actas 17:43 + skill |
| Spradling | Trimestral (abril, julio, octubre, enero), sin agendar | Cuando esté en el calendario | Tarea de actas 17:52 + skill |
| Hispano Suiza | Mensual, la fecha la cierra Nina | Cuando esté en el calendario | Skill |

## 6. Dónde está cada cosa (por cliente)
- **Instrucciones** (reglas, rutas, Kanbanize, Basecamp): `Claude/Instrucciones - <Cliente>.md`
- **Pendientes**: Barraquer y Spradling en `Claude/Datos/Pendientes - <Cliente>.md`; Hispano Suiza en `Pendientes - Hispano Suiza.md`
- **Actas**: `3. Reuniones/Raw` y `Procesadas` (Hispano Suiza: `Reuniones/`)
- **Preparación de reuniones**: `3. Reuniones/Preparación/` (Hispano Suiza: `Reuniones/Preparación/`)
- **Log**: `Claude/Log - <Cliente>.md` (Hispano Suiza: `Log - Hispano Suiza.md`)

## 7. Pendiente
- [ ] **Paprika 2027 de Hispano Suiza**: cuando lo haya, apuntarlo en sus Instrucciones y en la tarea de Kanbanize.
- [ ] **Parent cards 2027**: cuando se creen, actualizarlas en las Instrucciones y en la tarea de Kanbanize.
- [ ] Decidir si la tarea de actas deja preparados el **borrador de Basecamp y las cards** para que Nina solo diga "adelante".
- [ ] Hispano Suiza: ¿tarea de actas y estructura de carpetas como Barraquer y Spradling?
- [ ] Las cards antiguas de Spradling y su parent card llevan el Paprika SPR010021 (el bueno de 2026 es SPR010023): cambiar solo si Nina lo pide.
