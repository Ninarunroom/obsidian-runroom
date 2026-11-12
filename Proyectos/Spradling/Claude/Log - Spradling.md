# Log — Spradling

Registro cronológico de lo que se ha hecho en esta carpeta (ingests de fuentes nuevas, consultas importantes respondidas y guardadas, revisiones/lint). Cada entrada empieza con `## [AAAA-MM-DD] tipo | título breve` para poder buscarlas con `grep "^## \[" "Log - Spradling.md"`.

## [2026-10-20] reorganización | Reestructuración de la carpeta siguiendo el patrón LLM Wiki (info, Pendientes, Reuniones Raw/Procesadas, Claude/Instrucciones, este log)

## [2025-11-26] reunion | Next steps analítica y tracking (muestras, formularios, presupuesto 2026)
Ingest de la reunión "Next steps spradling". Se fija el enfoque de medición de conversiones por envío de formulario y se define el marco de presupuesto 2026 (~110k€ Adwords + 22k€ fee Runroom). Raw/Procesadas en Reuniones/; Spradling.md actualizado (Servicios, Contexto).

## [2025-12-19] reunion | Estrategia 2026
Ingest de la reunión "Estrategia spradling 2026". Plan anual completo: geotargeting 40/60, awareness 9%, conversiones mejoradas, nueva web prevista para abril 2026. Raw/Procesadas en Reuniones/.

## [2026-01-26] reunion | CRM Sugar — problema de vinculación UTM sin resolver
Ingest de la reunión "CRM Spradling". Primera vez que aparece el problema (aún abierto en septiembre) de que SugarCRM no vincula UTMs sin desarrollo adicional. Se identifica a Redka como proveedor/implementador de Sugar y a Diego Lara Montealegre como desarrollador de la nueva web (Next.js + Python en AWS Amplify). Raw/Procesadas en Reuniones/.

## [2026-07-28] reunion | Revisión backlog — plan de lanzamiento (duplicar y pausar campañas)
Ingest de la reunión interna "Revisión backlog spradling". Se fija el plan de lanzamiento (duplicar campañas, pausarlas, activar con luz verde) con fecha objetivo 7 de septiembre. Raw/Procesadas en Reuniones/.

## [2026-09-01] reunion | Next steps nueva web — lanzamiento confirmado, UTM-CRM sigue sin resolver
Ingest de la reunión "Spradling - next steps nueva web". Confirma el lanzamiento oficial (10/09) y el aplazamiento de campañas al 14/09. El problema de vinculación UTM-CRM (ver 26/01/2026) seguía abierto. Spradling.md, Pendientes y Contactos actualizados con Andrea Ferrer y Diego Lara Montealegre.
## [2026-11-02] ingest | Añadidas cards recurrentes Presupuesto (semanal) y Facturación (mensual, noviembre) — generadas automáticamente, no vía Basecamp/email (fallo del trigger matutino, ver diagnóstico).

## [2026-11-06] reorganización | KB de Spradling con la estructura de Barraquer
Copia de seguridad previa: Claude/_copia-seguridad-2026-11-05.tar.gz. Nueva estructura: 1. Conocer la cuenta (Ficha, Cronología, Documentos, Mercados y canales, Personas, Propuestas y decisiones), 2. Acuerdos, 3. Reuniones (Raw/Procesadas), 4. Seguimiento (paneles Tareas, Horas y Facturación y fee; sin Saldos, porque Runroom paga los medios), Claude/ (Instrucciones, Datos panel, Datos/Pendientes, Estrategia 2026, Actas procesadas, Scripts). Las notas antiguas (Spradling.md, Pendientes, actas e Instrucciones anteriores) están en Claude/_estructura-anterior/ sin borrar.

## [2026-11-06] ingest | Descubrimiento e ingesta inicial
Fuentes: los dos proyectos de Basecamp (Spradling Europa 19500347 y Spradling Internacional 20351671, este último creado el 21/10/2026 con Colombia), el Sheet "2026 - Presupuestos Spradling", la carpeta de Drive y los correos de spradling.group. Actas: las 5 que ya había, rehechas con el formato nuevo (los Raw anteriores se mantienen como estaban, renombrados a "(transcripción)"), y 4 nuevas (05/02, 18/02, 15/04 y 26/10). Pendientes: las 8 tareas anteriores, reorganizadas en 🟦 Runroom / 🟧 Cliente con actualizaciones, y 10 nuevas. Estrategia 2026: 33 acciones. Facturación de enero a octubre según Check cierre (se factura por previsión; confirmado por Nina). Horas y código de Paprika 2026, pendientes de Nina.

## [2026-11-06] automatización | Script de Google Ads y Sheet diario
Claude/Scripts/spradling-google-ads-diario.js (copia del de Barraquer: cuenta 350-973-8243, campaña × día desde el 1/1 del año anterior, zonas de los últimos 90 días y zona × mes). Sheet "Spradling - Google Ads diario" creado en el Drive de Nina (el primero, 19wug…, pasó a ser el de Barraquer; el de Spradling es 1sriNDuH…). Reglas de alertas activadas en Instrucciones con umbrales provisionales.

## [2026-11-06] ajustes | Facturación por país, tareas y Sheet nuevo
Panel de Facturación: nuevas tarjetas "Total 2026" (invertido previsto y facturado previsto frente a lo aprobado) y "Por país" (Check cierre S-AF: invertido, facturado y cuadre del año; importes por país de la próxima factura; en diciembre, el importe para cuadrar). Factura de noviembre emitida (Nina). Pendientes: quitada la tarea de E-sense (Nina no la reconoce; la estrategia la deja como "sin confirmar"); la facturación de noviembre, marcada como hecha; el remanente pasa a ser "preparar una propuesta de reparto". Script y Documentos apuntan al Sheet nuevo.

## [2026-11-06] automatización | Actas movidas y tarea diaria actualizada
5 actas de Nina (26/11, 19/12, 26/01, 28/07, 01/09) movidas de "Meet Recordings" a 03. Actas. Tarea "Basecamp - Pendientes diarios": ahora lee Spradling Europa (19500347) y Spradling Internacional (20351671), sigue la estructura de Instrucciones - Spradling (Pendientes en Claude/Datos, 🟦/🟧, Log en Claude/), hace el Status y las alertas "Spradling · Alertas DD/MM" y mantiene los paneles. La tarea "Spradling - Actas de reunión" (L-V 17:52) mueve las actas nuevas a 03. Actas.

## [2026-11-06] horas | Plan de horas, registro de 2026 y códigos de Paprika
Horas vendidas (Nina): hasta agosto Head 1 h, KAM 7,31 h y Performance 17,43 h; desde septiembre Head 16 h y KAM 9 h. Registro de enero a noviembre (a 06/11) desde la captura de la herramienta de horas. Paprika: SPR010023 (2026) y SPR010024 (2027).

## [2026-11-12] actas | Dos notas a mano de Nina añadidas como complemento
"Implementación CRM Tracking 26 ene" → [[2026-01-26 - CRM Sugar]] y "Documento sin título" (01/09) → [[2026-09-01 - Next steps nueva web]]. 0 tareas nuevas (reuniones de hace más de 30 días). 0 documentos movidos (ya estaban en 03. Actas). 1 ⚠️ en revisión en el acta del 01/09 ("UTMs ya está todo ok" frente a "vinculación UTM → Sugar sin hacer").

## [2026-11-12] ajustes | Sin emails
Nina no quiere ningún email. Las tareas "Spradling - Actas de reunión" y "Basecamp - Pendientes diarios" ya no envían correos: las actas nuevas y las alertas (Barraquer y Spradling) se avisan con una notificación al móvil. Instrucciones actualizadas.

## [2026-11-12] lint | Limpieza de tareas con Nina + novedades del 06-10/11
Copia de seguridad previa: Claude/_copia-seguridad-2026-11-12.tar.gz. Quitadas del Pendientes (Nina): vinculación UTM → Sugar (lo hace el cliente; hilo archivado), acceso de Colombia a GTM (el GTM es de Colombia), reunión de medición sin cookies (no hace falta: se les explica por escrito), reunión de acceso a leads del CRM (próximo paso "de grupo" sin fecha ni dueño), card automática de presupuesto semanal (nadie la pidió), propuesta de reparto del remanente (hecha: Ari la mandó el 10/11), material de ferias (llegó el 06/11; sitelinks lanzados el 10/11), fechas de awareness y lanzamientos (contestado el 10/11: lanzamientos a febrero de 2027, vídeo en el aire), facturación de noviembre (ya hecha). Nueva: OK de Natalia a la reinversión. Estrategia: lanzamientos 1 y 2 descartados para 2026, ferias hechas, awareness actualizado, nueva acción de reinversión; todas las acciones con `[fuente:: …]`. Propuestas y decisiones: fuente en cada fila. Panel de Tareas: fuera la sección "Marcar como hecho"; las fuentes se ven en la lista. Instrucciones: Nina no marca casillas (cierra Claude), regla anti-paja y fuente obligatoria. Causa de que no se viera nada desde el 06/11: la tarea diaria apuntaba a la carpeta antigua "Clientes RR".

## [2026-11-12] ajustes | Acciones "sin confirmar" con responsable y enlace
Las 6 acciones `[?]` de la estrategia (iSense, PMax por categoría, colección sostenible, auditoría fase 1, sesión IDG, PostHog) llevan ahora `[responsable:: …]` sacado del acta (o "sin asignar" si el acta no lo dice) y el enlace a las notas de Gemini (o al PDF de la propuesta) en el campo de enlace, que el panel muestra como "Fuente". La columna del panel pasa de "Sin confirmar (revisar con Ari)" a "No consta si se hizo", y enseña "Le toca a: …".

## [2026-11-12] ajustes | Estrategia solo con lo de la propuesta
Con Nina: "iSense" (18/02) y la colección sostenible (26/10) son el mismo tema y salen de reuniones, no de la estrategia: fuera de Estrategia 2026 y nueva tarea en Pendientes (🟦 Runroom, Ari) con las dos actas. PMax por categoría: pendiente de Ari (está en la propuesta). Descartados: auditoría de medición fase 1, sesión IDG (dos pings sin respuesta) y customer journey con PostHog. Propuestas y decisiones actualizado.

## [2026-11-12] ajustes | Estrategia solo con la propuesta
Fuera de Estrategia 2026 las 15 acciones que salían de reuniones o de Basecamp (las abiertas ya están en Pendientes; las decisiones, en Propuestas y decisiones). Regla añadida en Instrucciones.

## [2026-11-12] kanbanize | Primera card creada
61754 "Spradling - migrar campañas a las audiencias nuevas de GA4" (Sky, Backlog → Spradling, Transversal; hija de 52124; Optimización de campañas; Paprika SPR010023; sin responsable ni fecha). Enlazada en Pendientes.

## [2026-11-12] ajustes | Cards recurrentes solo en Kanbanize
Presupuestos (semanal) y Facturación (mensual) las crea la tarea "Kanbanize - Cards recurrentes performance" (lunes 8:47, columna Ready, sin responsable). Quitadas de Pendientes las cards recurrentes de Obsidian; en Pendientes solo tareas pendientes nuestras o del cliente.

## [2026-11-12] automatización | Cards de informe y preparación de reuniones
Kanbanize (lunes 8:47): informe mensual de Barraquer la semana antes de la "Status barraquer / RR" (Ready, Fixed-date, fecha = día de la reunión); trimestral de Spradling el lunes de la semana del 15 de mar/jun/sep/dic (Backlog, sin fecha, recordatorio para fijar fecha con el cliente); mensual de Hispano Suiza al inicio de mes (Ready, sin fecha). Nueva tarea "Preparación de reuniones de cliente (día antes)" (L-V 16:13): nota en Reuniones/Preparación/ + notificación.
