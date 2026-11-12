# Instrucciones para Claude — Esade Contenidos Beyond

Esto es lo que debo tener en cuenta (en chat o en las tareas programadas) antes de escribir o responder algo sobre el proyecto de contenidos y link building de Esade (blog **Beyond**). Es el **esquema** de la wiki: dice cómo está organizada la carpeta y cómo mantenerla. La ficha general de Esade (todas las líneas) es `Proyectos/Esade/Esade.md`, con sus propias Instrucciones en `Proyectos/Esade/Claude/`.

## Alcance
- **Entra**: contenidos del blog Beyond (keyword research y briefings de 2 artículos/mes, mejoras SEO y de conversión), link building (propuesta, compra y revisión de medios; estudio de la competencia; toxicidad y disavow), los KPIs mensuales para Astrid y la gestión de Nina (presupuesto, pedidos, facturación). Basecamp [ESADE SEO de Contenidos](https://basecamp.com/1771388/projects/15430351) y el correo de @esade.edu sobre estos temas (Astrid, Helen; Sergi y Natzir cuando hablan de Beyond).
- **No entra**: el fee de SEO técnico y analítica (`Esade/SEO y Analítica/`), Do Better (blog doBetter), OPENS y paid (Ari, Adsmurai), Eulerian y Medición LLMs. Si aparecen, se mencionan solo como contexto y sus tareas no van aquí (van al KB de su proyecto; ver [[Esade]]).
- **Zona gris**: los KPIs y análisis de Beyond los hace Fer, que también lleva el fee de SEO. Hasta que Nina diga a qué fee se imputan, las tareas de Beyond van aquí y sus horas no se suman sin confirmarlo.

## Tono y estilo con el cliente
- Astrid y Helen escriben en **castellano**; Sergi en **catalán**. Olga contesta en castellano; Fer, en valenciano con Sergi. Si Nina redacta, respeta el idioma del hilo.
- Astrid: mensajes cortos y concretos, firma "A". Helen: muy pendiente de importes y horas; quiere los números cuadrados y por escrito.

## Cosas que nunca debo hacer o decir
- No imputar a este proyecto ni mezclar en sus pendientes nada del fee de SEO y analítica, Do Better u OPENS.
- No comprometer presupuesto, horas, medios ni precios ante el cliente sin que Nina lo valide.
- No dar por publicado un medio sin el enlace del medio (to-do de Basecamp o Sheet).
- No sugerir tocar contenido firmado por profesores sin autorización de Esade.
- No guardar datos personales de candidatos ni leads.

## Aprobaciones necesarias antes de actuar
- Cualquier medio: lo valida Astrid (temática, URL, anchor y precio) y Comunicación.
- Cualquier cambio de presupuesto, pedido o precio/hora: lo decide Nina con Helen (y compras de Runroom para el PV de 2027).

## Otros
- "Elena" (Basecamp) y "Helen" son la **misma persona**: Elena Sánchez González.
- "Consumido" en el Sheet de medios = comprometido (aprobado), aunque el medio no haya publicado todavía.
- Proveedores de Esade que salen en los hilos: **Eleven** (redacta los artículos), **Vansters** (implementa cambios en Beyond).

---

## Estructura de la carpeta (patrón LLM Wiki de Karpathy)

Ruta: `Proyectos/Esade/Contenidos Beyond/`. Las carpetas están numeradas en orden de lectura. La nota de entrada es `1. Conocer la cuenta/00 Ficha de cliente - Esade Beyond.md`. Todo lo que es "de Claude" vive en `Claude/`.

```
Contenidos Beyond/
├── 1. Conocer la cuenta/   00 Ficha de cliente - Esade Beyond (puerta de entrada), Propuestas y decisiones - Esade Beyond,
│                           Cronología - Esade Beyond, Personas - Esade Beyond, Documentos - Esade Beyond,
│                           Líneas de trabajo - Esade Beyond (Contenidos, Link building, KPIs, Gestión)
├── 2. Acuerdos/            Acuerdos - Esade Beyond
├── 3. Reuniones/
│   ├── Raw/                transcripciones, NUNCA se modifican ("AAAA-MM-DD - Tema (transcripción).md"); Nina también deja aquí las suyas
│   └── Procesadas/         actas resumidas ("AAAA-MM-DD - Tema.md"), con enlace a su transcripción
├── 4. Seguimiento/        3 paneles dataviewjs: Tareas - Esade Beyond, Horas - Esade Beyond, Facturación y fee - Esade Beyond
└── Claude/                 de Claude: Datos/ (Pendientes - Esade Beyond, Estrategia 26-27 - seguimiento Esade Beyond,
                            Actas procesadas - Esade Beyond), Instrucciones - Esade Beyond, Log - Esade Beyond,
                            Datos panel - Esade Beyond, Fuentes/ (copias de Sheets a una fecha), Scripts/
```

## Operaciones

### Actas de reunión (tarea programada "Esade Beyond - Actas de reunión")
Las notas de Gemini se guardan solas en el Drive de Nina. La tarea las busca cada tarde, mira en `Claude/Datos/Actas procesadas - Esade Beyond.md` si ya están y, si son de contenidos o link building, las pasa a `3. Reuniones/Raw/` y `3. Reuniones/Procesadas/` y reparte la información (Ingest). Las reuniones de otras líneas de Esade se registran como "descartada". **En Drive no mueve nada**: no hay carpeta de actas definida para este proyecto.

### Ingest (llega una fuente nueva: transcripción, hilo de Basecamp, correo, documento)
1. Léela entera.
2. Si es una reunión, guarda el texto original en `3. Reuniones/Raw/AAAA-MM-DD - Tema (transcripción).md` (si no estaba ya) y el acta en `3. Reuniones/Procesadas/AAAA-MM-DD - Tema.md`, con una línea final `Transcripción: [[AAAA-MM-DD - Tema (transcripción)]]`: asistentes, contexto, decisiones, próximos pasos y temas abiertos.
3. Actualiza **cada nota afectada**:
   - **Reglas y convenciones** → `2. Acuerdos/Acuerdos - Esade Beyond`.
   - **Propuestas, aprobaciones, descartes y aplazamientos** (también medios descartados) → `Propuestas y decisiones - Esade Beyond`, siempre con el porqué.
   - **Resultados e hitos** (medios publicados, KPIs de cierre de mes) → `Cronología - Esade Beyond` y, si cambia algo importante, la Ficha.
   - **Temas de una línea** → su sección en `Líneas de trabajo - Esade Beyond`.
   - **Personas** → `Personas - Esade Beyond`. **Documentos nuevos** → `Documentos - Esade Beyond`.
   - **Tareas** → `Claude/Datos/Pendientes - Esade Beyond.md`. Fuente: enlace al to-do o hilo de Basecamp, al correo (enlace de Gmail) o al documento de Drive (+ `· acta: [[…]]`). **Basecamp no se copia a Raw**: se consulta en directo.
   - **Avance de la estrategia** → `Claude/Datos/Estrategia 26-27 - seguimiento Esade Beyond.md` (estado de la casilla y `[motivo:: …]`).
   - **Medios del mes** → línea `[medios:: AAAA-MM]` de `4. Seguimiento/Facturación y fee - Esade Beyond` (comprometido y notas), leyendo el Sheet de link building.
4. **Contradicciones**: no sobrescribir. Marca "⚠️ en revisión" con las dos versiones, su fuente y su fecha, y avisa a Nina.
5. Registra la entrada en `Claude/Log - Esade Beyond.md`.

### Pendientes: status y quién tiene la pelota
- Arriba va la sección **"## Status (DD/MM/AAAA)"**, que reescribe la tarea diaria. Es un resumen, no una alerta:
  - 💶 **Presupuesto y medios**: pedido pendiente, facturación del mes, medios comprometidos frente al ritmo del curso.
  - 🕒 **Horas**: consumo del último mes frente a lo presupuestado; mes anterior sin volcar a partir del día 5.
  - 🟧 lo que está **esperando al cliente más de 7 días** (con los días);
  - 🟦 lo **nuestro vencido o que vence en ≤2 días laborables**, y medios aprobados que llevan más de 21 días sin publicar;
  - 💬 **mensajes de Astrid, Helen o Sergi sin respuesta de RR después de 48 h laborables**.
- **🟦 Runroom**: campos Línea, Entrega, Responsable (Olga, Fer o Nina), Info, Fuente. `[ ]` backlog y `[/]` en curso. Claude puede pasar de `[ ]` a `[/]` con evidencia, pero nunca a `[x]`.
- **🟧 Cliente**: campos Esperando desde, Info, Fuente. Aquí van Astrid, Helen, Sergi, Comunicación, Eleven, Vansters y los medios que dependen de Esade.
- **Línea**: `- **Línea:** Contenidos | Link building | Gestión` (el panel agrupa el tablero por línea).
- **Enlace de referencia obligatorio** en la línea `Fuente:` de cada tarea: `[Basecamp: <título>](url)`, `[📧 "<asunto>" (<remitente>, DD/MM)](enlace de Gmail)`, `[Sheet: …](url)` o `[Acta …](url)`.
- **🔍 Por verificar**: pendientes antiguos que quizá ya están cerrados. El panel no los lee.
- **Nunca marques `[x]` ni borres**: eso lo hace Nina. Si una tarea tiene novedades, añade debajo "- **Actualización DD/MM:** …".

### Query
Contesto a partir de la wiki, citando las notas. Si la pregunta toca datos actuales (medios, presupuesto, KPIs, horas), consulto en vivo los documentos de `Documentos - Esade Beyond`. Si no puedo, lo digo.

### Lint
Busco contradicciones, datos desactualizados, pendientes que parezcan resueltos (los señalo, no los marco), enlaces rotos y huecos.

## Paneles de seguimiento (4. Seguimiento)
Tres notas con un bloque `dataviewjs` cada una (plugin Dataview). **Nunca se edita su código ni se les añaden propiedades**: los datos viven en otras notas o en las listas del final de cada panel.

| Panel | De dónde lee | Qué mantiene Claude |
|---|---|---|
| **Tareas - Esade Beyond** | `Claude/Datos/Pendientes - Esade Beyond.md` y `Claude/Datos/Estrategia 26-27 - seguimiento Esade Beyond.md` | Las tareas. Estrategia: `[x]` `[/]` `[ ]` `[?]` `[-]`, `[pelota:: cliente\|runroom]`, `[motivo:: …]`, `[basecamp:: …]`, `[fuente:: …]`, `[plan:: …] [inicio:: AAAA-MM] [fin:: AAAA-MM]`, `[nuevo:: sí]`. Las secciones de la estrategia con "Link" en el nombre van a la línea Link building |
| **Horas - Esade Beyond** | Lista "Registro mensual" de la propia nota (`[mes:: AAAA-MM] [agencia:: h] [kam:: h] [total:: h] [actualizado:: …] [notas:: …]`) y `horas_plan`, `remanente_inicial`, `curso_inicio`, `paprika_codigos`, `variacion_max_pct` de Datos panel | A cierre de mes (desde el día 5): la línea del mes con las horas de la Bolsa de horas (pestaña ESADE, filas "SEO blogging (beyond)"). Actualiza `remanente_horas` y `remanente_mes` |
| **Facturación y fee - Esade Beyond** | Lista "Pedidos y facturas 26/27" (`- [ ] … [mes::] [hasta::] [importe::] [oc::]`), lista "Compra de medios por mes" (`[medios:: AAAA-MM] [plan::] [facturado::] [consumido::] [notas::]`) y `presupuesto_curso`, `precio_hora`, `medios_*`, `facturacion_*` de Datos panel | OC e importes cuando se conozcan; cada mes, el comprometido de medios desde el Sheet. Nina marca la casilla de las facturas |

**Propiedades de `Claude/Datos panel - Esade Beyond.md`**: `actualizado`, `alertas_hoy`, `curso_inicio`, `paprika_codigos`, `horas_plan`, `remanente_inicial`, `remanente_horas`, `remanente_mes`, `precio_hora`, `precio_hora_nota`, `variacion_max_pct`, `umbral_cliente_dias`, `presupuesto_curso`, `presupuesto_nota`, `medios_presupuesto`, `medios_remanente_ly`, `medios_meses`, `medios_nota`, `facturacion_revision`, `facturacion_cuadra`, `facturacion_periodo`, `facturacion_nota`. Edítalas con un script read-modify-write.

## Alertas
Para esta cuenta, las alertas van **en el Status del Pendientes y en `alertas_hoy` de Datos panel**, no por email. Si una tarea programada avisa, lo hace con una notificación push.

| Tipo | Regla |
|---|---|
| 💶 **Medios** | Lo comprometido se desvía más de 10 puntos del ritmo del curso (% de meses cerrados), o un mes compromete más de un 30 % por encima de su presupuesto |
| 📰 **Medio parado** | Un medio aprobado lleva más de 21 días sin publicar |
| 🕒 **Horas** | Un mes consume más de un ±20 % de lo presupuestado (umbral provisional), o se acerca el one-shot del mes (toxicidad, estudio de la competencia) sin empezar |
| 📅 **Cierre sin volcar** | A partir del día 5, el mes anterior no tiene línea en el Registro mensual de Horas ni en Compra de medios |
| 🟧 **Pelota en el cliente** | Una tarea de 🟧 Cliente lleva más de `umbral_cliente_dias` (7) días esperando |
| 💬 **Sin respuesta** | Astrid, Helen o Sergi escribieron y RR no ha contestado en 48 h laborables |
| 📉 **SEO del blog** | *Pendiente de definir con Fer y Olga*: caída de impresiones o clics de /beyond/ en GSC, ratio de clics de Beyond a esade.edu por debajo del 0,7 %, dominios de referencia que bajan. De momento no se calculan |
