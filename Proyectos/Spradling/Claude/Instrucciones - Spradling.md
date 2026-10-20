# Instrucciones para Claude — Spradling

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente.

## Tono y estilo con el cliente
- Relación cercana y de confianza con el equipo de Spradling Europe (tuteo, charla informal, bromas) — no hace falta un tono excesivamente formal.
- La comunicación de problemas técnicos o errores (bugs, bloqueos, plazos que no se van a cumplir) es directa y transparente, sin rodeos — así se gestiona internamente entre Runroom y el cliente.

## Cosas que nunca debo hacer o decir
*(pendiente — completar)*

## Aprobaciones necesarias antes de actuar
- Cualquier trabajo de configuración de GTM/CRM fuera del alcance estándar (p. ej. creación de eventos/acciones de conversión en SugarCRM) se factura aparte — no asumir sin confirmar presupuesto/horas con Nina o Araceli (acordado en reunión de julio 2026).

## Otros
- Cuenta multi-país (6 geografías, agrupadas en Grupo 1: Alemania/UK/Polonia y Grupo 2: España/Italia/Francia) — tener en cuenta el reparto de presupuesto al hablar de inversión.
- El equipo de Colombia (desarrollo + analítica) es difícil de coordinar directamente; casi toda la comunicación pasa por Delia.
- Las "Notas de Gemini" de varias reuniones transcriben "Runroom" como "Randroom"/"Ranroom" — es un error de transcripción, no una agencia externa distinta.


## Cómo mantener esta carpeta (patrón LLM Wiki)
Esta carpeta sigue el patrón de "wiki persistente" de Karpathy: las fuentes en bruto (Reuniones/Raw, los emails y Basecamp) se leen pero nunca se modifican; esta carpeta es la wiki que Claude mantiene a partir de ellas; este fichero es el "esquema" que dice cómo hacerlo.

- **Ingest** (llega una fuente nueva, p. ej. una transcripción en `Reuniones/Raw/`): léela entera, resume lo clave, guarda la versión trabajada en `Reuniones/Procesadas/`, actualiza las secciones que correspondan de `Spradling.md` (no todo al final) y añade a `Pendientes - Spradling.md` cualquier tarea nueva que salga de ahí. Registra la entrada en `Log - Spradling.md`.
- **Query** (me preguntas algo sobre este cliente): contesto a partir de lo que ya hay en esta carpeta, no repito la búsqueda desde cero. Si la respuesta genera algo que vale la pena conservar (un análisis, una comparación, una decisión), te lo ofrezco para guardarlo aquí en vez de que se quede solo en el chat.
- **Lint** (me pides una revisión): reviso esta carpeta buscando contradicciones entre notas, datos que parezcan desactualizados, huecos de información y referencias cruzadas que falten, y te los señalo.
