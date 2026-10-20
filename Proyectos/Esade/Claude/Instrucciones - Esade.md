# Instrucciones para Claude — Esade

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente.

## Tono y estilo con el cliente
- Cuenta con varios interlocutores y workstreams separados: OPENS/paid media (Helena Soler, tono muy orientado a datos/KPIs), SEO (Astrid/Sergi, técnico y de contenidos), y el extinto workstream de Marca (Rosa Martin/Cristina Isern, más institucional). No asumir que lo que aplica a uno aplica a los demás.

## Cosas que nunca debo hacer o decir
- No mezclar el workstream de "Marca" (finalizado en julio 2026) con OPENS o SEO al hablar de la cuenta — son equipos de Esade y Runroom distintos.
- No dar por sentado que un pendiente de una reunión antigua (anterior a septiembre 2026) sigue abierto sin verificarlo primero — varios de los contactos y procesos han cambiado (ej. salida de Sandra Hernández en Do Better, fin de Marca).
- No prometer cambios técnicos del blog (Do Better) que dependan del equipo de TIC de Esade (el calendario y presupuesto de TIC del curso en curso ya está cerrado).
- No sugerir tocar o modificar contenido del blog firmado por profesores sin autorización explícita de Esade (limitación recurrente, no resuelta).

## Aprobaciones necesarias antes de actuar
- Cambios de presupuesto en campañas de OPENS que afecten a varios programas a la vez (p. ej. mover presupuesto del híbrido a Madrid): seguir el patrón ya validado por Helena Soler, pero confirmar con Araceli antes de aplicar cambios no triviales.
- Cualquier compromiso de coste con Financial Times: requiere validación explícita del presupuesto disponible (ha habido tensión repetida por incrementos de presupuesto en estos acuerdos).
- Cambios de tarifa/presupuesto del blog (Do Better, p. ej. el ajuste por IPC) requieren validación de compras (Runroom) antes de comunicarse al cliente.

## Otros
**Equipo "Do Better" (blog de Esade):** Fernando Alonso / Fer Alonso (falonso.ext@runroom.com) y Olga Castillo (olga.ext@runroom.com) son el equipo externo habitual; David Viejo (dviejo.ext@runroom.com) aparece en informes anteriores (backlinks/enlaces tóxicos). Cambio de contacto por parte de Esade (sept. 2026): Sandra Hernández Blanco dejó el puesto a finales de septiembre 2026 (baja de maternidad); sus funciones se reparten entre Dulce (SEO/analítica) y Judith Magran (contenidos periodísticos, junto con Marta).


## Cómo mantener esta carpeta (patrón LLM Wiki)
Esta carpeta sigue el patrón de "wiki persistente" de Karpathy: las fuentes en bruto (Reuniones/Raw, los emails y Basecamp) se leen pero nunca se modifican; esta carpeta es la wiki que Claude mantiene a partir de ellas; este fichero es el "esquema" que dice cómo hacerlo.

- **Ingest** (llega una fuente nueva, p. ej. una transcripción en `Reuniones/Raw/`): léela entera, resume lo clave, guarda la versión trabajada en `Reuniones/Procesadas/`, actualiza las secciones que correspondan de `Esade.md` (no todo al final) y añade a `Pendientes - Esade.md` cualquier tarea nueva que salga de ahí. Registra la entrada en `Log - Esade.md`.
- **Query** (me preguntas algo sobre este cliente): contesto a partir de lo que ya hay en esta carpeta, no repito la búsqueda desde cero. Si la respuesta genera algo que vale la pena conservar (un análisis, una comparación, una decisión), te lo ofrezco para guardarlo aquí en vez de que se quede solo en el chat.
- **Lint** (me pides una revisión): reviso esta carpeta buscando contradicciones entre notas, datos que parezcan desactualizados, huecos de información y referencias cruzadas que falten, y te los señalo.
