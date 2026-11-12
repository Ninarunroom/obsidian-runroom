# Instrucciones para Claude — Esade Do Better

Esto es lo que debo tener en cuenta (en chat o en las tareas programadas) antes de escribir o responder algo sobre **Do Better**, el blog de Esade. Es el **esquema** de la wiki: dice cómo está organizada la carpeta y cómo mantenerla. La ficha general de Esade (todas las líneas) es `Proyectos/Esade/Esade.md`.

## Alcance
- **Entra**: SEO, GEO, iteración de contenidos, contenido visual, analítica y reporting de **dobetter.esade.edu** (fee de 25 h/mes: Fer, Olga, Marta Baldó y Nina). Basecamp [Esade Dobetter - Analítica & SEO](https://basecamp.com/1771388/projects/19338495) y el correo de @esade.edu sobre Do Better (Dulce, Judith, Marta Barquier).
- **No entra**: el fee de SEO técnico y analítica de esade.edu (Sergi; tiene su KB en `Esade/SEO y Analítica/`), contenidos/Beyond y link building, OPENS y paid. Si aparecen, se mencionan solo como contexto y no van a este Pendientes.
- **Cómo distinguirlo**: si habla del blog, de dobetter.esade.edu, de Dulce, Judith o Marta Barquier, o del hilo de Basecamp 19338495, es Do Better. Si es Sergi, Helen o Natzir, es SEO y Analítica.

## Tono y estilo con el cliente
- Dulce escribe en castellano, formal y con preguntas de detalle (periodos, objetivos, de dónde sale cada dato). Quiere respuestas concretas y con datos, y a menudo con prisa.
- Marta Barquier es cercana y rápida validando.
- Si Nina redacta para ellas, castellano y tono cordial; respeta su forma de escribir (edición ligera).

## Cosas que nunca debo hacer o decir
- No imputar a este fee ni mezclar en sus pendientes nada del fee de SEO y analítica de Sergi, ni al revés.
- No proponer tocar artículos firmados por profesores, ni nada que necesite a TIC este curso.
- No confundir a **Marta Barquier** (Esade, redacción) con **Marta Baldó** (nuestra analista).
- No hablar con el cliente de la OC de la agencia (12.720 €, 53 €/h): es un coste interno.
- No comprometer horas, precio ni alcance ante el cliente sin que Nina lo valide.
- No guardar datos personales de lectores ni suscriptores de la newsletter.

## Aprobaciones necesarias antes de actuar
- Cualquier trabajo fuera de las cinco líneas del curso (p. ej., el análisis de suscriptores que pidió Dulce): lo estima y lo valida Nina.

## Otros
- "Judith Magran" en el acta del 04/09 es Judith Mangrane.
- En la Bolsa de horas, solo cuentan las filas con proyecto "SEO&Analítica Do Better". Marta Baldó a veces pone la OC012692 en filas del fee de SEO: eso no es de Do Better.

---

## Estructura de la carpeta (patrón LLM Wiki de Karpathy)

Ruta: `Proyectos/Esade/Do Better/`. Las carpetas están numeradas en orden de lectura. La nota de entrada es `1. Conocer la cuenta/00 Ficha de cliente - Esade Do Better.md`. Todo lo que es "de Claude" vive en `Claude/`.

```
Do Better/
├── 1. Conocer la cuenta/   00 Ficha de cliente - Esade Do Better (puerta de entrada), Roadmap 26-27, Líneas de trabajo,
│                           Propuestas y decisiones, Cronología, Personas, Documentos (todas con sufijo "- Esade Do Better")
├── 2. Acuerdos/            Acuerdos - Esade Do Better
├── 3. Reuniones/
│   ├── Raw/                transcripciones, NUNCA se modifican ("AAAA-MM-DD - Tema (transcripción).md"); Nina también deja aquí las suyas
│   └── Procesadas/         actas resumidas ("AAAA-MM-DD - Tema.md"), con enlace a su transcripción
├── 4. Seguimiento/        3 paneles dataviewjs: Tareas, Horas, Facturación y fee (- Esade Do Better)
└── Claude/                 de Claude: Datos/ (Pendientes, Estrategia 26-27 - seguimiento, Actas procesadas),
                            Instrucciones, Log, Datos panel (- Esade Do Better), Fuentes/ (copias de Sheets), Scripts/
```

## Operaciones

### Actas de reunión (tarea programada "Esade Do Better - Actas de reunión")
Las notas de Gemini se guardan solas en el Drive de Nina. La tarea las busca cada tarde, mira en `Claude/Datos/Actas procesadas - Esade Do Better.md` si ya están y, si son de Do Better, las pasa a `3. Reuniones/Raw/` y `3. Reuniones/Procesadas/` y reparte la información (Ingest). Las reuniones de otras líneas de Esade se registran como "descartada". **En Drive no mueve nada**: no hay carpeta de actas definida para este proyecto.

### Ingest (llega una fuente nueva: transcripción, hilo de Basecamp, correo, documento)
1. Léela entera.
2. Si es una reunión, guarda el texto original en `3. Reuniones/Raw/AAAA-MM-DD - Tema (transcripción).md` (si no estaba ya) y el acta en `3. Reuniones/Procesadas/AAAA-MM-DD - Tema.md`, con una línea final `Transcripción: [[AAAA-MM-DD - Tema (transcripción)]]`: asistentes, contexto, decisiones, próximos pasos y temas abiertos.
3. Actualiza **cada nota afectada**:
   - **Reglas y convenciones** → `2. Acuerdos/Acuerdos - Esade Do Better`.
   - **Propuestas, aprobaciones, descartes y aplazamientos** → `Propuestas y decisiones - Esade Do Better`, siempre con el porqué.
   - **Resultados e hitos** → `Cronología - Esade Do Better` y, si cambia algo importante, la sección que toque de la Ficha.
   - **Temas de una línea** (iteración, tendencias, SEO técnico, GEO, analítica…) → su sección en `Líneas de trabajo - Esade Do Better`.
   - **Personas** → `Personas - Esade Do Better`. **Documentos nuevos** → `Documentos - Esade Do Better`.
   - **Tareas** → `Claude/Datos/Pendientes - Esade Do Better.md`. Si salen de una reunión, la Fuente lleva el enlace al documento de Drive y `· acta: [[AAAA-MM-DD - Tema]]`. Si salen de Basecamp, el enlace al hilo. Si salen del correo, el asunto, el remitente, la fecha y "(email)". **Basecamp no se copia a Raw**: se consulta en directo.
   - **Avance de la estrategia** → `Claude/Datos/Estrategia 26-27 - seguimiento Esade Do Better.md` (cambia el estado de la casilla y el `[motivo:: …]`).
4. **Contradicciones**: no sobrescribir. Marca "⚠️ en revisión" con las dos versiones, su fuente y su fecha, y avisa a Nina.
5. Registra la entrada en `Claude/Log - Esade Do Better.md`.

### Pendientes: status y quién tiene la pelota
- Arriba va la sección **"## Status (DD/MM/AAAA)"**, que reescribe la tarea diaria. Es un resumen, no una alerta:
  - 🕒 **Horas**: remanente a cierre del último mes registrado, si se desvía más de un ±20 % de un mes; si el mes anterior sigue sin volcar a partir del día 5; y si Sergi ha preguntado por horas sin respuesta.
  - 🟧 lo que está **esperando al cliente o a terceros más de 7 días** (con los días);
  - 🟦 lo **nuestro vencido o que vence en ≤2 días laborables**;
  - 💬 los **mensajes de Sergi, Helen o Natzir sin respuesta de RR después de 48 h laborables** (Basecamp o correo).
- **🟦 Runroom**: campos Entrega, Responsable (Fer, Marta o Nina), Info, Fuente. Estado con la casilla: `[ ]` backlog (sin empezar) y `[/]` en curso. Claude puede pasar una tarea de `[ ]` a `[/]` cuando haya evidencia de que RR ya ha empezado (correo, Basecamp, horas imputadas), pero nunca a `[x]`. El panel de Tareas las pinta como tablero de tres columnas (Backlog · Esperando al cliente · En curso) con Hecho plegado debajo.
- **🟧 Cliente (esperando a Esade o a terceros)**: campos Esperando desde, Info, Fuente. Aquí van también OneTrust, Unibuddy, TIC (Jira) y Natzir.
- **Línea**: cada tarea lleva `- **Línea:** SEO técnico | Analítica | Gestión` (Fer, Marta y Nina; el panel agrupa el tablero por línea). **El tablero de trabajo es el de Obsidian; Kanbanize no se usa** (decisión de Nina, 12/11/2026: la agencia SEO ya no usa su tablero). Por eso el contexto completo va en la propia tarea (Info y Actualizaciones), que se despliega con "Ver contexto" en cada tarjeta.
- **Enlace de referencia obligatorio**: la línea `Fuente:` de cada tarea lleva siempre al menos un enlace clicable al origen, con formato markdown: `[Basecamp: <título del hilo>](url)`, `[📧 "<asunto del email>" (<remitente>, DD/MM)](enlace de Gmail del hilo: https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:<id>)`, `[Sheet: …](url)` o `[Acta …](url de Drive)`. Nada de "(email)" sin enlace. En la estrategia, cada tarea lleva `[basecamp:: url]` o `[fuente:: url]`. El panel muestra estos enlaces en cada tarjeta y avisa con "⚠️ sin enlace de referencia" si falta.
- **🔍 Por verificar**: pendientes antiguos que quizá ya están cerrados. El panel no los lee.
- **Nunca marques `[x]` ni borres**: eso lo hace Nina. Si una tarea tiene novedades, añade debajo "- **Actualización DD/MM:** …".

### Query
Contesto a partir de la wiki, citando las notas. Si la pregunta toca datos actuales (horas, remanente, KPIs), consulto en vivo los documentos de `Documentos - Esade Do Better`. Si no puedo, lo digo.

### Lint
Busco contradicciones, datos desactualizados, pendientes que parezcan resueltos (los señalo, no los marco), enlaces rotos y huecos.

## Paneles de seguimiento (4. Seguimiento)
Tres notas con un bloque `dataviewjs` cada una (plugin Dataview). **Nunca se edita su código ni se les añaden propiedades**: los datos viven en otras notas.

| Panel | De dónde lee | Qué mantiene Claude |
|---|---|---|
| **Tareas - Esade Do Better** | `Claude/Datos/Pendientes - Esade Do Better.md` (Status + 🟦 Runroom / 🟧 Cliente) y `Claude/Datos/Estrategia 26-27 - seguimiento Esade Do Better.md` | Las tareas. Estrategia: `[x]` hecho, `[/]` a medias, `[ ]` pendiente, `[?]` sin confirmar, `[-]` descartado, `[pelota:: cliente\|runroom]`, `[linea:: …]`, `[motivo:: …]`, `[basecamp:: enlace]`, `[fuente:: enlace]`, `[nuevo:: sí]` |
| **Horas - Esade Do Better** | Lista "Registro mensual" de la propia nota (`[mes:: AAAA-MM] [agencia:: h] [kam:: h] [actualizado:: AAAA-MM-DD] [notas:: …]`) y `horas_plan`, `remanente_inicial`, `curso_inicio`, `paprika_codigos`, `variacion_max_pct` de Datos panel | A cierre de mes (a partir del día 5): la línea del mes, con las horas de la agencia (Bolsa de horas, solo filas "SEO&Analítica Do Better") y las de Nina (Paprika ESA010245). Actualiza también `remanente_horas` y `remanente_mes` |
| **Facturación y fee - Esade Do Better** | Lista "Facturas 26/27" de la propia nota y `precio_hora`, `facturacion_*`, `coste_agencia_*` de Datos panel | La factura del curso ya está emitida. Calcula el coste de la agencia con sus horas × 53 €/h y el margen |

**Propiedades de `Claude/Datos panel - Esade Do Better.md`**: `actualizado`, `alertas_hoy`, `curso_inicio`, `paprika_codigos` (en agosto, si falta el del curso siguiente, recuérdaselo a Nina), `horas_plan` (25 h/mes: 20 agencia + 5 Nina, reparto deducido), `remanente_inicial` (0), `remanente_horas`, `remanente_mes`, `precio_hora`, `precio_hora_nota`, `variacion_max_pct`, `umbral_cliente_dias`, `facturacion_*`, `coste_agencia_oc`, `coste_agencia_importe`, `coste_agencia_precio_hora`. Edítalas con un script read-modify-write.

## Tareas recurrentes (las crea la tarea diaria en 🟦 Runroom si no existen)
- **Tendencias de búsqueda**: una por semana (Fer). Si en el hilo de Tendencias no hay mensaje de Runroom en 7 días, sale en el Status.
- **Informe mensual**: el primer día laborable de cada mes, "Informe de <mes anterior>: enviar y ofrecer presentarlo" (Fer y Nina).
- **Iteración de contenidos**: el primer día laborable de cada mes, "Optimizaciones de <mes>" (Olga), con el estado de cada URL según el Sheet de briefings.
- **Cierre de horas**: el día 5 de cada mes (Nina).

## Alertas
> [!warning] Propuesta pendiente del OK de Nina (12/11/2026)
> Funcionan en el Status del Pendientes y en `alertas_hoy` de Datos panel. Si una tarea programada avisa, lo hace con una notificación push, sin email.

| Tipo | Regla |
|---|---|
| 🕒 **Horas** | Agencia + Nina consumen más de un +20 % o menos de un −20 % de las 25 h de un mes, o el remanente acumulado pasa de ±5 h (20 % de un mes) |
| 📅 **Cierre sin volcar** | A partir del día 5, el mes anterior no tiene las horas de la agencia y las de Nina en el Registro mensual |
| 🔎 **Tendencias** | Más de 7 días sin un envío de Runroom en el hilo de Tendencias de búsqueda |
| 📄 **Informe** | A día 7 del mes, el informe del mes anterior no está en el hilo de Informes mensuales |
| ✍️ **Iteración** | A día 20 del mes, las temáticas del mes no están validadas en el Sheet, o hay URLs en "Esade OK" de meses anteriores sin publicar |
| 🟧 **Pelota en el cliente** | Una tarea de 🟧 Cliente lleva más de `umbral_cliente_dias` (7) días esperando |
| 💬 **Sin respuesta** | Dulce, Judith o Marta Barquier escribieron y RR no ha contestado en 48 h laborables |
| 📉 **SEO y GEO** | *Por definir con Fer*: caída de clics o impresiones en GSC, KPIs del informe por debajo del ritmo para los objetivos 26/27. De momento no se calculan |
