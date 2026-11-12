# Instrucciones para Claude — Esade SEO y Analítica

Esto es lo que debo tener en cuenta (en chat o en las tareas programadas) antes de escribir o responder algo sobre el fee de SEO y analítica de Esade. Es el **esquema** de la wiki: dice cómo está organizada la carpeta y cómo mantenerla. La ficha general de Esade (todas las líneas) es `Proyectos/Esade/Esade.md`, con sus propias Instrucciones en `Proyectos/Esade/Claude/`.

## Alcance
- **Entra**: SEO técnico (Fer) y analítica (Marta) del fee de 50 h/mes, más la gestión de Nina. Basecamp [Esade SEO tècnic](https://basecamp.com/1771388/projects/19742261) y [Esade - Analítica](https://basecamp.com/1771388/projects/16901662), y el correo de @esade.edu (y de Natzir) sobre estos temas.
- **No entra**: Do Better, contenidos/Beyond y link building (Olga), OPENS y paid (Ari, Adsmurai), Eulerian y Medición LLMs. Si aparecen, se mencionan solo como contexto y sus tareas no van aquí (van a `Proyectos/Esade/Pendientes - Esade.md`).

## Tono y estilo con el cliente
- Sergi escribe en **catalán** y es muy de datos; Helen escribe en castellano. Fer suele contestar en valenciano y Marta en catalán o castellano. Si Nina redacta para ellos, respeta el idioma del hilo.
- Sergi quiere respuestas rápidas y concretas, y que se le avise del impacto en horas antes de empezar. Valora la proactividad y que se le diga claramente qué es estacionalidad y qué no.

## Cosas que nunca debo hacer o decir
- No imputar a este fee ni mezclar en sus pendientes nada de Do Better, Beyond, link building u OPENS.
- No dar un dato de GA4 sin decir si está filtrado (bots de China, "ping robot") y con qué identidad (combinada u observada; desde el 10/11 GA4 modeliza sesiones).
- No comprometer horas, precio ni alcance ante el cliente sin que Nina lo valide.
- No guardar datos personales de leads ni de candidatos (exportaciones del CRM, formularios).

## Aprobaciones necesarias antes de actuar
- Cualquier estimación de horas o trabajo extra que se comunique a Sergi: la valida Nina.
- Cambios de accesos a GTM o GA4 (p. ej. dar acceso a Adsmurai): los decide Nina.

## Otros
- "Elena" (Basecamp, correo) y "Helen" son la **misma persona**: Elena Sánchez González.
- "Claudy" es como Sergi y Marta llaman a Claude en sus análisis.
- En la Bolsa de horas, Marta firma también como marta@agenciaseo.eu.

---

## Estructura de la carpeta (patrón LLM Wiki de Karpathy)

Ruta: `Proyectos/Esade/SEO y Analítica/`. Las carpetas están numeradas en orden de lectura. La nota de entrada es `1. Conocer la cuenta/00 Ficha de cliente - Esade SEO.md`. Todo lo que es "de Claude" vive en `Claude/`.

```
SEO y Analítica/
├── 1. Conocer la cuenta/   00 Ficha de cliente - Esade SEO (puerta de entrada), Propuestas y decisiones - Esade SEO,
│                           Cronología - Esade SEO, Personas - Esade SEO, Documentos - Esade SEO,
│                           Líneas de trabajo - Esade SEO (SEO técnico e IA, EMBA, Full Time MBA, analítica, dashboard)
├── 2. Acuerdos/            Acuerdos - Esade SEO
├── 3. Reuniones/
│   ├── Raw/                transcripciones, NUNCA se modifican ("AAAA-MM-DD - Tema (transcripción).md"); Nina también deja aquí las suyas
│   └── Procesadas/         actas resumidas ("AAAA-MM-DD - Tema.md"), con enlace a su transcripción
├── 4. Seguimiento/        3 paneles dataviewjs: Tareas - Esade SEO, Horas - Esade SEO, Facturación y fee - Esade SEO
└── Claude/                 de Claude: Datos/ (Pendientes - Esade SEO, Estrategia 26-27 - seguimiento Esade SEO,
                            Actas procesadas - Esade SEO), Instrucciones - Esade SEO, Log - Esade SEO,
                            Datos panel - Esade SEO, Fuentes/ (copias de Excel históricos), Scripts/
```

## Operaciones

### Actas de reunión (tarea programada "Esade SEO - Actas de reunión")
Las notas de Gemini se guardan solas en el Drive de Nina. La tarea las busca cada tarde, mira en `Claude/Datos/Actas procesadas - Esade SEO.md` si ya están y, si son de SEO o analítica, las pasa a `3. Reuniones/Raw/` y `3. Reuniones/Procesadas/` y reparte la información (Ingest). Las reuniones de otras líneas de Esade se registran como "descartada". **En Drive no mueve nada**: no hay carpeta de actas definida para este proyecto.

### Ingest (llega una fuente nueva: transcripción, hilo de Basecamp, correo, documento)
1. Léela entera.
2. Si es una reunión, guarda el texto original en `3. Reuniones/Raw/AAAA-MM-DD - Tema (transcripción).md` (si no estaba ya) y el acta en `3. Reuniones/Procesadas/AAAA-MM-DD - Tema.md`, con una línea final `Transcripción: [[AAAA-MM-DD - Tema (transcripción)]]`: asistentes, contexto, decisiones, próximos pasos y temas abiertos.
3. Actualiza **cada nota afectada**:
   - **Reglas y convenciones** → `2. Acuerdos/Acuerdos - Esade SEO`.
   - **Propuestas, aprobaciones, descartes y aplazamientos** → `Propuestas y decisiones - Esade SEO`, siempre con el porqué.
   - **Resultados e hitos** → `Cronología - Esade SEO` y, si cambia algo importante, la sección que toque de la Ficha.
   - **Temas de una línea** (EMBA, analítica, IA…) → su sección en `Líneas de trabajo - Esade SEO`.
   - **Personas** → `Personas - Esade SEO`. **Documentos nuevos** → `Documentos - Esade SEO`.
   - **Tareas** → `Claude/Datos/Pendientes - Esade SEO.md`. Si salen de una reunión, la Fuente lleva el enlace al documento de Drive y `· acta: [[AAAA-MM-DD - Tema]]`. Si salen de Basecamp, el enlace al hilo. Si salen del correo, el asunto, el remitente, la fecha y "(email)". **Basecamp no se copia a Raw**: se consulta en directo.
   - **Avance de la estrategia o del plan EMBA** → `Claude/Datos/Estrategia 26-27 - seguimiento Esade SEO.md` (cambia el estado de la casilla y el `[motivo:: …]`).
4. **Contradicciones**: no sobrescribir. Marca "⚠️ en revisión" con las dos versiones, su fuente y su fecha, y avisa a Nina.
5. Registra la entrada en `Claude/Log - Esade SEO.md`.

### Pendientes: status y quién tiene la pelota
- Arriba va la sección **"## Status (DD/MM/AAAA)"**, que reescribe la tarea diaria. Es un resumen, no una alerta:
  - 🕒 **Horas**: remanente a cierre del último mes registrado, si se desvía más de un ±20 % de un mes; si el mes anterior sigue sin volcar a partir del día 5; y si Sergi ha preguntado por horas sin respuesta.
  - 🟧 lo que está **esperando al cliente o a terceros más de 7 días** (con los días);
  - 🟦 lo **nuestro vencido o que vence en ≤2 días laborables**;
  - 💬 los **mensajes de Sergi, Helen o Natzir sin respuesta de RR después de 48 h laborables** (Basecamp o correo).
- **🟦 Runroom**: campos Entrega, Responsable (Fer, Marta o Nina), Info, Fuente.
- **🟧 Cliente (esperando a Esade o a terceros)**: campos Esperando desde, Info, Fuente. Aquí van también OneTrust, Unibuddy, TIC (Jira) y Natzir.
- **🔍 Por verificar**: pendientes antiguos que quizá ya están cerrados. El panel no los lee.
- **Nunca marques `[x]` ni borres**: eso lo hace Nina. Si una tarea tiene novedades, añade debajo "- **Actualización DD/MM:** …".

### Query
Contesto a partir de la wiki, citando las notas. Si la pregunta toca datos actuales (horas, remanente, KPIs), consulto en vivo los documentos de `Documentos - Esade SEO`. Si no puedo, lo digo.

### Lint
Busco contradicciones, datos desactualizados, pendientes que parezcan resueltos (los señalo, no los marco), enlaces rotos y huecos.

## Paneles de seguimiento (4. Seguimiento)
Tres notas con un bloque `dataviewjs` cada una (plugin Dataview). **Nunca se edita su código ni se les añaden propiedades**: los datos viven en otras notas.

| Panel | De dónde lee | Qué mantiene Claude |
|---|---|---|
| **Tareas - Esade SEO** | `Claude/Datos/Pendientes - Esade SEO.md` (Status + 🟦 Runroom / 🟧 Cliente) y `Claude/Datos/Estrategia 26-27 - seguimiento Esade SEO.md` | Las tareas. Estrategia: `[x]` hecho, `[/]` a medias, `[ ]` pendiente, `[?]` sin confirmar, `[-]` descartado, `[pelota:: cliente\|runroom]`, `[motivo:: …]`, `[basecamp:: enlace]`, `[nuevo:: sí]` |
| **Horas - Esade SEO** | Lista "Registro mensual" de la propia nota (`[mes:: AAAA-MM] [agencia:: h] [kam:: h] [total:: h] [actualizado:: AAAA-MM-DD] [notas:: …]`) y `horas_plan`, `remanente_inicial`, `curso_inicio`, `paprika_codigos`, `variacion_max_pct` de Datos panel | A cierre de mes (a partir del día 5): la línea del mes, con las horas de la agencia (Bolsa de horas, solo las filas "Fee SEO&Analítica") y las de Nina (Paprika o el Seguimiento del fee). `total` solo si no hay desglose. Actualiza también `remanente_horas` y `remanente_mes` de Datos panel |
| **Facturación y fee - Esade SEO** | Lista "Facturas 26/27" de la propia nota (`- [ ] Factura de <mes> [mes:: AAAA-MM] [oc:: …] [importe:: €]`) y `precio_hora`, `facturacion_*` de Datos panel | Añade la línea del mes cuando se conozcan la OC y el importe. Nina marca la casilla |

**Propiedades de `Claude/Datos panel - Esade SEO.md`**: `actualizado`, `alertas_hoy`, `curso_inicio`, `paprika_codigos` (por curso; en agosto, si falta el del curso siguiente, recuérdaselo a Nina), `horas_plan`, `remanente_inicial`, `remanente_horas`, `remanente_mes`, `precio_hora`, `precio_hora_nota`, `variacion_max_pct`, `umbral_cliente_dias`, `facturacion_revision`, `facturacion_cuadra`, `facturacion_nota`. Edítalas con un script read-modify-write.

## Alertas
Para esta cuenta, las alertas van **en el Status del Pendientes y en `alertas_hoy` de Datos panel**, no por email. Si una tarea programada avisa, lo hace con una notificación push.

| Tipo | Regla |
|---|---|
| 🕒 **Bolsa de horas** | El remanente se desvía más de un ±20 % de las horas de un mes, o un mes consume más de un ±20 % de lo vendido |
| 📅 **Cierre sin volcar** | A partir del día 5, el mes anterior no tiene línea completa en el Registro mensual |
| 🟧 **Pelota en el cliente** | Una tarea de 🟧 Cliente lleva más de `umbral_cliente_dias` (7) días esperando |
| 💬 **Sin respuesta** | Sergi, Helen o Natzir escribieron y RR no ha contestado en 48 h laborables (más grave si preguntan por horas) |
| 📉 **SEO y analítica** | *Pendiente de definir con Fer y Marta*: caídas de clics o impresiones en GSC, errores de indexación, conversiones de GA4 que dejan de dispararse, picos de bots. De momento no se calculan |
