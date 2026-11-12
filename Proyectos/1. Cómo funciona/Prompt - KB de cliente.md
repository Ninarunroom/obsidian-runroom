# Prompt — Montar el KB de un cliente (patrón Barraquer)

> Cópialo en un proyecto nuevo de Claude (uno por cliente), rellena el bloque **DATOS DEL CLIENTE** y envíalo desde una conversación vinculada a tu ordenador. Lo que no sepas déjalo vacío: Claude lo buscará o te lo preguntará.

---

Soy Nina, KAM en Runroom. Quiero montar para **[CLIENTE]** el mismo sistema que ya tenemos para Barraquer: un knowledge base de la cuenta en mi bóveda de Obsidian, con paneles de seguimiento y automatizaciones. El modelo de referencia está en mi bóveda, en `Runroom/Runroom/Proyectos/Barraquer/`. **Léelo antes de empezar** (sobre todo `Claude/Instrucciones - Barraquer.md`, las notas de `4. Seguimiento/` y `Claude/Scripts/`) y copia su estructura, su código y su estilo. No lo modifiques.

## DATOS DEL CLIENTE
- Cliente y qué le hacemos (servicios de Runroom): [ ]
- Proyecto(s) de Basecamp (ID de la cuenta 1771388): [ ]
- Dominio de email del cliente: [ ]
- Interlocutor(es) del cliente: [ ]
- Equipo Runroom y rol de cada uno: [ ]
- Carpeta de Drive del cliente: [ ]
- Sheet de presupuesto/facturación: [ ]
- Carpeta de Drive para las actas de reunión: [ ]
- Presupuesto anual aprobado, fee y escalado de fee (si lo hay): [ ]
- Cómo se factura (automática mensual, por hitos…) y cuota mensual: [ ]
- Horas vendidas por perfil y mes, y si han cambiado durante el año: [ ]
- Código de Paprika del año en curso (y del siguiente, si lo sé): [ ]
- ¿Cuentas de prepago con recargas? ¿Quién recarga y qué cuentas comparten saldo?: [ ]
- Plataformas de medios (Google Ads, Meta, DV360, LinkedIn…) y cuentas: [ ]

## REGLAS (no negociables)
- **Basecamp**: solo lectura. Nunca publiques, comentes ni crees nada.
- **Google Drive**: solo lectura. La única excepción es **mover** actas de reunión del cliente que sean mías a su carpeta de actas.
- **Gmail**: solo lectura, salvo los emails de alertas y de actas, que van **solo a nina@runroom.com**. Nunca proceses `notifications@basecamp.com` como correo nuevo.
- **Tareas**: nunca las marques como hechas ni las borres. Lo hago yo, salvo que te lo pida.
- **Datos personales**: si aparecen datos de clientes finales o pacientes (leads, formularios), no los guardes.
- **Compromisos**: no registres como acordado nada de precio, fee o condiciones que no se haya acordado explícitamente.
- No muestres nunca credenciales.
- Las automatizaciones de este proyecto funcionan sin pedirme permiso y me avisan después.

## CÓMO TRABAJAR
1. **Arranque**: dime en una frase qué vas a hacer y crea una lista de tareas con las fases de abajo. Pregúntame solo lo imprescindible que no puedas encontrar tú, todo junto y al principio.
2. **Copia de seguridad**: si la carpeta del cliente ya existe en `Proyectos/`, haz antes una copia (`Claude/_copia-seguridad-AAAA-MM-DD.tar.gz`) y no borres nada sin preguntarme.

## FASES

**1. Descubrimiento.** Lee el proyecto de Basecamp entero (usa `events --pages N` para sacar los IDs de los hilos), la carpeta de Drive, el Sheet de presupuesto, las actas de reunión (busca notas de Gemini con el nombre del cliente en todo mi Drive, en la carpeta de actas y en lo compartido conmigo) y los correos del dominio del cliente. Resúmeme en 10 líneas lo que has entendido y lo que no cuadra.

**2. Estructura en Obsidian** (`Proyectos/[CLIENTE]/`), igual que Barraquer:
- `1. Conocer la cuenta/`: `00 Ficha de cliente - [CLIENTE]` (puerta de entrada, con un callout "Empieza aquí"), `Cronología`, `Documentos`, `Mercados y canales` (o el equivalente para el servicio), `Personas`, `Propuestas y decisiones`.
- `2. Acuerdos/`: reglas pactadas con el cliente, con su porqué. Incluye el escalado de fee si lo hay.
- `3. Reuniones/Raw/` (transcripciones, inmutables) y `3. Reuniones/Procesadas/` (actas que enlazan a su transcripción).
- `4. Seguimiento/`: paneles dataviewjs **Tareas**, **Horas**, **Facturación y fee** y, si hay prepago, **Saldos**.
- `Claude/`: `Instrucciones - [CLIENTE]` (el esquema), `Log`, `Datos panel`, `Datos/` (Pendientes, Estrategia, Actas procesadas), `Fuentes/` y `Scripts/`.
- Añade el cliente a `Proyectos/Inicio.md`.

**3. Paneles.** Copia el código de los paneles de Barraquer y adáptalo: cambia "Barraquer" por el nombre de la carpeta en la detección de la ruta y en los nombres de nota. Lo que ya sabemos que funciona:
- Las notas de panel **no llevan propiedades**. Los datos van en `Claude/Datos panel` y en las listas del final de cada nota (Registro mensual de horas, Recargas, Facturas).
- Las fechas: Dataview convierte `AAAA-MM-DD` y `AAAA-MM` en objetos de fecha, así que usa el helper `fecha()` del panel de Barraquer.
- Euros con punto de miles a mano, sin `toLocaleString`.
- Las horas se registran por mes y por perfil, a partir de la captura de la herramienta de horas. Incluye el plan de horas vendidas por tramo de fechas (`horas_plan`) y el código de Paprika por año (`paprika_codigos`).
- **Prueba cada panel** antes de entregarlo (con jsdom + luxon, simulando Dataview) y revisa una captura.

**4. Ingesta inicial.** Procesa todas las actas (Raw + Procesadas + reparto por el KB + registro en `Actas procesadas`), crea el Pendientes (🟦 Runroom / 🟧 Cliente, con enlace a Basecamp o al acta), la estrategia del año (hecho, a medias, pendiente, sin confirmar, descartado, y de quién es la pelota) y la facturación (aprobado, facturado, invertido y diferencias). Si una tarea de estrategia ya está en Basecamp o en un acta, que salga solo una vez.

**5. Automatizaciones.**
- **Actas**: crea una tarea programada "[CLIENTE] - Actas de reunión" (L-V por la tarde, vinculada a mi ordenador y a la carpeta del cliente), copiando la de Barraquer: busca actas, las pasa a Raw y Procesadas, las mueve a la carpeta de actas si son mías y me envía un email.
- **Tarea diaria de Basecamp** ("Basecamp - Pendientes diarios"): comprueba que el proyecto de Basecamp y el dominio del cliente están incluidos y que su excepción apunta a `Instrucciones - [CLIENTE]`. Si hay que cambiar el prompt, enséñame antes el cambio.
- **Alertas de campaña** (si hay medios): copia `Claude/Scripts/barraquer-google-ads-diario.js` con un Sheet nuevo "[CLIENTE] - Google Ads diario" (histórico desde el 1/1 del año anterior). Pásame el script con la URL ya puesta y las instrucciones para instalarlo en la MCC. Activa las reglas de alertas en Instrucciones con umbrales provisionales.

**6. Cierre.** Comprueba que no hay enlaces rotos, añade una entrada al Log y dime en pocas líneas qué has montado, qué falta (con quién) y las preguntas abiertas.

Escríbeme en castellano, con frases cortas y paso a paso.

## Tablero de tareas (formato estándar)
El Pendientes de cada cliente tiene cuatro secciones, que el panel de Tareas dibuja como un tablero tipo Kanbanize: **🟦 Pendiente Runroom** (nuestro, en marcha) · **🟧 Pendiente cliente** · **📥 Backlog** (nuestro, sin empezar) · **✅ Done**. Cada tarea es un título y, debajo, todo su contexto, que se despliega. Referencia: Spradling (`Claude/Datos/Pendientes - Spradling.md` y `4. Seguimiento/Tareas - Spradling.md`).
