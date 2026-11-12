---
tipo: lineas-trabajo
cliente: "[[00 Ficha de cliente - Esade SEO]]"
actualizado: 2026-11-12
---
# Líneas de trabajo — Esade SEO y Analítica

Una sección por línea o tema vivo. Es el equivalente a "Mercados y canales" de otras cuentas. Las tareas abiertas están en [[Pendientes - Esade SEO]]; aquí va el contexto.

## SEO técnico y visibilidad en IA - Esade SEO
- **Contexto 26/27**: año de mucha volatilidad (siete incidentes de ranking entre febrero y agosto de 2026; caídas de mayo-junio en varias BU). En jun-ago de 2026, frente al mismo periodo de 2025, el MBA perdió un 34,6 % de clics orgánicos y el EXED un 34,9 % ([[2026-09-18 - Estrategia SEO 26-27]]).
- **Citación en IA**: el 89 % en Google AI Mode y AI Overviews, pero solo el 4,4 % en ChatGPT (media global, 47,1 %). Con Google se trabaja la web; con ChatGPT, el entorno (rankings, prensa, foros).
- **KPIs de IA**: Sistrix (prompts y fuentes de citación) y LLM Pulse. Se reportan a cierre de mes en el hilo [KPIs a les IAs](https://basecamp.com/1771388/projects/19742261/messages/112018257).
- **Fichas de metadatos**: Fer prepara una ficha de keywords y title/meta (BBA, Relaciones Corporativas, Becas) y Sergi la aplica o la pasa a Comunicación. Sergi quiere usar este sistema para las sugerencias de su dashboard.
- **Grados**: metas de BBA aplicadas y reindexadas (28/10). Caída de "student loans" a 0 impresiones (03/11), por revisar.

## EMBA - Esade SEO
- **Problema**: caída sostenida de tráfico y, sobre todo, de solicitudes desde junio de 2026; Madrid es la que más cae. Según el análisis de Sergi (27/10), la web convierte igual que el año pasado, pero llega menos demanda de marca. El orgánico pierde un 38 % de clics, los leads web convierten en solicitud 3-4 veces más que los de Ads, y la caída de la web explica el 44 % de las solicitudes que faltan.
- **Natzir (29/10)**: en Madrid hay 15 solicitudes enviadas frente a 44 el año pasado; el margen está en las solicitudes que se abran antes de febrero. Search Console tuvo un error de registro de impresiones entre el 13/05/2025 y el 27/04/2026: los clics son fiables, las impresiones y posiciones de antes de mayo, no.
- **Trabajo de RR**: backlog F0-F4 de Fer (recuperar posiciones 4-10 en student-profile, precio, admissions y formatos) y plan de acción conjunto del 30/10. Seguimiento en [[Estrategia 26-27 - seguimiento Esade SEO]].
- Las páginas de formatos pasan a unificarse en la ficha del programa (decisión del 30/10).

## Full Time MBA - Esade SEO
- /mba/en pierde un 37 % de clics (28/6-26/10, interanual), igual en marca y en genéricas. La posición de marca mejora: hay menos demanda (migración a la IA). La ficha del programa cae de la posición 12,4 a la 25,8 y la India pierde un 42 %. Sergi activa todos los siguientes pasos (29/10).

## Analítica: GA4, GTM y calidad del dato - Esade SEO
- **Stack**: GA4 (propiedad Web Global), GTM web + sGTM en Stape (load.ss.esade.edu), OneTrust, CrazyEgg, Microsoft Clarity, VWO (por retirar), FormAssembly (esadeforms.tfaforms.net), Eulerian (otro proyecto). Esade usa Windsor para sacar datos por API.
- **Bots de China**: el ~84 % del tráfico de China es automatizado (12 combinaciones de resolución y navegador; Lanzhou al 99 %) e infla el orgánico y el directo. Hubo un pico el 4/11 (15.000 sesiones, IPs de China Telecom y Unicom). Sistemas puso un captcha en CloudFront. Plan aprobado el 10/11 (marca en sGTM, filtro en GA4, fuera `user_active_120`).
- **Consent Mode**: desde el 10/11 GA4 modeliza sesiones (+59 % de un día para otro). Natzir recomienda "Observado" para los KPI.
- **Consentimiento**: auditoría de OneTrust (el 'unknown' es un 25-42 % de las transacciones, a la espera de OneTrust) y cinco ajustes en GTM pedidos el 11/11.
- **Atribución tfaforms.net**: conversiones de FormAssembly atribuidas al referral desde abril; corregido en GTM (finalizado según el Excel del 22/10).
- **Smartwifi**: canal personalizado en GA4 para app-v2.smartwifi.fr (wifi del campus), 01/10; hilo archivado el 05/11.
- **Medición de componentes**: `component_view` con `component_type` en marcha desde el 03/11.
- **Formularios**: FormAssembly ofrece una protección anti-spam (ALTCHA). Está desactivada en todos los formularios actuales y se activa a mano, uno a uno. RR lo está analizando y Sergi pregunta por las horas.

## Dashboard de Sergi - Esade SEO
- Sergi ha montado un dashboard mensual de KPIs (GSC + GA4) con recomendaciones de SEO y CRO generadas por IA. Fer y Marta lo revisaron (14 y 19/10) y lo ven como punto de unión. Marta aclaró el filtro de bots ("ping robot") y que solo cuentan conversiones de formulario. Sergi lo usa como fuente de tareas.
