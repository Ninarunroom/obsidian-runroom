# Instrucciones para Claude — Hispano Suiza

Esto es lo que debo tener en cuenta (en chat o en las tareas programadas) antes de escribir o responder algo sobre este cliente. Es el **esquema** de la wiki: dice cómo está organizada la carpeta y cómo mantenerla.

## Alcance
- **Entra**: solo **Performance Media** (paid media de awareness: YouTube, Meta, Search y, si vuelven, TikTok, Demand Gen o LinkedIn), presupuesto, facturación, horas e informes de esa línea.
- **No entra**: el e-commerce [hispanosuiza.boutique](https://www.hispanosuiza.boutique/es/) ni cualquier otro servicio a Hispano Suiza. Si llega algo de eso, no se procesa aquí: se avisa a Nina.
- **Basecamp**: [Hispano Suiza - Performance Media](https://basecamp.com/1771388/projects/19038192) (19038192). **Dominio de email**: hispanosuizacars.com.
- **Rol**: Nina es la KAM (cuenta, presupuesto, facturación, agenda de informes). Ari Iglesias (Head de Performance) ejecuta las campañas desde septiembre de 2026.

## Tono y estilo con el cliente
- Trato cercano e informal (tuteo) con Pablo y Pipo; conversación muy técnica y colaborativa, con jerga de marketing en inglés mezclada con el español de forma natural (BTR, CTR, VTR, CPV, awareness, Demand Gen).
- Nina y Ari muestran datos y proponen; el cliente valida o ajusta en el momento (p. ej. exclusión de keywords, reparto de presupuesto por target).
- Mensajes de Basecamp en **castellano**, saludo "Hola Pablo, Pipo," o "Hola equipo,", firmados "Gracias, Nina". Con cifras claras y sin IVA.
- Pipo viaja mucho y tarda: si hace falta respuesta, recordarlo en el mismo hilo.

## Cosas que nunca debo hacer o decir
- No especular ni comunicar externamente nada sobre la negociación de un socio o partner industrial para la "fase 2" de Hispano Suiza, ni sobre la decisión estratégica de la familia propietaria (vía supercar frente a hypercar con hibridación). Es información interna sensible y no cerrada.
- No comprometerse ante el cliente sobre precio, fee, horas o condiciones sin validarlo antes con Nina o Ari.

## Aprobaciones necesarias antes de actuar
- Cambios de presupuesto o de facturación: requieren confirmación explícita de Pablo (así se ha hecho en septiembre, octubre y noviembre de 2026).
- Exclusión de keywords o cambios relevantes de segmentación en campañas: se revisan y acuerdan con Pablo antes de aplicarlos (p. ej. exclusiones de "Car", "Cars", etc. en marzo de 2026).

## Otros
- "Araceli Iglesias" (en las transcripciones) y "Ari Iglesias" (en Basecamp) son la **misma persona**. Gemini escribe "Randroom/Ranroom" por Runroom, "Deman" por Demand Gen y "Maga" por Magalí.
- Runroom paga los medios y los factura al cliente: **no hay prepago ni recargas**, así que no hay panel de Saldos.

---

## Estructura de la carpeta (patrón LLM Wiki de Karpathy)

Las carpetas están numeradas en orden de lectura. La nota de entrada es `1. Conocer la cuenta/00 Ficha de cliente - Hispano Suiza.md` (alias "Hispano Suiza"). Todo lo que es "de Claude" vive en `Claude/`.

```
Hispano Suiza/
├── 1. Conocer la cuenta/   00 Ficha de cliente - Hispano Suiza (puerta de entrada: cliente, qué hacemos, contactos, dinero, reglas clave, día a día),
│                           Propuestas y decisiones, Cronología, Personas, Documentos,
│                           Mercados y canales - Hispano Suiza (targets, mercados, canales, creatividades y medición)
├── 2. Acuerdos/            Acuerdos - Hispano Suiza
├── 3. Reuniones/
│   ├── Raw/                transcripciones, NUNCA se modifican ("AAAA-MM-DD - Tema (transcripción).md"); Nina también deja aquí las suyas
│   ├── Procesadas/         actas resumidas ("AAAA-MM-DD - Tema.md"), con enlace a su transcripción
│   ├── Para Basecamp/      mensaje con el acta y los next steps, listo para que Nina lo envíe
│   └── Preparación/        pre-acta del día antes
├── 4. Seguimiento/         3 paneles dataviewjs: Tareas, Horas, Facturación y fee (sin Saldos: Runroom paga los medios)
└── Claude/                 de Claude: Datos/ (Pendientes - Hispano Suiza, Estrategia 2026 - Hispano Suiza, Actas procesadas - Hispano Suiza),
                            Instrucciones, Log - Hispano Suiza, Datos panel - Hispano Suiza, Fuentes/, Scripts/, copias de seguridad
```

`Claude/_estructura-anterior/` guarda las notas de antes de la reestructuración del 12/11/2026 (Hispano Suiza.md, Pendientes, Tareas e Instrucciones antiguas). Solo es histórico: no se actualiza ni se toca.

## Operaciones

### Actas de reunión (tarea programada "Actas de reunión - Performance (post-acta)")
Las notas de Gemini se guardan en el "Meet Recordings" de Nina o en documentos que comparte Ari. La carpeta de actas del cliente es [Hispano Suiza/2026/02. Actas](https://drive.google.com/drive/folders/19n_3Ieb866Dv_H7g0kuSM7P1Swp920ln) (`19n_3Ieb866Dv_H7g0kuSM7P1Swp920ln`). Se buscan por título con "hispano" + "Gemini" o con invitados de @hispanosuizacars.com. La tarea mira en `Claude/Datos/Actas procesadas - Hispano Suiza.md` si ya están y, si no: copia el texto a `3. Reuniones/Raw/`, escribe el acta en `3. Reuniones/Procesadas/`, reparte la información por el KB (Ingest, abajo), deja el mensaje en `3. Reuniones/Para Basecamp/` y apunta el ID en el registro. En Drive lo único que hace es **mover** las actas de Hispano Suiza que son de Nina a «02. Actas» (nunca las de otras personas, y nunca edita, renombra, borra ni comparte).

### Ingest (llega una fuente nueva: transcripción, hilo de Basecamp, correo, PDF)
1. Léela entera.
2. Si es una reunión, guarda el texto original en `3. Reuniones/Raw/AAAA-MM-DD - Tema (transcripción).md` (si no estaba ya) y el acta procesada en `3. Reuniones/Procesadas/AAAA-MM-DD - Tema.md`, con una línea final `Transcripción: [[AAAA-MM-DD - Tema (transcripción)]]`: asistentes, contexto, decisiones, próximos pasos y temas abiertos.
3. Actualiza **cada nota afectada**:
   - **Reglas y convenciones** → `2. Acuerdos/Acuerdos - Hispano Suiza`.
   - **Propuestas, aprobaciones, descartes y aplazamientos** → `1. Conocer la cuenta/Propuestas y decisiones - Hispano Suiza`, siempre con el porqué.
   - **Resultados e hitos** → `1. Conocer la cuenta/Cronología - Hispano Suiza` y, si cambia algo importante del estado de la cuenta, la sección que toque de `00 Ficha de cliente - Hispano Suiza` (Dinero, Contactos, Temas sensibles…).
   - **Targets, mercados, canales, creatividades y medición** → la sección que toque de `1. Conocer la cuenta/Mercados y canales - Hispano Suiza`.
   - **Personas** → `1. Conocer la cuenta/Personas - Hispano Suiza`.
   - **Documentos nuevos (con enlace)** → `1. Conocer la cuenta/Documentos - Hispano Suiza`.
   - **Avances de la estrategia** → `Claude/Datos/Estrategia 2026 - Hispano Suiza.md` (cambia el estado de la casilla y el `motivo`, con evidencia).
   - **Tareas** → `Claude/Datos/Pendientes - Hispano Suiza.md`. Si salen de una reunión, la línea Fuente lleva el enlace al documento de Drive y además `· acta: [[AAAA-MM-DD - Tema]]`. Si salen de Basecamp, el enlace al hilo. **Basecamp no se copia a Raw**: es la fuente en bruto y se consulta en directo.
4. Si cambia algo de lo que resume la Ficha de cliente, actualiza su sección. Las "Reglas clave" son un resumen de Acuerdos.
5. **Contradicciones**: no sobrescribir. Marca "⚠️ en revisión" con las dos versiones, su fuente y su fecha, y avisa a Nina.
6. Registra la entrada en `Claude/Log - Hispano Suiza.md`.

### Pendientes: status y quién tiene la pelota
- Arriba del todo va la sección **"## Status (DD/MM/AAAA)"**, que reescribe la tarea diaria. Es un resumen, no una alerta:
  - lo que está **esperando al cliente más de 7 días** (con los días);
  - lo **nuestro vencido o que vence en ≤2 días laborables**;
  - los **mensajes de Pablo o Pipo sin contestar después de 48 h laborables**;
  - la **factura del mes**: si está aprobada y no consta emitida, o si falta la aprobación de Pablo;
  - las tareas que parecen hechas, como **"¿cerrar? …"**.
- **Secciones**, en este orden: `## 🟦 Runroom` (nuestro, en marcha) · `## 🟧 Cliente (esperando a Hispano Suiza)` · `## 🔍 Por verificar` (temas antiguos que pueden estar cerrados) · `## 📥 Backlog` (nuestro, sin empezar) · `## ✅ Done`. El panel de Tareas las dibuja como un tablero.
- Cada tarea: una línea `- [ ] **[Tipo]** Hispano Suiza — título` y debajo, con sangría, el contexto.
  - **🟦 Runroom**: campos Entrega, Responsable, Info, Fuente.
  - **🟧 Cliente**: campos Esperando desde, Info, Fuente.
- **Qué entra**: solo tareas concretas, con dueño y una fuente que se pueda abrir. No entran "confirmar si…" genéricos ni cards automáticas.
- **Cerrar tareas lo decide Nina.** Claude no marca ni borra tareas por su cuenta: si Basecamp, el correo o un acta dejan claro que algo está hecho o sobra, lo pone en el Status como "¿cerrar? …" y añade debajo de la tarea "- **Actualización DD/MM:** …". Cuando Nina lo dice en el chat ("hecho", "sobra", "quítalo"), Claude la cierra: `[x]` si está hecha o `[-]` si ya no aplica, la mueve a `## ✅ Done` con "- **Cerrada DD/MM:** motivo" y lo apunta en el Log.
- **Estrategia ≠ reuniones**: en `Estrategia 2026 - Hispano Suiza` solo va lo que está en la propuesta de 2026. Lo que sale de una reunión o de Basecamp va a Pendientes o a Propuestas y decisiones.

### Query
Contesto a partir de la wiki, citando las notas. Si la pregunta toca datos actuales (inversión, facturación, resultados), consulto en vivo los documentos de `1. Conocer la cuenta/Documentos - Hispano Suiza`. Si no puedo, lo digo.

### Lint
Busco contradicciones, datos desactualizados, pendientes que parezcan resueltos (los señalo, no los marco), enlaces rotos y huecos.

## Paneles de seguimiento (4. Seguimiento)
Tres notas con un bloque `dataviewjs` cada una (plugin Dataview). **Nunca se edita su código ni se les añaden propiedades**: los datos viven en otras notas.

| Panel | De dónde lee | Qué mantiene Claude |
|---|---|---|
| **Tareas - Hispano Suiza** | `Claude/Datos/Pendientes - Hispano Suiza.md` y `Claude/Datos/Estrategia 2026 - Hispano Suiza.md` | Las tareas. Estrategia: `[x]` hecho, `[/]` a medias, `[ ]` pendiente, `[?]` sin confirmar, `[-]` descartado, `[pelota:: cliente\|runroom]`, `[motivo:: …]`, `[basecamp:: enlace]`, `[nuevo:: sí]`, `[fuente:: …]` (obligatorio) |
| **Horas - Hispano Suiza** | Lista "Registro mensual" de la propia nota (`[mes:: AAAA-MM] [head:: h] [kam:: h] [performance:: h] [otros:: h] [actualizado:: AAAA-MM-DD]`) y `horas_plan` de Datos panel (horas vendidas al mes: hasta agosto Head-Ari 0,47 / KAM-Nina 2,66 / Performance 5,86; desde septiembre Head-Ari 13 / KAM-Nina 1,5) | Cuando Nina pase una captura de la herramienta de horas, actualiza la línea del mes (y `actualizado`). "KAMPO" = kam, "Performance M…" = performance, "z_Becario" = otros |
| **Facturación y fee - Hispano Suiza** | Lista "Facturas 2026" de la propia nota (`- [x] Factura de <mes> [mes:: AAAA-MM] [importe:: fee facturado] [medios:: medios + tasa facturados] [total:: €]`) y las propiedades de facturación de Datos panel | Cuando Nina diga que ha emitido una factura, marca la casilla y pon los importes reales. Los meses futuros llevan la previsión del Sheet: cuando cambie, actualízala. El primer día laborable a partir del día 5, la revisión de cierre (abajo) |

**Propiedades de `Claude/Datos panel - Hispano Suiza.md`**: `actualizado`, `alertas_hoy`, `facturacion_revision`, `facturacion_cuadra`, `facturacion_nota`, `medios_aprobado`, `medios_previsto`, `fee_aprobado`, `fee_consumido`, `fee_facturado`, `fee_pct` (22), `tasa_aprobado`, `tasa_prevista`, `meses_reales`, `fee_consumido_mes`, `fee_facturado_mes`, `medios_mes`, `tasa_mes` (12 valores cada uno), `aprobado_total` (vigente, "v2" de Check cierre), `aprobado_original` (110.300), `consumido_previsto_total`, `facturado_previsto_total`, `fee_tramos` (vacío: sin escalado), `cuota_fee_mensual` (vacío: no hay cuota fija), `horas_plan`, `paprika_codigos` (cambia cada año: en diciembre, si falta el del año siguiente, recuérdaselo a Nina). Edítalas con un script read-modify-write.

- **Cierre de mes** (el primer día laborable a partir del día 5): desde el Sheet `2026 - Presupuesto Hispano Suiza` (`Check cierre`, `Presupuesto_Anual`, `Detalle_Mensual`) actualiza las propiedades: `medios_mes`, `tasa_mes` y `fee_consumido_mes` = columnas "Consumido" (Medios, Tasa, Fee); `fee_facturado_mes` = "Facturado · Fee"; `aprobado_total` = C2 ("v2"); `consumido_previsto_total` y `facturado_previsto_total` = totales de las tablas Consumido y Facturado; `meses_reales` = meses cerrados con datos reales. La columna "Reconocido" de `Check cierre` no se usa (Nina, 12/11/2026). Como se factura por previsión, que un mes no coincida **no es un error por sí solo**. `facturacion_cuadra: false` si el consumido previsto o el facturado previsto del año se desvían más de 100 € del aprobado vigente, o si `Detalle_Mensual` no suma lo mismo que `Presupuesto_Anual` (más de 1 €). Explícalo en `facturacion_nota`.
- **Factura del mes**: el importe que se propone a Pablo es la previsión del mes + la diferencia acumulada (consumido real − facturado) a cierre del mes anterior, como el 05/11/2026. Nunca se da por aprobada sin su OK en Basecamp.
- **Lunes**: horas del mes en curso frente a lo previsto a la fecha de la última captura (aviso en el Status si un perfil va más de un 10 % por encima).
- **Cada día**: `actualizado` y `alertas_hoy` (de momento, vacío: no hay alertas de campaña).

## Alertas
**De momento, ninguna alerta de campaña** (decisión de Nina, 12/11/2026). Solo el Status de Pendientes (tareas, mensajes sin contestar, factura del mes y horas). No se envían emails. Si Nina las pide más adelante, el Sheet de presupuesto ya tiene `GoogleAds_Spend` y `MetaAds_Spend` por campaña para calcular pacing y campañas paradas, como en Spradling.

## Kanbanize (cards de tareas)
Lo leen las skills de preparación y de después de reunión (y es la misma lógica en Spradling y Barraquer).
- **Reglas de Nina para las cards**: **nunca se pone responsable** en ninguna card. **Tipo de card siempre**. **Fecha** solo si aplica (fecha comprometida o de entrega). **Antes de crear o cambiar una card, Claude le dice a Nina cómo la va a crear y dónde, y espera su OK.**
- **Cards recurrentes de Presupuestos, Facturación e Informe mensual**: las crea en Kanbanize la tarea programada "Kanbanize - Cards recurrentes performance" (lunes 8:47, columna Ready). **En Obsidian no se crean**: en Pendientes solo van tareas pendientes nuestras o del cliente.
- **Tipos del tablero Sky**: 13 Landings · 15 Informes · 18 Propuestas · 22 Implementación analítica · 24 Lanzamiento de campaña · 25 Optimización de campañas · 26 Control presupuestario · 27 Implementación canal · 30 Proyecto · 57 Test a/b.
- **Tablero**: Sky (board_id 21), en `https://runroom.kanbanize.com`. Workflow **Performance** (80), carril **Transversal** (116). Código Paprika en el campo personalizado **field_id 9**.
- **Dónde entran**: columna **Backlog → Hispano Suiza** (1679).
- **Parent card**: [51523 · Hispano Suiza Campañas 2026](https://runroom.kanbanize.com/ctrl_board/21/cards/51523/details/). La de 2027 aún no existe.
- **Código Paprika**: **HIS010010 (2026) · HIS010011 (2027)** (los mismos que en `Datos panel - Hispano Suiza`).
- **Formato de las cards de Hispano Suiza**: título `Hispano Suiza - <tarea>`, prioridad media, color rojo (af0020), etiqueta 639.

## Reuniones
- **Mensual de informe**. La fecha la decide Nina con Ari y después la cierra con el cliente (por el to-do "2026 - report <mes>" de Basecamp). A veces se juntan dos meses. La card de informe se crea a principios de mes, en Ready, sin fecha, con la subtask "Nina - cerrar fecha de la reunión con Ari".
- Pre-acta: la tarde anterior (`3. Reuniones/Preparación/`). Post-acta: la tarde de la reunión (ver "Actas de reunión" arriba).
- **Mensaje para Basecamp**: proyecto Hispano Suiza - Performance Media (19038192), en el to-do del informe del mes. Ruta del borrador: `3. Reuniones/Para Basecamp/`. Sin nada de la fase 2. En Basecamp publica siempre Nina.
