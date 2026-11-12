# Log — Hispano Suiza

Registro cronológico de lo que se ha hecho en esta carpeta (ingests de fuentes nuevas, consultas importantes respondidas y guardadas, revisiones/lint). Cada entrada empieza con `## [AAAA-MM-DD] tipo | título breve` para poder buscarlas con `grep "^## \[" "Log - Hispano Suiza.md"`.

## [2026-10-20] reorganización | Reestructuración de la carpeta siguiendo el patrón LLM Wiki (info, Pendientes, Reuniones Raw/Procesadas, Claude/Instrucciones, este log)

## [2026-10-20] reunion | Ingest de 3 reuniones desde Drive (Estrategia 2026, Informe marzo, Informe mensual julio)
Procesadas 3 "Notas de Gemini" compartidas por Nina vía Drive (20/02, 22/04, 22/07 — las únicas encontradas para Hispano Suiza en el share). Guardadas en Reuniones/Raw y Reuniones/Procesadas. Actualizada la ficha principal (contactos con email, detalle de servicios/segmentación, contexto sobre la "fase 2"/socio industrial pendiente de firma y el posible tema de acceso a Analytics). Añadido 1 pendiente nuevo (acceso a Analytics, a verificar si sigue abierto). Rellenadas partes de Claude/Instrucciones a partir de patrones observados en las reuniones.
## [2026-11-02] ingest | Añadidas cards recurrentes Presupuesto (semanal) y Facturación (mensual, noviembre) — generadas automáticamente, no vía Basecamp/email (fallo del trigger matutino, ver diagnóstico).

## [2026-11-12] ajustes | Sección Kanbanize en Instrucciones
Tablero Sky, columna del cliente, parent card, código Paprika y formato de las cards, para las skills de preparación y de después de reunión (misma lógica que Spradling).

## [2026-11-12] ajustes | Cards recurrentes solo en Kanbanize
Presupuestos (semanal) y Facturación (mensual) las crea la tarea "Kanbanize - Cards recurrentes performance" (lunes 8:47, columna Ready, sin responsable). Quitadas de Pendientes las cards recurrentes de Obsidian; en Pendientes solo tareas pendientes nuestras o del cliente.

## [2026-11-12] automatización | Cards de informe y preparación de reuniones
Kanbanize (lunes 8:47): informe mensual de Barraquer la semana antes de la "Status barraquer / RR" (Ready, Fixed-date, fecha = día de la reunión); trimestral de Spradling el lunes de la semana del 15 de mar/jun/sep/dic (Backlog, sin fecha, recordatorio para fijar fecha con el cliente); mensual de Hispano Suiza al inicio de mes (Ready, sin fecha). Nueva tarea "Preparación de reuniones de cliente (día antes)" (L-V 16:13): nota en Reuniones/Preparación/ + notificación.

## [2026-11-12] actas | Post-acta: informe mensual octubre (29/10) + brief 2026 (17/12/2025)
- Procesadas: 2026-10-29 Informe mensual octubre (Gemini de Nina) y 2025-12-17 Brief 2026 (acta manual en 02. Actas). Raw, acta en Procesadas, ficha actualizada (mix de canales desde octubre, reparto, criterio Black Friday/remanentes, contexto oct., brief 2026, actualización fase 2).
- Vacía: "Documento sin título" (1yFWn…) de 02. Actas.
- Pendientes: 4 tareas nuevas (Ari ×3: vídeo nuevo de Pipo, optimizaciones Q4/Black Friday, Search; Nina: fecha del informe de noviembre). Ninguna cerrada.
- Mensaje para Basecamp: Reuniones/Para Basecamp/2026-10-29 - Informe mensual octubre (para Basecamp).md (carpeta creada). Sin mensaje para el brief de 2025.
- Movidos a 02. Actas: notas de Gemini del 20/02, 22/04, 22/07 y 29/10.

## [2026-11-12] montaje | KB de performance con el patrón Barraquer
- Estructura nueva: `1. Conocer la cuenta/` (Ficha, Cronología, Documentos, Mercados y canales, Personas, Propuestas y decisiones), `2. Acuerdos/`, `4. Seguimiento/` (paneles Tareas, Horas y Facturación y fee, copiados de Spradling; sin Saldos), `Claude/Datos/` (Pendientes, Estrategia 2026, Actas procesadas) y `Claude/Datos panel`. Instrucciones reescritas con Alcance (solo Performance Media), paneles, reglas de tareas y alertas (ninguna por ahora).
- Fuentes: Basecamp 19038192 (to-dos de presupuesto, facturación, informes, Creas y TRANSVERSAL IA); Sheet "2026 - Presupuesto Hispano Suiza" (Presupuesto_Anual, Detalle_Mensual, Check cierre, leído el 12/11); "2026 - Propuesta Hispano Suiza" (estrategia); carpetas de Drive 01. Propuesta, 02. Actas y 03. Informes; actas procesadas. Gmail: sin correos de hispanosuizacars.com en 45 días.
- Datos de Nina (12/11): horas vendidas (antes: Ari 0,47 / Performance 5,86 / Nina 2,66; después: Ari 13 / Nina 1,5; mes del cambio supuesto: septiembre), sin prepago (Runroom paga los medios), sin alertas de campaña, solo Performance, Paprika 2027 = HIS010011.
- Acta nueva: 2026-01-27 Cierre 2025 (estaba como "descartada" en el registro): Raw + Procesadas.
- Pendientes reorganizado en formato card: 5 tareas 🟦 (las 5 anteriores, con actualizaciones del 30/10 y 05/11), 1 🟧 nueva (enlaces del vídeo nuevo de Pipo, desde el 30/10), 2 🔍 por verificar (acceso a GA4; etiquetado de IA). Ninguna cerrada: en el Status, "¿cerrar?" para la revisión del vídeo (Ari contestó el 30/10) y la regularización de la factura (sustituida por la factura de noviembre de 5.811,65 €, aprobada el 05/11).
- Copia de seguridad previa: `Claude/_copia-seguridad-2026-11-12-b.tar.gz`. `Claude/_estructura-anterior/` se mantiene sin tocar.

## [2026-11-12] ajustes | Respuestas de Nina
- Confirmado: el nuevo reparto de horas (Ari 13 h, Nina 1,5 h) empieza en septiembre de 2026.
- La columna "Reconocido" de Check cierre (y su "bolsa para Next year") no se usa: quitadas las menciones de Datos panel, Acuerdos, Propuestas e Instrucciones.
- Paneles probados (jsdom + captura): Tareas, Horas y Facturación y fee se dibujan sin errores.
