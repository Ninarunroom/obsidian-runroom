# Instrucciones para Claude — BAU - Hubspot

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente.

## Tono y estilo con el cliente
- Conversación técnica orientada a HubSpot/automatizaciones (workflows, plantillas, segmentación); tono cercano, de trabajo conjunto entre Idoia/Julia (Runroom) y Guillermo/Adrià (BAU).

## Cosas que nunca debo hacer o decir
- No activar/mostrar canales o comunicaciones (p. ej. WhatsApp) a público no segmentado correctamente sin confirmar antes con el cliente — ya han pedido explícitamente restringir ciertos canales por idioma/país (ej. no mostrar WhatsApp a estudiantes no españoles).

## Aprobaciones necesarias antes de actuar
- Cualquier plantilla de WhatsApp Business nueva requiere aprobación de Meta antes de poder enviarse — no asumir que está lista sin confirmarlo.
- Cambios de consentimiento/checkbox legal en formularios: consultar con el equipo legal antes de implementar (mencionado explícitamente en la reunión de febrero 2026).

## Otros
- Verificar con Guillermo/Idoia el estado actual del proyecto de WhatsApp para Grados y de la traducción al catalán de las comunicaciones de Grados (última reunión documentada es de febrero 2026, sin seguimiento posterior en este Drive).


## Cómo mantener esta carpeta (patrón LLM Wiki)
Esta carpeta sigue el patrón de "wiki persistente" de Karpathy: las fuentes en bruto (Reuniones/Raw, los emails y Basecamp) se leen pero nunca se modifican; esta carpeta es la wiki que Claude mantiene a partir de ellas; este fichero es el "esquema" que dice cómo hacerlo.

- **Ingest** (llega una fuente nueva, p. ej. una transcripción en `Reuniones/Raw/`): léela entera, resume lo clave, guarda la versión trabajada en `Reuniones/Procesadas/`, actualiza las secciones que correspondan de `BAU - Hubspot.md` (no todo al final) y añade a `Pendientes - BAU - Hubspot.md` cualquier tarea nueva que salga de ahí. Registra la entrada en `Log - BAU - Hubspot.md`.
- **Query** (me preguntas algo sobre este cliente): contesto a partir de lo que ya hay en esta carpeta, no repito la búsqueda desde cero. Si la respuesta genera algo que vale la pena conservar (un análisis, una comparación, una decisión), te lo ofrezco para guardarlo aquí en vez de que se quede solo en el chat.
- **Lint** (me pides una revisión): reviso esta carpeta buscando contradicciones entre notas, datos que parezcan desactualizados, huecos de información y referencias cruzadas que falten, y te los señalo.
