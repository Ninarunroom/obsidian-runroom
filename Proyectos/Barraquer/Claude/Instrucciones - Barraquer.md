# Instrucciones para Claude — Barraquer

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente. Es el **esquema** de la wiki: dice cómo está organizada la carpeta y cómo mantenerla.

## Tono y estilo con el cliente
- El contacto principal, Cristian García Bufí, puede ser exigente en temas de precio y condiciones comerciales, y valora mucho la proactividad y la visión transversal (ha habido quejas por falta de ella en el servicio web). Pide soluciones, no preguntas, y cifras orientativas.
- Prefiere comunicación directa y resolutiva, por Basecamp (WhatsApp solo para avisar si urge). Escribe en castellano o catalán. En Dubái, Mohamed Akram Hanini prefiere emails breves a llamadas para dudas puntuales.

## Cosas que nunca debo hacer o decir
- No comprometerse ante el cliente sobre cambios de precio, modelo de fee o condiciones del servicio web o de mantenimiento sin validarlo antes internamente (negociación sensible abierta desde finales de 2025).
- No compartir con el cliente los márgenes internos de Runroom en la cuenta.
- No sugerir que Madrid acepta mutuas.
- No guardar leads ni datos de pacientes en archivos de Runroom.

## Aprobaciones necesarias antes de actuar
- Cualquier cambio en el modelo de fee, precios o condiciones comerciales: validar con Ari Iglesias o César Úbeda antes de comunicarlo a Cristian.
- Cambios de presupuesto en Madrid o en otros países fuera de lo acordado en las reuniones de planificación: validar con Ari Iglesias o Nina.

## Otros
- "Araceli Iglesias" (en las transcripciones) y "Ari Iglesias" (en Basecamp) son la **misma persona**.
- Equipo en transición: Magalí Federico salió en septiembre de 2026; Ari lleva el día a día de medios con Nina.
- El equipo web tiene su propia KB (GitHub `Runroom/BarraquerKB`, rama `vault`). Si algo de la web afecta a medición o landings, enlázalo y no lo dupliques.

---

## Estructura de la carpeta (patrón LLM Wiki de Karpathy)

Las carpetas están numeradas en orden de lectura. La nota de entrada es `1. Conocer la cuenta/00 Ficha de cliente - Barraquer.md`. Todo lo que es "de Claude" vive en `Claude/`.

```
Barraquer/
├── 1. Conocer la cuenta/   00 Ficha de cliente - Barraquer (puerta de entrada: cliente, qué hacemos, contactos, dinero, reglas clave, día a día),
│                           Propuestas y decisiones, Cronología, Personas, Documentos,
│                           Mercados y canales - Barraquer (una sección por mercado, Instituto, canales y medición)
├── 2. Acuerdos/            Acuerdos - Barraquer
├── 3. Reuniones/
│   ├── Raw/                transcripciones, NUNCA se modifican ("AAAA-MM-DD - Tema (transcripción).md"); Nina también deja aquí las suyas
│   └── Procesadas/         actas resumidas ("AAAA-MM-DD - Tema.md"), con enlace a su transcripción
├── 4. Seguimiento/        4 paneles dataviewjs: Tareas, Horas, Saldos, Facturación y fee (+ propuesta de alertas de campaña)
└── Claude/                 de Claude: Datos/ (Pendientes - Barraquer, Estrategia 2026 - seguimiento, Actas procesadas), Instrucciones, Log, Datos panel, Fuentes/Documentos (PDFs y exportaciones), copias de seguridad
```

## Operaciones

### Actas de reunión (tarea programada "Barraquer - Actas de reunión")
Las notas de Gemini de cada reunión se guardan solas en el Drive de Nina (carpetas de Meet, la unidad compartida "00. Actas reunión" o compartidas por Ari). Una tarea programada las busca cada tarde por título (`barraquer` + `Notas de Gemini`), mira en `Claude/Datos/Actas procesadas.md` si ya están, y si no: copia el texto a `3. Reuniones/Raw/`, escribe el acta en `3. Reuniones/Procesadas/`, reparte la información por el KB (Ingest, abajo) y apunta el ID en el registro. En Drive lo único que hace es **mover** las actas de Barraquer de Nina a «00. Actas reunión» (nunca las de otras personas, y nunca edita, renombra, borra ni comparte).

### Ingest (llega una fuente nueva: transcripción, hilo de Basecamp, correo, PDF)
1. Léela entera.
2. Si es una reunión, guarda el texto original en `3. Reuniones/Raw/AAAA-MM-DD - Tema (transcripción).md` (si no estaba ya) y el acta procesada en `3. Reuniones/Procesadas/AAAA-MM-DD - Tema.md`, con una línea final `Transcripción: [[AAAA-MM-DD - Tema (transcripción)]]`: contexto, decisiones, próximos pasos.
3. Actualiza **cada nota afectada**:
   - **Reglas y convenciones** → `2. Acuerdos/Acuerdos - Barraquer`.
   - **Propuestas, aprobaciones, descartes y aplazamientos** → `1. Conocer la cuenta/Propuestas y decisiones - Barraquer`, siempre con el porqué.
   - **Resultados e hitos** → `1. Conocer la cuenta/Cronología - Barraquer` y, si cambia algo importante del estado de la cuenta, la sección que toque de `1. Conocer la cuenta/00 Ficha de cliente - Barraquer.md` (Dinero, Contactos, Temas sensibles…).
   - **Temas de un mercado o canal** → su nota en `1. Conocer la cuenta/Mercados y canales - Barraquer.md (sección que toque)`.
   - **Personas** → `1. Conocer la cuenta/Personas - Barraquer`.
   - **Documentos nuevos (con enlace)** → `1. Conocer la cuenta/Documentos - Barraquer`.
   - **Tareas** → `Claude/Datos/Pendientes - Barraquer.md`. Si salen de una reunión, la línea Fuente lleva el enlace al documento de Drive y además `· acta: [[AAAA-MM-DD - Tema]]` (el acta procesada). Si salen de Basecamp, el enlace al hilo. **Basecamp no se copia a Raw**: es la fuente en bruto y se consulta en directo.
4. Si cambia algo de lo que resume la Ficha de cliente (contactos, dinero, reglas clave, día a día, temas sensibles), actualiza su sección. Las "Reglas clave" son un resumen de Acuerdos: no repitas ahí lo que ya está en otra sección de la ficha.
5. **Contradicciones**: no sobrescribir. Marca "⚠️ en revisión" con las dos versiones, su fuente y su fecha, y avisa a Nina.
6. Registra la entrada en `Claude/Log - Barraquer.md`.

### Pendientes: status y quién tiene la pelota
- Arriba del todo va la sección **"Status (DD/MM/AAAA)"**, que reescribe la tarea diaria. Es un resumen, no una alerta:
  - lo que está **esperando al cliente más de 7 días** (con los días);
  - lo **nuestro vencido o que vence en ≤2 días laborables**;
  - los **mensajes de Cristian sin contestar después de 48 h laborables**;
  - los **avisos de saldo sin confirmar la recarga**.
- **🟦 Runroom**: campos Entrega, Responsable, Info, Fuente.
- **🟧 Cliente**: campos Esperando desde, Info, Fuente.
- **Nunca marques `[x]` ni borres**: eso lo hace Nina. Si una tarea tiene novedades, añade debajo "- **Actualización DD/MM:** …".

### Query
Contesto a partir de la wiki, citando las notas. Si la pregunta toca datos actuales (inversión, saldos, resultados), consulto en vivo los documentos de `1. Conocer la cuenta/Documentos - Barraquer`. Si no puedo, lo digo.

### Lint
Busco contradicciones, datos desactualizados, pendientes que parezcan resueltos (los señalo, no los marco), enlaces rotos y huecos.

## Paneles de seguimiento (4. Seguimiento)
Cuatro notas con un bloque `dataviewjs` cada una (plugin Dataview). **Nunca se edita su código ni se les añaden propiedades**: los datos viven en otras notas.

| Panel | De dónde lee | Qué mantiene Claude |
|---|---|---|
| **Tareas - Barraquer** | `Claude/Datos/Pendientes - Barraquer.md` (Status + secciones 🟦 Runroom / 🟧 Cliente) y `Claude/Datos/Estrategia 2026 - seguimiento.md` | Las tareas, como siempre. Estrategia: `[x]` hecho, `[/]` a medias, `[ ]` pendiente, `[?]` sin confirmar, `[-]` descartado, `[pelota:: cliente\|runroom]`, `[motivo:: …]`, `[basecamp:: enlace]`, `[nuevo:: sí]`. El panel no repite una acción de la estrategia si su enlace ya aparece en una tarea de Pendientes |
| **Horas - Barraquer** | Lista "Registro mensual" de la propia nota (`[mes:: AAAA-MM] [head:: h] [kam:: h] [performance:: h] [otros:: h] [actualizado:: AAAA-MM-DD]`) y `horas_plan` de Datos panel (horas vendidas por perfil desde cada mes: hasta ago Head 2 / KAM 15 / Performance 37; desde sep Head-Ari 35 / KAM-Nina 19) | Cuando Nina pase una captura de la herramienta de horas, actualiza la línea del mes (y `actualizado`). `otros` = UX/UI, becario, etc. |
| **Saldos - Barraquer** | Lista "Recargas" de la propia nota y las propiedades `google_ads_*` y `umbral_alerta_*` de `Claude/Datos panel - Barraquer.md` | Cada día, las propiedades `google_ads_saldo_estimado`, `google_ads_ultima_recarga` (base de cálculo), `google_ads_gasto_diario`, `google_ads_fecha_datos` y `google_ads_nota`. **Clínica + Estética = un único saldo** |
| **Facturación y fee - Barraquer** | Lista "Facturas 2026" de la propia nota (`- [x] Factura de <mes> [mes:: AAAA-MM] [importe:: €]`) y las propiedades de facturación de Datos panel | Cuando Nina diga que ha facturado un mes, marca la casilla de ese mes. El primer día laborable a partir del día 5, la revisión de cierre (abajo) |

**Propiedades de `Claude/Datos panel - Barraquer.md`**: `actualizado`, `alertas_hoy`, `facturacion_revision`, `facturacion_cuadra`, `facturacion_nota`, `medios_aprobado`, `medios_previsto`, `fee_aprobado`, `fee_consumido`, `fee_facturado`, `tasa_aprobado`, `tasa_prevista`, `meses_reales`, `fee_consumido_mes`, `fee_facturado_mes`, `medios_mes`, `tasa_mes` (12 valores cada uno), `inversion_anual_prevista`, `fee_tramos`, `cuota_fee_mensual`, `horas_plan`, `paprika_codigos` (código de Paprika por año; cambia cada año: en diciembre, si falta el del año siguiente, recuérdaselo a Nina), `umbral_alerta_pct`, `umbral_alerta_dias`, `google_ads_*`. Edítalas con un script read-modify-write.

- **Cierre de mes** (el primer día laborable a partir del día 5): desde el Sheet `2026 - Presupuesto Barraquer` (`Check cierre`, `Presupuesto_Anual`, `Detalle_Mensual`) actualiza las propiedades de facturación, con `meses_reales` = meses cerrados con datos reales. `facturacion_cuadra: false` si alguna partida se desvía más de 100 € o si `Detalle_Mensual` no suma lo mismo que `Presupuesto_Anual`, y la explicación va en `facturacion_nota`. El panel compara el **facturado** (casillas marcadas) con el **invertido** (fee del 18 % sobre la inversión real de esos meses) y la inversión en medios con lo aprobado.
- **Lunes**: `inversion_anual_prevista` (escalado de fee); horas del mes en curso frente a lo previsto a la fecha de la última captura (alerta si un perfil va más de un 10 % por encima) y acumulado del año por perfil.
- **Cada día**: `actualizado` y `alertas_hoy`.

## Alertas (por email, solo si hay alguna)
Las alertas son **de campañas y de negocio**, no de status. Cada mañana la tarea diaria las calcula y, si hay al menos una, manda un email a nina@runroom.com con el asunto `Barraquer · Alertas DD/MM`. No se guardan en ninguna nota.

Fuente de datos: Sheet **"2026 - Presupuesto Barraquer"** (`1DwpGEDViOsgIxjQePCv2vf9ohf0TV5EfiTykFiQpu4U`):
- Pestañas de gasto que se actualizan solas: `GoogleAds_Spend`, `MetaAds_Spend`, `DV360_Spend` y `LinkedInAds_Spend` (MTD, ayer, semana pasada y mes pasado, por campaña).
- `Detalle_Mensual`: presupuesto por mes y por canal.
- `Presupuesto_Anual` y `Presupuesto_Anual_Instituto`: inversión anual aprobada y "Invertido + previsión".

| Tipo | Regla |
|---|---|
| 💶 **Pacing mensual** | Por canal (search, pmax, youtube, demand-gen, meta, dv360), y en total, se compara el gasto MTD con el presupuesto del mes en `Detalle_Mensual` × (días transcurridos / días del mes). Alerta si se desvía más de un **±15 %** y la diferencia supera los **300 €**. El canal se saca del nombre de la campaña (`google_<línea>_<canal>_…`, `meta_…`, `dv360_…`) |
| 📈 **Pico de gasto diario** (Google Ads: usa `Diario_Campañas` del Sheet diario; el resto de canales, solo si la foto de `*_Spend` es de ayer o de hoy) | Una campaña gasta ayer más del **150 %** de su media diaria de la semana pasada, con un mínimo de 50 € |
| ⛔ **Campaña parada** | Una campaña activa (ENABLED o ACTIVE; en Google Ads, según la pestaña `Campañas` del Sheet diario) gastó la semana pasada y ayer gastó 0 € (en Google Ads: no tiene fila de ayer en `Diario_Campañas`). Puede ser falta de saldo o un rechazo |
| 🪫 **Saldo bajo** | Lee `4. Seguimiento/Saldos - Barraquer.md` (lista "Recargas"; las cifras van en Datos panel). **Google Ads Clínica y Estética comparten saldo**: trátalas como una sola cuenta (`google-ads`) y suma su gasto. Por cada cuenta, el saldo estimado es el saldo de partida (última recarga + lo que quedara) menos el gasto de esa cuenta desde la fecha de la recarga, sacado de las pestañas `*_Spend` (MTD, semana y mes pasado; si no se puede aislar el periodo exacto, estímalo con la media diaria de la última semana). El gasto medio diario es el de la semana pasada. Alerta si el saldo estimado es menor que `umbral_alerta_pct` % de la última recarga o cubre menos de `umbral_alerta_dias` días laborables. Actualiza las propiedades `google_ads_*` de `Claude/Datos panel - Barraquer.md` (la nota de Saldos no tiene propiedades). Si Basecamp o un correo dicen que Cristian ha recargado o informa del saldo, añade una fila a "Recargas" (importe "?" si no lo dice) |
| 🧾 **Umbral de fee** | Se suma la inversión anual (clínica + estética "Invertido + previsión" + Instituto) y se compara con los tramos del escalado de fee (ver Acuerdos). Alerta si el total está a menos del **5 %** de un umbral, o si ha cruzado uno, hacia arriba o hacia abajo, respecto al tramo vigente (200-300k, 18 %). Hay que indicar el tramo y el % que corresponderían |
| 🕒 **Datos desactualizados** | Las pestañas de gasto **no se actualizan a diario** (a 05/11, la última foto era del 02/11 y LinkedIn del 23/10). Calcula el pacing con la fecha de la última foto (días transcurridos hasta esa fecha), indícala en el email, y avisa si tiene más de 7 días |
| 📉 **CTR / CR / CPL** (Google Ads) | Fuente: Sheet **"Barraquer - Google Ads diario"** (`1KGLV2nSbJ5-pVJaZWfvhq35Fe53iqMvVf3GLUjCtQ80`), que rellena cada noche un script de la MCC (`Claude/Scripts/barraquer-google-ads-diario.js`). Pestañas: `Diario_Campañas` (campaña × día desde el 1/1/2025), `Diario_Zonas` (campaña × país/región/provincia × día, últimos 90 días), `Mensual_Zonas` (campaña × zona × mes desde el 1/1/2025), `Campañas` (estado, tipo, presupuesto diario) e `Info` (última ejecución). Si la pestaña `Info` no existe todavía o la última ejecución tiene más de 2 días, no calcules estas alertas y dilo en el resumen (y en el email si ya había datos antes). Por campaña, compara **ayer** con la **media de los 7 días anteriores**: alerta si el **CTR cae más de un 25 %** (mín. 1.000 impresiones ayer), si el **CR cae más de un 25 %** (mín. 50 clics), o si el **CPL sube más de un 30 %** (mín. 3 conversiones en los 7 días). Indica campaña, valor de ayer, media y diferencia. *Umbrales provisionales, pendientes de validar con Ari* |
| 📊 **Resumen semanal** (lunes, Google Ads) | Va en el email de los lunes aunque no haya otras alertas. (1) **Semana pasada** (lun-dom) frente a la **semana anterior** y frente a la **misma semana del año pasado** (−52 semanas, mismos días de la semana): inversión, conversiones, CPL, CTR y CR, en total y por línea/canal (se saca del nombre de la campaña; no compares campaña a campaña con el año pasado porque los nombres cambian). (2) **Zonas**, con `Diario_Zonas` (semana pasada frente a las 4 anteriores) y `Mensual_Zonas` (mes en curso frente al mismo mes del año pasado), por país y región/provincia con al menos 30 € de inversión: las 3 zonas con mejor y peor CPL, y las que gastan sin convertir (≥100 € y 0 conversiones) |
| 📅 **Cierre de mes vs año pasado** (con la revisión de facturación del día 5) | Mes cerrado frente al mismo mes de 2025 y acumulado del año frente al mismo periodo de 2025: inversión, conversiones, CPL, CTR y CR, en total y por línea/canal. Se añade a `facturacion_nota` solo si hay algo relevante (CPL +15 % o conversiones −15 %) y siempre al email de ese día |

## Kanbanize (cards de tareas)
Lo leen las skills de preparación y de después de reunión (y es la misma lógica en Spradling e Hispano Suiza).
- **Reglas de Nina para las cards**: **nunca se pone responsable** en ninguna card. **Tipo de card siempre**. **Fecha** solo si aplica (fecha comprometida o de entrega). **Antes de crear o cambiar una card, Claude le dice a Nina cómo la va a crear y dónde, y espera su OK.**
- **Cards recurrentes de Presupuestos y Facturación**: las crea en Kanbanize la tarea programada "Kanbanize - Cards recurrentes performance" (lunes 8:47, columna Ready). **En Obsidian no se crean** (ni la semanal de Presupuesto ni la mensual de Facturación): en Pendientes solo van tareas pendientes nuestras o del cliente.
- **Tipos del tablero Sky**: 13 Landings · 15 Informes · 18 Propuestas · 22 Implementación analítica · 24 Lanzamiento de campaña · 25 Optimización de campañas · 26 Control presupuestario · 27 Implementación canal · 30 Proyecto · 57 Test a/b.
- **Tablero**: Sky (board_id 21), en `https://runroom.kanbanize.com`. Workflow **Performance** (80), carril **Transversal** (116). Código Paprika en el campo personalizado **field_id 9**.
- **Dónde entran**: columna **Backlog → Barraquer** (1682). Existe también **Backlog → Barraquer Dubai** (1677): solo para lo de Dubái.
- **Parent card**: [51536 · Barraquer campañas 2026](https://runroom.kanbanize.com/ctrl_board/21/cards/51536/details/)
- **Código Paprika**: **BAR020061 (2026) · BAR020066 (2027)** (los mismos que en `Datos panel - Barraquer`).
- **Formato de las cards de Barraquer**: título `Barraquer - <tarea>`, prioridad media, color verde (34a97b), etiqueta 62.
- **Basecamp para compartir actas**: Barraquer - SEM (17192035).
