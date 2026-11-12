# Pendientes — Esade SEO y Analítica

Status del día y tareas pendientes, separadas por **quién tiene la pelota**. Se actualiza cada mañana con la tarea diaria (Basecamp, correo y reuniones). Se añaden tareas nuevas en la sección que toca, pero nunca se borran ni se marcan como hechas automáticamente: márcalas tú con `[x]` cuando las completes. En 🟦 Runroom: `[ ]` = backlog (sin empezar) · `[/]` = en curso. Cada tarea lleva **Línea:** SEO técnico, Analítica o Gestión.

## Status (12/11/2026)
- 🕒 **Horas**: Sergi ha preguntado tres veces por la dedicación (02/11 "anem a full", 29/10 y 10/11 sobre el formulario de FormAssembly), y la última pregunta sigue **sin respuesta (2 días)**. Remanente de **37,25 h** a cierre de septiembre (16,25 del curso pasado + 50 − 29; el 75 % de un mes, por encima del ±20 %). **Octubre sin volcar** al Seguimiento.
- 🟧 **Esperando al cliente más de 7 días**: URLs de CrazyEgg (42 d) · Unibuddy y su Hotjar (42 d) · respuesta de OneTrust sobre el 'unknown' (36 d) · prompts de Sistrix / LLM Pulse (41 d) · pedido de compra pendiente (13 d).
- 🟦 **Nuevo de ayer (11/11)**: ajustes de consentimiento en GTM (5 puntos de Sergi) y pico de sesiones del 10/11 (modelización de Consent Mode). Los dos son de Marta.

## 🟦 Runroom

- [ ] **[Tarea]** Esade — Responder a Sergi sobre el volumen de horas (dedicación "a full" y estimación del formulario de FormAssembly)
    - **Línea:** Gestión
    - **Entrega:** cuanto antes (lo ha preguntado tres veces)
    - **Responsable:** Nina
    - **Info:** El 02/11 Sergi pidió que Nina vigile la dedicación porque van "a full". Sobre la protección anti-spam de FormAssembly (ALTCHA), el 29/10 avisó "alerta amb el volum d'hores" y el 10/11 volvió a preguntar si se había mirado. El análisis lo tienen Jordi, Jorge y Joshua, y estaba parado hasta que volviera Joshua.
    - Fuente: [📧 "New forms now come with built-in spam protection" (Sergi, 10/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1879761366507593429) · [📧 "Informe setembre amb alguna actualitzacions" (Sergi, 02/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1880109674396533661) — detectado 12/11/2026
- [/] **[Facturación]** Esade — Cierre de horas de octubre: volcar al Seguimiento las horas de la agencia y las de Paprika
    - **Línea:** Gestión
    - **Entrega:** 05/11/2026 (vencida)
    - **Responsable:** Nina
    - **Info:** En la Bolsa de horas, la agencia ya ha volcado 37,5 h de octubre (Fer 29, Marta 7, Olga 1,5). Faltan las de Nina en Paprika (ESA010246) y pasarlo a la pestaña Curso 26/27. Revisa la OC de las filas de Marta: llevan OC012692, que es la de Do Better.
    - Fuente: [Sheet: Bolsa de horas](https://docs.google.com/spreadsheets/d/1F2KfWNbXZaOp2sEN8ZtMgchEtRdHLS3hkFEeoXoKWTk) · [Sheet: Seguimiento del fee](https://docs.google.com/spreadsheets/d/1o_2qc46-s4txCu9g0rA1S_Q1jHP5T-0G9DjAy21_vG0) — detectado 12/11/2026
- [/] **[Tarea]** Esade — Tráfico bot de China: aplicar las acciones aprobadas por Sergi
    - **Línea:** Analítica
    - **Entrega:** sin fecha definida
    - **Responsable:** Marta
    - **Info:** Sergi aprobó el 10/11 la propuesta de Marta: marcar en el sGTM (Stape) `traffic_type=bot` las combinaciones detectadas sin enviarlas a Google Ads ni a Meta, filtro de datos en GA4 (primero en prueba), quitar `user_active_120` de los eventos clave, segmento para informes pasados y revisión mensual de las combinaciones. Natzir (11/11): la web va por CloudFront (AWS), no por Cloudflare; Sistemas ya puso un captcha a los rangos del pico; para las resoluciones raras basta "China + resolución", porque la versión de Chrome caduca enseguida; propone un honeypot con AWS WAF para Sistemas.
    - Fuente: [Basecamp: Xina](https://basecamp.com/1771388/projects/16901662/messages/113457396) · [📧 "Pico de bots en GA4 el 4 de noviembre" (Natzir, 11/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1881029419490066014) — detectado 22/10/2026
- [ ] **[Petición cliente]** Esade — Ajustes de consentimiento de cookies en GTM (incidencias del Compliance Assistant de OneTrust)
    - **Línea:** Analítica
    - **Entrega:** sin fecha definida
    - **Responsable:** Marta (Jordi en copia)
    - **Info:** Son cinco puntos: (1) CrazyEgg solo con consentimiento de Rendimiento, sin cargar el script antes; (2) API de YouTube sin consentimiento de Publicidad (los iframes los bloquea Esade desde Drupal; hay un Jira abierto); (3) Flowbox condicionado a Funcionales; (4) qué tags generan `_gcl_*`, `sbjs_*` y `crm_tracking`, y que solo se disparen con su consentimiento; (5) `functionality_storage` tiene que empezar denegado, y hay que confirmar el mapeo entre los grupos de OneTrust y Consent Mode y que el sGTM (load.ss.esade.edu) lo respeta.
    - Fuente: [📧 "www.esade.edu · Ajustos de consentiment de galetes a GTM" (Sergi, 11/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1881572888713368359) — detectado 12/11/2026
- [ ] **[Petición cliente]** Esade — Pico de sesiones del 10/11 en GA4: confirmar si es la modelización de Consent Mode
    - **Línea:** Analítica
    - **Entrega:** sin fecha definida
    - **Responsable:** Marta
    - **Info:** Sesiones +59 % y usuarios +73 % de un día para otro, mientras los eventos clave no cambian. Natzir cree que es la modelización (sesiones estimadas) y recomienda la identidad "Observado" para los KPI y para comparar con el histórico; la API y los dashboards también quedan afectados. Falta que Marta confirme si el 9 o el 10/11 cambió algo en GTM, en el sGTM o en OneTrust.
    - Fuente: [📧 "Esade: pic de sessions el 10/11 – és la modelització de Consent Mode?" (Sergi, 11/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1881574014061694620) — detectado 12/11/2026
- [/] **[Tarea]** Esade — EMBA: backlog de recuperación de posiciones 4-10 (F0 y F1)
    - **Línea:** SEO técnico
    - **Entrega:** sin fecha definida
    - **Responsable:** Fer
    - **Info:** F0-01 entregado el 26/10 (ficha de queries perdidas). Fer está con F0-02 (análisis de SERP). Para F1-01, 02, 05, 06, 07 y 08, Sergi pidió antes un inventario de "ya existe / hay que actualizar / hay que crear". El paso 3 del plan ("¿Cuánto cuesta un Executive MBA en España?") pasa a Beyond o link building (Olga). Seguimiento en [[Estrategia 26-27 - seguimiento Esade SEO]].
    - Fuente: [Basecamp: EMBA](https://basecamp.com/1771388/projects/19742261/messages/113264682) · [Backlog EMBA F0-F4 (Drive)](https://drive.google.com/file/d/17wPCCI_OlSEpzuTz6EX7LARGX6vP9JEN/view) — detectado 30/09/2026
- [/] **[Tarea]** Esade — Plan de acción EMBA (30/10): las tareas de RR
    - **Línea:** SEO técnico
    - **Entrega:** sin fecha definida
    - **Responsable:** Fer
    - **Info:** Recuperar las consultas que han caído de 4-10 (WIP); buscar acciones SEO fuera de la web para el EMBA (con Olga, después del 20/11 con Marc González de prensa); unificar las subpáginas del EMBA en la ficha (Natzir, RR y Web; nota en el Sheet: "¿Auditoría Aure?").
    - Fuente: [Sheet: Plan de acción EMBA](https://docs.google.com/spreadsheets/d/1p4C1jAwhScctAqE-pda1-lxsci2dfwnIcYKpeskvRaw) · acta: [[2026-10-30 - Plan de accion EMBA]] — detectado 30/10/2026
- [/] **[Tarea]** Esade — Full Time MBA: analizar a fondo la ficha del programa y el mercado indio
    - **Línea:** SEO técnico
    - **Entrega:** sin fecha definida
    - **Responsable:** Fer
    - **Info:** /mba/en pierde un 37 % de clics (28/6-26/10, interanual). Cuatro URLs concentran el 83 % de lo perdido; la ficha /programmes/full-time-mba pasa de la posición 12,4 a la 25,8 (−52 % de clics) e India pierde un 42 %. Sergi: "Activem tots els next steps" (29/10).
    - Fuente: [Basecamp: Full Time MBA](https://basecamp.com/1771388/projects/19742261/messages/113563313) — detectado 29/10/2026
- [/] **[Tarea]** Esade — Schema: devolver a Sergi los matices a su propuesta (redes sociales en schema)
    - **Línea:** SEO técnico
    - **Entrega:** sin fecha definida
    - **Responsable:** Fer
    - **Info:** Fer pasó el documento de Sergi por su agente de IA, lo cruzó con la respuesta de Natzir y ve cosas con sentido y otras que no haría o no harían falta.
    - Fuente: [📧 "Coses Schema (tot i que la IA potser no en fa cas)" (Sergi, 07/10)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1878390725484215667) — detectado 22/10/2026
- [x] **[Tarea]** Esade — KPIs de visibilidad en IA: capturas de Sistrix a 31/08 para Helen (cierre del curso 25/26)
    - **Línea:** SEO técnico
    - **Entrega:** 05/11/2026
    - **Responsable:** Fer
    - **Info:** Helen pidió capturas (no solo datos) a 31/08 para presentar los resultados del curso 25/26. Fer las mandó el 05/11 (Esade, IE, IESE, Bocconi y London BS) y Helen respondió "con esto es suficiente". Hilo cerrado. El KPI mensual de IA sigue como tarea recurrente en la estrategia.
    - Fuente: [Basecamp: KPIs a les IAs](https://basecamp.com/1771388/projects/19742261/messages/112018257) — detectado 05/11/2026
- [ ] **[Tarea]** Esade — Grados: revisar la caída de impresiones de "student loans" (de 100.000 a 0)
    - **Línea:** SEO técnico
    - **Entrega:** sin fecha definida
    - **Responsable:** Fer
    - **Info:** Lo señala Sergi el 03/11 al compartir el dashboard de octubre. En octubre Fer lo atribuyó a la estacionalidad (−31 clics), pero que caigan a 0 las impresiones apunta a algo técnico (indexación).
    - Fuente: [📧 "Dashboard Setembre" (Sergi, 03/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1878407521139447114) — detectado 12/11/2026


## 🟧 Cliente (esperando a Esade o a terceros)

- [ ] **[Petición cliente]** Esade — Píxeles: confirmar que Helen y Adsmurai dan por buena la respuesta de Marta a su auditoría
    - **Esperando desde:** 10/11/2026
    - **Línea:** Analítica
    - **Info:** Adsmurai (la agencia de paid de Esade) revisó los píxeles y Helen se lo pasó a Marta el 21/10 (Meta, TikTok, LinkedIn y Google Ads). El punto en el que más insistían: "las conversiones de Google Ads del envío del formulario de contacto no salen de GTM, están metidas directamente en el código de la página". Marta respondió el 10/11 que no hay ningún código en la web que envíe conversiones: el dataLayer solo recoge el ID y la etiqueta de conversión, y el envío se hace desde el GTM server. El 11/11 Nina dio a Adsmurai acceso al GTM server para que apliquen ellos sus cambios. Si Helen no vuelve a preguntar, se puede cerrar. Los demás puntos (eventos duplicados de TikTok y LinkedIn, conversiones de LinkedIn en el server que no envían datos, user_info para el EMQ) los aplicará Adsmurai.
    - Fuente: [📧 "Dudas píxels GTM Esade" (Helen 21/10 → Marta 10/11 → Nina 11/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1880287239191335334) — detectado 22/10/2026
- [ ] **[Petición cliente]** Esade — Pasar el listado de URLs de CrazyEgg para limitar la etiqueta de GTM
    - **Línea:** Analítica
    - **Esperando desde:** 01/10/2026
    - **Info:** Lo pidió Marta el 01/10 y Sergi no ha contestado. Con el correo del 11/11 (CrazyEgg solo con consentimiento de Rendimiento) se puede resolver todo junto.
    - Fuente: [Basecamp: Revisant cookies](https://basecamp.com/1771388/projects/16901662/messages/113008269) · [📧 "Ajustos de consentiment de galetes a GTM" (Sergi, 11/11)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1881572888713368359) — detectado 01/10/2026
- [ ] **[Petición cliente]** Esade — Unibuddy: desactivar su Hotjar y limpiar el inventario de OneTrust
    - **Línea:** Analítica
    - **Esperando desde:** 01/10/2026
    - **Info:** Es la propuesta de Marta del 01/10 para las cookies que no son de Esade (Hotjar, Contentsquare, Vimeo, Issuu). Lo tiene que pedir Esade a Unibuddy.
    - Fuente: [Basecamp: Revisant cookies](https://basecamp.com/1771388/projects/16901662/messages/113008269) — detectado 01/10/2026
- [ ] **[Incidencia]** Esade — OneTrust: aclarar qué genera el 'unknown' (25-42 % de transacciones) y qué KPI de consentimiento usar
    - **Línea:** Analítica
    - **Esperando desde:** 07/10/2026
    - **Info:** La consulta la abrió Sergi con OneTrust. Hasta que respondan no se puede concluir nada del CRO del banner. Marta cree que puede deberse al rechazo de cookies o a los adblockers.
    - Fuente: [Basecamp: Cookies](https://basecamp.com/1771388/projects/16901662/messages/108051224) — detectado 07/10/2026
- [x] **[Incidencia]** Esade — Quitar VWO del código (Jira WD9-893)
    - **Línea:** Analítica
    - **Esperando desde:** 29/09/2026
    - **Info:** El test A/B/C de la home de Grados daba resultados inservibles porque VWO y CrazyEgg competían por repintar la página. Sergi pausó el test, quitó dos módulos y abrió el Jira. ⚠️ en revisión: el Excel lo marca "Pendiente RR", pero el ticket es del equipo TIC de Esade. Confirmar quién lo tiene que hacer.
    - **Actualización 12/11:** hecho (lo confirma Nina).
    - Fuente: [Basecamp: Test A/B/C a la home de Graus](https://basecamp.com/1771388/projects/16901662/messages/112172205) · [WD9-893](https://supportesade.atlassian.net/browse/WD9-893) — detectado 29/09/2026
- [ ] **[Petición cliente]** Esade — Sistrix / LLM Pulse: definir qué prompts quiere monitorizar (por BU, marca…)
    - **Línea:** SEO técnico
    - **Esperando desde:** 02/10/2026
    - **Info:** Hay un límite de prompts y Natzir tiene los suyos. En la reunión de estrategia (18/09) se acordó revisarlos por BU e idioma y orientarlos a la decisión de compra. Posible fase 2.
    - Fuente: [📧 "Sistrix Esade" (Sergi/Fer, 02-05/10)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1877946429437146052) · [📧 "Urgent: Esade: Indiciador Sistrix" (Helen/Fer, 09-13/10)](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1878555688637272543) · acta: [[2026-09-18 - Estrategia SEO 26-27]] — detectado 02/10/2026
- [ ] **[Facturación]** Esade — Pedido de compra pendiente de esade marketing a Nina
    - **Línea:** Gestión
    - **Esperando desde:** 30/10/2026
    - **Info:** Quedó como próximo paso de la reunión del plan EMBA. Falta confirmar a qué fee o partida corresponde.
    - Fuente: [Acta Gemini 30/10: Plan de acción EMBA](https://docs.google.com/document/d/1ACMM4oTMCdfXlicfnL4MG2AcC-2oaih1YIF5ZRvOo7g) · acta: [[2026-10-30 - Plan de accion EMBA]] — detectado 30/10/2026
- [ ] **[Petición cliente]** Esade — Plan EMBA: las acciones de Esade, Web y Natzir
    - **Línea:** SEO técnico
    - **Esperando desde:** 30/10/2026
    - **Info:** Probar canonicals en 2-3 programas antes de redirigir (Sergi) · rediseñar el menú móvil (Sergi) · precio de la edición de Madrid de febrero de 2027 en la ficha, en la página de precio y en las metas de las 27 URLs (Natzir/Web, 20/11) · intersticial y chat que tapa el botón del folleto en móvil (Web, 13/11). Afectan al SEO de las URLs del EMBA.
    - Fuente: [Sheet: Plan de acción EMBA](https://docs.google.com/spreadsheets/d/1p4C1jAwhScctAqE-pda1-lxsci2dfwnIcYKpeskvRaw) · acta: [[2026-10-30 - Plan de accion EMBA]] — detectado 30/10/2026
- [ ] **[Petición cliente]** Esade — Validar las fichas de keywords y metadatos de Relaciones Corporativas y del Programa de Becas
    - **Línea:** SEO técnico
    - **Esperando desde:** 10/11/2026
    - **Info:** Fer las entregó el 09/11 y Sergi las ha pasado a Comunicación y Marca, que están rehaciendo esas webs.
    - Fuente: [Basecamp: Relacions corporatives + Endagement](https://basecamp.com/1771388/projects/19742261/messages/113570057) — detectado 10/11/2026

## 🔍 Por verificar (pendientes antiguos que pueden estar cerrados)
No los lee el panel. Confírmalos y márcalos o bórralos tú.
- [ ] tfaforms.net: el Excel marca la corrección en GTM como finalizada (22/10). ¿Respondieron los desarrolladores de FormAssembly y se contestó a Marc Rius y David Ferré (07/10)? → **Visto en el correo:** la exclusión funciona (Natzir, 07/10 y 19/10; [📧 "GTM"](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1876672463422294883)). Marc ofreció abrir un caso con FormAssembly y Sergi lo dejó con prioridad baja.
- [ ] Prodesade: ¿redirigen bien las URLs antiguas desde fuera de Esade? Sergi archivó el hilo el 29/09.
- [ ] Sistrix: ¿se mandaron a Sergi los 50 prompts, los modelos y el método de recogida (02/10)? → **Visto en el correo:** sí, Fer los envió el 05/10 ([📧 "Sistrix Esade"](https://mail.google.com/mail/?authuser=nina@runroom.com#all/thread-f:1877946429437146052)).
