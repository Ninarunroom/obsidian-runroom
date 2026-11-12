# Instrucciones para Claude — Spradling

Esto es lo que debo tener en cuenta (en chat o en las tareas programadas) antes de escribir o responder algo sobre este cliente. Es el **esquema** de la wiki: dice cómo está organizada la carpeta y cómo mantenerla.

## Tono y estilo con el cliente
- Relación cercana y de confianza con el equipo de Spradling Europe. Con Dèlia, tuteo y tono informal ("Hello!", bromas). Natalia es algo más formal ("Cordialmente").
- Los problemas técnicos o errores (bugs, bloqueos, plazos que no se van a cumplir) se cuentan de forma directa y transparente, sin rodeos.
- Con Colombia: por el Basecamp Spradling Internacional, con la hora de Colombia y la de España al proponer horarios.

## Cosas que nunca debo hacer o decir
- No comprometerse ante el cliente sobre precio, fee, horas extra o condiciones sin validarlo antes con Nina o Ari.
- No guardar listas de clientes ni datos personales de leads en archivos de Runroom: van en una carpeta propiedad de Spradling.
- No dar por buenos los datos de atribución del CRM (Sugar) mientras no esté el módulo UTM → CRM (16/11/2026): pueden inflar "directo".

## Aprobaciones necesarias antes de actuar
- Cualquier trabajo de GTM o CRM fuera del alcance estándar (por ejemplo, crear eventos o acciones de conversión en SugarCRM) se factura aparte: no asumirlo sin confirmar presupuesto u horas con Nina o Ari ([[2026-07-28 - Revision backlog]]).
- Cambios de presupuesto entre partidas o países fuera de lo acordado: validar con Nina o Ari, y apuntarlos en "Modificaciones presupuestarias" del Sheet.

## Otros
- Cuenta multipaís: Grupo 1 (Alemania, Reino Unido y Polonia) y Grupo 2 (España, Italia y Francia), 40/60 a favor del G2.
- Con el equipo de Colombia (desarrollo, Analytics y GTM) es difícil coordinarse directamente: casi todo pasa por Dèlia o por el Basecamp Internacional.
- Gemini transcribe "Runroom" como "Randroom", "Ranroom" o "Ranro", y "Spradling" como "Spradlin". "Araceli Iglesias" (en las transcripciones) y "Ari Iglesias" (en Basecamp) son la **misma persona**.
- **Dos proyectos de Basecamp**: [Spradling Europa](https://basecamp.com/1771388/projects/19500347) (19500347; España + Runroom: presupuestos, informes y campañas) y [Spradling Internacional](https://basecamp.com/1771388/projects/20351671) (20351671; con Colombia desde el 21/10/2026: tracking, GA4/GTM, reuniones e informes). Hay que leer los dos.
- Dominio de email del cliente: **spradling.group** (Natalia aparece también como n.cortes@spradling.eu en Basecamp).

---

## Estructura de la carpeta (patrón LLM Wiki de Karpathy)

Las carpetas están numeradas en orden de lectura. La nota de entrada es `1. Conocer la cuenta/00 Ficha de cliente - Spradling.md`. Todo lo que es "de Claude" vive en `Claude/`.

```
Spradling/
├── 1. Conocer la cuenta/   00 Ficha de cliente - Spradling (puerta de entrada: cliente, qué hacemos, contactos, dinero, reglas clave, día a día),
│                           Propuestas y decisiones, Cronología, Personas, Documentos,
│                           Mercados y canales - Spradling (grupos de países, canales, lanzamientos de producto, medición y CRM)
├── 2. Acuerdos/            Acuerdos - Spradling
├── 3. Reuniones/
│   ├── Raw/                transcripciones, NUNCA se modifican ("AAAA-MM-DD - Tema (transcripción).md"); Nina también deja aquí las suyas
│   └── Procesadas/         actas resumidas ("AAAA-MM-DD - Tema.md"), con enlace a su transcripción
├── 4. Seguimiento/         3 paneles dataviewjs: Tareas, Horas, Facturación y fee (sin Saldos: Runroom paga los medios)
└── Claude/                 de Claude: Datos/ (Pendientes - Spradling, Estrategia 2026 - Spradling, Actas procesadas - Spradling),
                            Instrucciones, Log - Spradling, Datos panel - Spradling, Fuentes/ (PDFs y exportaciones), Scripts/ (script de Google Ads), copias de seguridad
```

`Claude/_estructura-anterior/` guarda las notas de antes de la reestructuración del 06/11/2026 (Spradling.md y las actas antiguas). Solo es histórico: no se actualiza.

## Operaciones

### Actas de reunión (tarea programada "Spradling - Actas de reunión")
Las notas de Gemini de cada reunión se guardan solas en el Drive de Nina ("Meet Recordings"), en la carpeta de actas del cliente o en documentos que comparte Ari. Una tarea programada las busca cada tarde por título (`spradling` + `Notas de Gemini`) y en la carpeta **03. Actas** (`1Zr_cZ08Im-NHo471bTyRlwHQzIKWjUdM`). Mira en `Claude/Datos/Actas procesadas - Spradling.md` si ya están y, si no: copia el texto a `3. Reuniones/Raw/`, escribe el acta en `3. Reuniones/Procesadas/`, reparte la información por el KB (Ingest, abajo) y apunta el ID en el registro. En Drive lo único que hace es **mover** las actas de Spradling que son de Nina a «03. Actas» (nunca las de otras personas, y nunca edita, renombra, borra ni comparte).

### Ingest (llega una fuente nueva: transcripción, hilo de Basecamp, correo, PDF)
1. Léela entera.
2. Si es una reunión, guarda el texto original en `3. Reuniones/Raw/AAAA-MM-DD - Tema (transcripción).md` (si no estaba ya) y el acta procesada en `3. Reuniones/Procesadas/AAAA-MM-DD - Tema.md`, con una línea final `Transcripción: [[AAAA-MM-DD - Tema (transcripción)]]`: contexto, decisiones, próximos pasos y temas abiertos.
3. Actualiza **cada nota afectada**:
   - **Reglas y convenciones** → `2. Acuerdos/Acuerdos - Spradling`.
   - **Propuestas, aprobaciones, descartes y aplazamientos** → `1. Conocer la cuenta/Propuestas y decisiones - Spradling`, siempre con el porqué.
   - **Resultados e hitos** → `1. Conocer la cuenta/Cronología - Spradling` y, si cambia algo importante del estado de la cuenta, la sección que toque de `00 Ficha de cliente - Spradling` (Dinero, Contactos, Temas sensibles…).
   - **Países, canales, lanzamientos, medición y CRM** → la sección que toque de `1. Conocer la cuenta/Mercados y canales - Spradling`.
   - **Personas** → `1. Conocer la cuenta/Personas - Spradling`.
   - **Documentos nuevos (con enlace)** → `1. Conocer la cuenta/Documentos - Spradling`.
   - **Avances de la estrategia** → `Claude/Datos/Estrategia 2026 - Spradling.md` (cambia el estado de la casilla y el `motivo`, con evidencia).
   - **Tareas** → `Claude/Datos/Pendientes - Spradling.md`. Si salen de una reunión, la línea Fuente lleva el enlace al documento de Drive y además `· acta: [[AAAA-MM-DD - Tema]]` (el acta procesada). Si salen de Basecamp, el enlace al hilo. **Basecamp no se copia a Raw**: es la fuente en bruto y se consulta en directo.
4. Si cambia algo de lo que resume la Ficha de cliente (contactos, dinero, reglas clave, día a día, temas sensibles), actualiza su sección. Las "Reglas clave" son un resumen de Acuerdos: no repitas ahí lo que ya está en otra sección de la ficha.
5. **Contradicciones**: no sobrescribir. Marca "⚠️ en revisión" con las dos versiones, su fuente y su fecha, y avisa a Nina.
6. Registra la entrada en `Claude/Log - Spradling.md`.

### Pendientes: status y quién tiene la pelota
- Arriba del todo va la sección **"Status (DD/MM/AAAA)"**, que reescribe la tarea diaria. Es un resumen, no una alerta:
  - lo que está **esperando al cliente más de 7 días** (con los días);
  - lo **nuestro vencido o que vence en ≤2 días laborables**;
  - los **mensajes de Natalia o Dèlia sin contestar después de 48 h laborables** (en los dos Basecamp);
  - el **remanente o los cambios de presupuesto pedidos** que aún no estén reflejados en el Sheet.
- **🟦 Runroom**: campos Entrega, Responsable, Info, Fuente.
- **🟧 Cliente**: campos Esperando desde, Info, Fuente.
- **Qué entra** (nada de paja): solo tareas concretas, con dueño y una fuente que se pueda abrir. No entran "confirmar si…" genéricos, próximos pasos "de grupo" sin fecha ni responsable, cards automáticas que nadie ha pedido, ni cosas que dependen de otro equipo del cliente y no nos tocan (p. ej. el GTM, que es de Colombia).
- **Cerrar tareas lo hace Claude, no Nina** (Nina no marca casillas). Se cierra cuando: Nina lo dice en el chat ("hecho", "sobra", "quítalo"), o Basecamp/correo lo dejan claro (el cliente ha contestado lo que esperábamos, Runroom ya ha enviado lo suyo, el material ha llegado). `[x]` si está hecha, `[-]` si ya no aplica, y una línea en el Log con el motivo y el enlace. Si hay duda, no se cierra: se pone en el Status como "¿cerrar? …" para que Nina lo diga. Si una tarea tiene novedades sin cerrarse, añade debajo "- **Actualización DD/MM:** …".
- **Estrategia ≠ reuniones**: en `Estrategia 2026 - Spradling` solo va lo que está en la propuesta de estrategia (PDF del 19/12/2025 y revisión del 18/05/2026). Lo que sale de una reunión o de Basecamp va a Pendientes (si está abierto) o a Propuestas y decisiones (si es una decisión), nunca a la estrategia.
- **Lo de estrategia lleva fuente**: cada acción de `Estrategia 2026 - Spradling` y cada fila de `Propuestas y decisiones` dice de dónde sale (`[fuente:: …]`: PDF de la propuesta, acta o hilo). Sin fuente no se pone como "acordado".

### Query
Contesto a partir de la wiki, citando las notas. Si la pregunta toca datos actuales (inversión, facturación, resultados), consulto en vivo los documentos de `1. Conocer la cuenta/Documentos - Spradling`. Si no puedo, lo digo.

### Lint
Busco contradicciones, datos desactualizados, pendientes que parezcan resueltos (los señalo, no los marco), enlaces rotos y huecos.

## Paneles de seguimiento (4. Seguimiento)
Tres notas con un bloque `dataviewjs` cada una (plugin Dataview). **Nunca se edita su código ni se les añaden propiedades**: los datos viven en otras notas.

| Panel | De dónde lee | Qué mantiene Claude |
|---|---|---|
| **Tareas - Spradling** | `Claude/Datos/Pendientes - Spradling.md` (Status + secciones 🟦 Runroom / 🟧 Cliente) y `Claude/Datos/Estrategia 2026 - Spradling.md` | Las tareas, como siempre. Estrategia: `[x]` hecho, `[/]` a medias, `[ ]` pendiente, `[?]` sin confirmar, `[-]` descartado, `[pelota:: cliente\|runroom]`, `[motivo:: …]`, `[basecamp:: enlace]`, `[nuevo:: sí]`, `[fuente:: propuesta, acta o hilo]` (obligatorio). El panel no repite una acción de la estrategia si su enlace ya aparece en una tarea de Pendientes |
| **Horas - Spradling** | Lista "Registro mensual" de la propia nota (`[mes:: AAAA-MM] [head:: h] [kam:: h] [performance:: h] [otros:: h] [actualizado:: AAAA-MM-DD]`) y `horas_plan` de Datos panel (horas vendidas por perfil desde cada mes: hasta agosto Head 1 / KAM 7,31 / Performance 17,43; desde septiembre Head-Ari 16 / KAM-Nina 9) | Cuando Nina pase una captura de la herramienta de horas, actualiza la línea del mes (y `actualizado`). En la captura, "KAMPO" = kam, "Performance M…" = performance y "z_Becario" = otros |
| **Facturación y fee - Spradling** | Lista "Facturas 2026" de la propia nota (`- [x] Factura de <mes> [mes:: AAAA-MM] [importe:: fee facturado] [medios:: €] [tasa:: €]`) y las propiedades de facturación de Datos panel (totales y por país) | Cuando Nina diga que ha facturado un mes, marca la casilla y pon los importes reales. Como se factura por previsión, el importe de los meses futuros es la previsión del Sheet: cuando cambie, actualízalo. El primer día laborable a partir del día 5, la revisión de cierre (abajo) |

**Propiedades de `Claude/Datos panel - Spradling.md`**: `actualizado`, `alertas_hoy`, `facturacion_revision`, `facturacion_cuadra`, `facturacion_nota`, `medios_aprobado`, `medios_previsto`, `fee_aprobado`, `fee_consumido`, `fee_facturado`, `fee_pct` (20), `tasa_aprobado`, `tasa_prevista`, `meses_reales`, `fee_consumido_mes`, `fee_facturado_mes`, `medios_mes`, `tasa_mes` (12 valores cada uno), `reserva_web`, `reserva_web_usada`, `remanente`, `aprobado_total`, `consumido_previsto_total`, `facturado_previsto_total`, `paises` (clave → nombre), `aprobado_pais` (Search de cada país en `Presupuesto_Anual`), `inversion_pais` y `facturado_pais` (12 valores por país, de `Check cierre`), `fee_tramos` (vacío: sin escalado), `cuota_fee_mensual` (vacío: no hay cuota fija), `horas_plan`, `paprika_codigos` (código de Paprika por año; cambia cada año: en diciembre, si falta el del año siguiente, recuérdaselo a Nina). Edítalas con un script read-modify-write.

- **Cierre de mes** (el primer día laborable a partir del día 5): desde el Sheet `2026 - Presupuestos Spradling` (`Check cierre`, `Presupuesto_Anual`, `Detalle_Mensual`) actualiza las propiedades de facturación, con `meses_reales` = meses cerrados con datos reales. Totales: `fee_consumido_mes`, `medios_mes` y `tasa_mes` = columnas "Consumido" de `Check cierre`; `fee_facturado_mes` = columna "Facturado · Fee"; `aprobado_total` = "Aprobado · Medios" (C3, sin la reserva web); `consumido_previsto_total` y `facturado_previsto_total` = C5 y C7. **Por país** (columnas S a AF de `Check cierre`): `inversion_pais` = tabla "INVERTIDO" (filas germany… Nuevos productos, enero a diciembre) y `facturado_pais` = tabla "FACTURADO" (lo que va en la descripción de cada factura). Nina controla dos cosas: **lo invertido (real + previsión) cuadra con lo aprobado** y **lo facturado (emitido + previsión) cuadra con lo aprobado**. Como se factura por previsión, que un mes no coincida **no es un error por sí solo**. `facturacion_cuadra: false` si: el invertido previsto o el facturado previsto se desvían más de 100 € de lo aprobado; `Detalle_Mensual` no suma lo mismo que `Presupuesto_Anual`; o el facturado previsto del año de algún país no coincide con su invertido previsto (más de 1 € de diferencia). Explícalo en `facturacion_nota`.
- **Factura de diciembre**: es la que cuadra el año. Cuando se acerque, comprueba por país que "invertido previsto del año − facturado de enero a noviembre" coincide con lo que pone el Sheet para diciembre. Si no, avísalo en la notificación de alertas con la tabla por país. El panel lo enseña en "Próxima factura".
- **Facturas emitidas**: cuando Nina diga que ha emitido una factura, marca la línea del mes en la lista "Facturas 2026" del panel, con el fee, los medios y la tasa reales.
- **Lunes**: horas del mes en curso frente a lo previsto a la fecha de la última captura (alerta si un perfil va más de un 10 % por encima), cuando haya `horas_plan`.
- **Cada día**: `actualizado` y `alertas_hoy`.

## Alertas (por notificación al móvil, solo si hay alguna; nunca por email)
Las alertas son **de campañas y de negocio**, no de status. Cada mañana la tarea diaria las calcula y, si hay al menos una, avisa a Nina con una notificación (PushNotification). Nina no quiere ningún email: no se envían correos. No se guardan en ninguna nota.

Fuente de datos: Sheet **"2026 - Presupuestos Spradling"** (`1Tpj7xuhoNpdiIOewbF-EGHcHCdaRI72TP10_9UYmeGg`):
- Pestañas de gasto que se actualizan solas: `GoogleAds_Spend` y `MetaAds_Spend` (MTD, ayer, semana pasada y mes pasado, por campaña).
- `Detalle_Mensual`: inversión por mes y por canal (youtube, meta, demand-gen, pmax, search).
- `Presupuesto_Anual`: presupuesto por campaña, estado y "Modificaciones presupuestarias".

**Umbrales provisionales** (activados el 06/11/2026, pendientes de validar con Ari):

| Tipo | Regla |
|---|---|
| 💶 **Pacing mensual** | Por canal (search, pmax, demand-gen, youtube, meta) y en total, se compara el gasto MTD con la inversión del mes en `Detalle_Mensual` × (días transcurridos / días del mes). Alerta si se desvía más de un **±15 %** y la diferencia supera los **200 €**. El canal se saca del nombre de la campaña (`<país>_spradling_conversion_search…`, `…_search-ia_…` = search, `…_performance-max_…` = pmax, `…_awareness_youtube_…`, `…_awareness_meta_…`; Meta, por `MetaAds_Spend`). En noviembre y diciembre, ten en cuenta que hay que ejecutar el remanente de 6.820 € hasta el 15/12 |
| 📈 **Pico de gasto diario** (Google Ads: usa `Diario_Campañas` del Sheet diario; Meta, solo si la foto de `MetaAds_Spend` es de ayer o de hoy) | Una campaña gasta ayer más del **150 %** de su media diaria de la semana pasada, con un mínimo de 40 € |
| ⛔ **Campaña parada** | Una campaña activa (ENABLED o ACTIVE; en Google Ads, según la pestaña `Campañas` del Sheet diario) gastó la semana pasada y ayer gastó 0 € (en Google Ads: no tiene fila de ayer en `Diario_Campañas`) |
| 🕒 **Datos desactualizados** | Si las pestañas de gasto no se han actualizado en más de 7 días, calcula el pacing con la fecha de la última foto, indícala en la notificación y avisa |
| 📉 **CTR / CR / CPL** (Google Ads) | Fuente: Sheet **"Spradling - Google Ads diario"** (`1sriNDuHvnG8zTRi07J_-yoHd-lB8ciazJWXwMG6Y_nw`), que rellena cada noche un script de la MCC (`Claude/Scripts/spradling-google-ads-diario.js`). Pestañas: `Diario_Campañas` (campaña × día desde el 1/1/2025), `Diario_Zonas` (campaña × país/región/provincia × día, últimos 90 días), `Mensual_Zonas` (campaña × zona × mes desde el 1/1/2025), `Campañas` (estado, tipo, presupuesto diario) e `Info` (última ejecución). Si la pestaña `Info` no existe todavía o la última ejecución tiene más de 2 días, no calcules estas alertas y dilo en el resumen. Por campaña, compara **ayer** con la **media de los 7 días anteriores**: alerta si el **CTR cae más de un 25 %** (mín. 500 impresiones ayer), si el **CR cae más de un 30 %** (mín. 30 clics) o si el **CPL sube más de un 30 %** (mín. 3 conversiones en los 7 días). Indica campaña, valor de ayer, media y diferencia. Spradling tiene poco volumen por campaña: si una regla salta a diario sin motivo, propón subir el mínimo |
| 📊 **Resumen semanal** (lunes, Google Ads) | Va en la notificación de los lunes aunque no haya otras alertas. (1) **Semana pasada** (lun-dom) frente a la **semana anterior** y frente a la **misma semana del año pasado** (−52 semanas): inversión, conversiones, CPL, CTR y CR, en total, por grupo/país y por tipo (marca, producto, IA, PMax). No compares campaña a campaña con el año pasado (los nombres cambiaron el 22/09/2026). Recuerda que el modelo de conversión cambió con la web nueva: la comparativa interanual es orientativa. (2) **Países**, con `Diario_Zonas` y `Mensual_Zonas`: CPL por país (ES, IT, FR, DE, UK, PL) y los que gastan sin convertir (≥100 € y 0 conversiones) |
| 📅 **Cierre de mes vs año pasado** (con la revisión de facturación del día 5) | Mes cerrado frente al mismo mes de 2025 y acumulado del año: inversión, conversiones, CPL, CTR y CR, en total y por grupo/país. Se añade a `facturacion_nota` solo si hay algo relevante (CPL +15 % o conversiones −15 %) y siempre a la notificación de ese día |

## Kanbanize (cards de tareas)
Lo leen las skills de preparación y de después de reunión (misma lógica en Barraquer e Hispano Suiza). **Antes de crear o cambiar una card, Claude le dice a Nina cómo la va a crear y dónde, y espera su OK.**
- **Tablero**: Sky (board_id 21), en `https://runroom.kanbanize.com`
- **Dónde entran**: workflow **Performance** (80) · columna **Backlog → Spradling** (1680) · carril **Transversal** (116)
- **Parent card**: [52124 · Spradling Campañas 2026](https://runroom.kanbanize.com/ctrl_board/21/cards/52124/details/) (workflow Proyectos). Vínculo de tipo parent.
- **Código Paprika**: campo personalizado **field_id 9**. **SPR010023 (2026) · SPR010024 (2027)** (los de Nina; las cards antiguas y la parent card llevan SPR010021).
- **Reglas de Nina para las cards**: **nunca se pone responsable** en ninguna card. **Tipo de card siempre**. **Fecha** solo si aplica (si hay una fecha comprometida o de entrega).
- **Cards recurrentes de Presupuestos y Facturación**: las crea en Kanbanize la tarea programada "Kanbanize - Cards recurrentes performance" (lunes 8:47, columna Ready). **En Obsidian no se crean** (ni la semanal de Presupuesto ni la mensual de Facturación): en Pendientes solo van tareas pendientes nuestras o del cliente.
- **Tipos del tablero Sky**: 13 Landings · 15 Informes · 18 Propuestas · 22 Implementación analítica · 24 Lanzamiento de campaña · 25 Optimización de campañas · 26 Control presupuestario · 27 Implementación canal · 30 Proyecto · 57 Test a/b.
- **Cómo son las cards de Spradling hoy** (ej. 61669): título `Spradling - <tarea en minúscula>`, tipo 26, prioridad media, color amarillo (fdd835), etiqueta 502, fecha de entrega en `deadline` (12:00), descripción con el enlace a la fuente arriba.
- **Basecamp para compartir actas**: Spradling Europa (19500347) para lo de España; Spradling Internacional (20351671) si afecta a Colombia, en el hilo "2026. Reuniones" (521134468)
