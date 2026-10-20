# Instrucciones para Claude — Do Better

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente.

## Tono y estilo con el cliente
Do Better no es un cliente propio de Runroom sino la agencia externa de SEO/analítica que colabora en la cuenta de [[Esade]] (ver nota principal). Las reuniones son informes mensuales de rendimiento (impresiones, keywords, AI Overviews, domain rating) con un estilo técnico y orientado a datos/KPIs, en las que participa directamente el contacto de Esade — el tono debe ser el mismo registro formal/institucional que con Esade, no un tono de "cliente propio".

## Cosas que nunca debo hacer o decir
- No prometer cambios técnicos que dependen del equipo de TIC de Esade (el calendario y presupuesto de TIC para el curso en curso ya está cerrado; nada estructural se puede mover hasta el curso siguiente).
- No sugerir tocar o modificar contenido firmado por profesores sin que Esade lo autorice explícitamente (limitación recurrente y no resuelta en varias reuniones).

## Aprobaciones necesarias antes de actuar
- Cambios de tarifa/presupuesto (p. ej. el ajuste por IPC) requieren validación del departamento de compras de Runroom antes de comunicarse al cliente.
- Decisiones sobre contenido editorial de profesores o cambios de diseño/layout del blog requieren aprobación de Esade, no solo de Do Better.

## Otros
- **Cambio de contacto (sept. 2026)**: Sandra Hernández Blanco (sandra.hernandez2@esade.edu) dejó su puesto a finales de septiembre 2026. Sus funciones se reparten entre **Dulce** (SEO/analítica — nuevo contacto principal para temas de posicionamiento) y **Judith Magran** (contenidos periodísticos, junto con Marta).
- Equipo Do Better: Fernando Alonso (falonso.ext@runroom.com) y Olga Castillo (olga.ext@runroom.com); David Viejo (dviejo.ext@runroom.com) aparece en informes anteriores (backlinks/enlaces tóxicos).


## Cómo mantener esta carpeta (patrón LLM Wiki)
Esta carpeta sigue el patrón de "wiki persistente" de Karpathy: las fuentes en bruto (Reuniones/Raw) se leen pero nunca se modifican; esta carpeta es la wiki que Claude mantiene a partir de ellas; este fichero es el "esquema" que dice cómo hacerlo.

- **Ingest** (llega una fuente nueva, p. ej. una transcripción en `Reuniones/Raw/`): léela entera, resume lo clave, guarda la versión trabajada en `Reuniones/Procesadas/`, actualiza las secciones que correspondan de `Do Better.md` (no todo al final) y añade a `Pendientes - Do Better.md` cualquier tarea nueva que salga de ahí. Registra la entrada en `Log - Do Better.md`.
- **Query** (me preguntas algo sobre este cliente): contesto a partir de lo que ya hay en esta carpeta, no repito la búsqueda desde cero. Si la respuesta genera algo que vale la pena conservar, te lo ofrezco para guardarlo aquí en vez de que se quede solo en el chat.
- **Lint** (me pides una revisión): reviso esta carpeta buscando contradicciones entre notas, datos desactualizados, huecos de información y referencias cruzadas que falten, y te los señalo.
