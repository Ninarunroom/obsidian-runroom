# Instrucciones para Claude — Hispano Suiza

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente.

## Tono y estilo con el cliente
- Trato cercano e informal (tuteo) con Pablo y Pipo; conversación muy técnica y colaborativa, con jerga de marketing en inglés mezclada con el español de forma natural (BTR, CTR, VTR, Awareness, Demand Gen).
- Nina/el equipo de Runroom suele ir mostrando datos y proponiendo, y el cliente valida o ajusta en el momento (p. ej. exclusión de keywords, reparto de presupuesto por target).

## Cosas que nunca debo hacer o decir
- No especular ni comunicar externamente nada sobre la negociación en curso de un socio/partner industrial para la "fase 2" de Hispano Suiza, ni sobre la decisión estratégica de la familia propietaria (vía supercar vs. hypercar+hibridación). Es información interna sensible y no cerrada.

## Aprobaciones necesarias antes de actuar
- Cambios de presupuesto o de facturación: requieren confirmación explícita de Pablo (así se ha hecho en la revisión de presupuesto de septiembre 2026).
- Exclusión de keywords o cambios relevantes de segmentación en campañas: se revisan y acuerdan con Pablo antes de aplicarlos (p. ej. exclusiones de "Car", "Cars", etc. en marzo 2026).

## Otros
*(pendiente — completar)*


## Cómo mantener esta carpeta (patrón LLM Wiki)
Esta carpeta sigue el patrón de "wiki persistente" de Karpathy: las fuentes en bruto (Reuniones/Raw, los emails y Basecamp) se leen pero nunca se modifican; esta carpeta es la wiki que Claude mantiene a partir de ellas; este fichero es el "esquema" que dice cómo hacerlo.

- **Ingest** (llega una fuente nueva, p. ej. una transcripción en `Reuniones/Raw/`): léela entera, resume lo clave, guarda la versión trabajada en `Reuniones/Procesadas/`, actualiza las secciones que correspondan de `Hispano Suiza.md` (no todo al final) y añade a `Pendientes - Hispano Suiza.md` cualquier tarea nueva que salga de ahí. Registra la entrada en `Log - Hispano Suiza.md`.
- **Query** (me preguntas algo sobre este cliente): contesto a partir de lo que ya hay en esta carpeta, no repito la búsqueda desde cero. Si la respuesta genera algo que vale la pena conservar (un análisis, una comparación, una decisión), te lo ofrezco para guardarlo aquí en vez de que se quede solo en el chat.
- **Lint** (me pides una revisión): reviso esta carpeta buscando contradicciones entre notas, datos que parezcan desactualizados, huecos de información y referencias cruzadas que falten, y te los señalo.

## Kanbanize (cards de tareas)
Lo leen las skills de preparación y de después de reunión (y es la misma lógica en Spradling y Barraquer).
- **Reglas de Nina para las cards**: **nunca se pone responsable** en ninguna card. **Tipo de card siempre**. **Fecha** solo si aplica (fecha comprometida o de entrega). **Antes de crear o cambiar una card, Claude le dice a Nina cómo la va a crear y dónde, y espera su OK.**
- **Cards recurrentes de Presupuestos y Facturación**: las crea en Kanbanize la tarea programada "Kanbanize - Cards recurrentes performance" (lunes 8:47, columna Ready). **En Obsidian no se crean** (ni la semanal de Presupuesto ni la mensual de Facturación): en Pendientes solo van tareas pendientes nuestras o del cliente.
- **Tipos del tablero Sky**: 13 Landings · 15 Informes · 18 Propuestas · 22 Implementación analítica · 24 Lanzamiento de campaña · 25 Optimización de campañas · 26 Control presupuestario · 27 Implementación canal · 30 Proyecto · 57 Test a/b.
- **Tablero**: Sky (board_id 21), en `https://runroom.kanbanize.com`. Workflow **Performance** (80), carril **Transversal** (116). Código Paprika en el campo personalizado **field_id 9**.
- **Dónde entran**: columna **Backlog → Hispano Suiza** (1679).
- **Parent card**: [51523 · Hispano Suiza Campañas 2026](https://runroom.kanbanize.com/ctrl_board/21/cards/51523/details/)
- **Código Paprika**: **HIS010010 (2026)**. El de 2027 será otro: cuando Nina lo diga, apuntarlo aquí y en la tarea "Kanbanize - Cards recurrentes performance".
- **Formato de las cards de Hispano Suiza**: título `Hispano Suiza - <tarea>`, prioridad media, color rojo (af0020), etiqueta 639.
- **Basecamp para compartir actas**: Hispano Suiza - Performance Media (19038192).
