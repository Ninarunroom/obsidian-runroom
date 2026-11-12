---
tipo: sistema
actualizado: 2026-11-12
---
# Sistema de gestión de clientes

Nota padre: reglas comunes, lo que es transversal a todos los clientes y el índice por tipología. El detalle de cada cliente está en su `Claude/Instrucciones - <Cliente>.md`, que **manda** sobre las tareas y las skills.

## Por tipología
| Tipología | Clientes | Nota | Estado |
|---|---|---|---|
| **Performance** | Barraquer, Spradling, Hispano Suiza | [[Sistema - Performance]] | Montado: KB, Kanbanize, cards recurrentes, preparación y actas |
| **SEO / contenidos** | Esade | [[Sistema - SEO y contenidos]] | KB y actas de SEO y Analítica; Kanbanize y preparación por definir |
| **CRM** | BAU - Hubspot | [[Sistema - CRM]] | Solo KB básico y tarea diaria; resto por definir |

## Reglas comunes
- **Pendientes sin paja**: solo tareas concretas, con dueño y fuente. Nada de "confirmar si…" genéricos, próximos pasos de grupo sin fecha ni cosas que no nos tocan.
- **Las tareas las cierra Claude**, no Nina: cuando Nina lo dice o Basecamp/correo lo dejan claro (`[x]` hecha, `[-]` ya no aplica, con motivo en el Log). Si hay duda, se pregunta.
- **Estrategia ≠ reuniones**: en la nota de estrategia solo va la propuesta anual. Lo que sale de reuniones o de Basecamp va a Pendientes (si está abierto) o a Propuestas y decisiones (si es una decisión).
- **Todo con fuente**: cada acción de estrategia y cada propuesta o decisión dice de dónde sale (PDF, acta o hilo), con enlace.
- **En Obsidian no hay cards recurrentes** (presupuesto, facturación): viven en Kanbanize.
- **Kanbanize**: nunca responsable · tipo siempre · fecha solo si aplica · Paprika del año · hija de la parent card del cliente · antes de crear una card a mano, Claude dice cómo y dónde y espera el OK.
- **Sin emails**: los avisos llegan como notificación al móvil.
- **Solo lectura** en Basecamp, Drive, Gmail y Calendar para las tareas automáticas. Publicar en Basecamp, solo con el OK de Nina.

## Transversal a todos los clientes
| Tarea programada | Cuándo | Qué hace | Ordenador |
|---|---|---|---|
| **Basecamp - Pendientes diarios** | L-V 10:12 | Lee los proyectos de Basecamp y el correo de todos los clientes; actualiza Pendientes, Status, contexto y alertas | Sí ⚠️ |

⚠️ Apunta a la carpeta antigua "Clientes RR": hay que cambiarla a `Documents/Obsidian/Runroom` en los ajustes de la tarea. Hasta entonces no escribe en Obsidian.

**Cómo se monta un cliente nuevo**: [[Prompt - KB de cliente]].

**Skills** (sirven para cualquier cliente con Instrucciones): **preparar-reunion-cliente** y **despues-reunion-cliente**. Ver [[Sistema - Performance]].

**Credenciales** (Basecamp y Kanbanize): dentro de las tareas programadas, nunca en la bóveda (la bóveda se sube a GitHub).

## Pendiente común
- [ ] Cambiar la carpeta de la tarea **Basecamp - Pendientes diarios** (Nina, en sus ajustes).
