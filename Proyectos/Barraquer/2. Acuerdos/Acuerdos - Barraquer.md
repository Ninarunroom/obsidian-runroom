---
tipo: acuerdos
cliente: "[[00 Ficha de cliente - Barraquer]]"
actualizado: 2026-11-05
---
# Acuerdos — Barraquer

Reglas y convenciones que rigen el trabajo con Barraquer (explícitas o tácitas). Si una nueva fuente contradice alguna, **no se cambia en silencio**: se marca como "en revisión" y se avisa a Nina.

Formato: **regla** · por qué · origen · estado.

## Campañas y mensajes
### Madrid es 100 % privado: no se aceptan mutuas
- **Por qué**: es la política del centro de Madrid. Cualquier anuncio que lo insinúe genera pacientes que no se pueden atender.
- **Origen**: [[2026-07-21 - Status - incidente seguridad y ajustes Madrid]] · **Estado**: vigente

### Sin Lead Gen en Meta para Madrid; foco en awareness y consideración
- **Por qué**: la primera visita cuesta 350 €; el formato de Lead Gen no encaja con una clínica privada de alto coste.
- **Origen**: [[2026-06-22 - Revision presupuestos - expansion Madrid]] · **Estado**: vigente

### Toda campaña con keywords de marca lleva "marca" en el nombre
- **Por qué**: Cristian cruza los namings con sus informes (Power BI). Renombrar campañas existentes rompe la reconciliación manual de gasto; crear campañas nuevas no.
- **Origen**: [[2026-05-14 - Status RR - taxonomia y atribucion]] · [[2026-07-07 - Status - produccion y landing Madrid]] · **Estado**: vigente

### Las campañas por patología van separadas
- **Por qué**: agruparlas (junio de 2026) mejoró el rendimiento, pero impedía atribuir los leads por patología. Se acepta el coste de gestión.
- **Origen**: [[2026-09-10 - Status RR - traspaso de cuenta y discrepancias]] · **Estado**: vigente

### La segmentación geográfica en España se mantiene centralizada (no se separa Cataluña del resto)
- **Por qué**: fragmentarla limita la competencia diaria de los anuncios y empeora el algoritmo.
- **Origen**: [[2026-09-10 - Status RR - traspaso de cuenta y discrepancias]] · **Estado**: vigente

### Las llamadas son conversión secundaria (no principal)
- **Por qué**: no queremos que alteren las pujas automáticas mientras no sepamos cuántas acaban en cita. Se revisan los datos desde el 17/10/2026.
- **Origen**: [[2026-10-08 - Status RR - optimizacion octubre]] · **Estado**: vigente (en evaluación)

### Conversiones principales = contactos con datos del lead
- **Por qué**: citas (1.ª/2.ª visita), contacto de landing, Lead Gen, máster, contacto genérico o portal. Los clics en teléfono, WhatsApp o "cómo llegar" se miden pero no se optimiza hacia ellos. Instituto optimiza a contacto training, contacto general y clic a teléfono.
- **Origen**: [Revisión conversiones (sept 26)](https://basecamp.com/1771388/projects/17192035/todos/520415512) · **Estado**: vigente, pendiente de feedback de Cristian

### Rangos de edad por patología (Google Ads y Meta)
- **Valores**: genérica 30-65+, blefaroplastia 45-65+, refractiva 20-45, cataratas 45-65+, pediátrica 25-65+, presbicia 35-65+, ojo seco 30-65+, estética 40-65+.
- **Origen**: [2025 - Audiencias](https://basecamp.com/1771388/projects/17192035/todos/504838909) (02/2025) · **Estado**: vigente salvo cambio

### Etiquetado de IA en creatividades de Google Ads
- **Regla**: declarar en cada creatividad si usa IA o no (también las activas, de forma retroactiva). En Madrid la IA solo se usó para las locuciones.
- **Por qué**: normativa europea.
- **Origen**: [Uso de imágenes con IA](https://basecamp.com/1771388/projects/17192035/todos/518925595) · **Estado**: vigente

### No usar personas de la web en las creatividades sin confirmar los derechos de imagen
- **Origen**: [A/B Test - CTA](https://basecamp.com/1771388/projects/17192035/todos/476658871) (2023) · **Estado**: vigente

## Datos y accesos
### No se dan accesos a las cuentas publicitarias sin validarlo
- **Por qué**: en julio de 2026 un acceso externo (asociado a Dubái) cambió el CPA objetivo desde el MCC.
- **Origen**: [[2026-07-21 - Status - incidente seguridad y ajustes Madrid]] · **Estado**: vigente

### Los leads de Meta Lead Gen no se guardan en el Drive de Runroom
- **Por qué**: son datos de salud. Van a HubSpot (Lead syncing, formulario `Formulario_Cita_2025_Meta`) o a una carpeta del cliente. Si se comparte un archivo, se borra en cuanto él lo descarga.
- **Origen**: [2025 - Campaña Meta Lead Gen](https://basecamp.com/1771388/projects/17192035/todos/511928663) · **Estado**: vigente

### El dato de leads que cuenta es el de HubSpot, solo formularios de pedir cita y landings
- **Por qué**: la vista "fuente de tráfico más reciente = paid" incluye newsletter y contacto, y eso infla la cifra. Cristian exporta cada semana y cruza con su Power BI.
- **Origen**: [Discrepancias Leads Julio 2026](https://basecamp.com/1771388/projects/17192035/messages/113206335) · **Estado**: vigente

## Presupuesto, saldos y fee
### Escalado de fee por inversión anual
- **Regla**: el % de fee depende de la inversión anual en medios:

| Inversión anual | Fee |
|---|---|
| 0 - 120k | 25 % |
| 120k - 200k | 20 % |
| **200k - 300k** | **18 %** ← tramo actual |
| 300k - 400k | 17 % |
| 400k - 500k | 16 % |
| +500k | 15 % |

- **Por qué**: el fee estándar de Runroom es del 20 %, porque más inversión exige más dedicación y recursos. Por la larga relación, la estabilidad de la cuenta y el alto nivel de control, a Barraquer se le aplica un 10 % de descuento (18 %) y se le ofrece un escalado progresivo *ad hoc* si la inversión sigue creciendo año tras año.
- **Origen**: "Propuesta escalado", propuesta y validada en diciembre de 2025 (negociación del 19/12) · **Estado**: vigente
- ⚠️ **Vigilar**: en 2026 la inversión prevista es de ~292k (clínica y estética 283,7k + Instituto 8,4k), a menos de 8k del umbral de 300k (que pasaría a 17 %). Cualquier push o extra puede cruzarlo. La tarea diaria avisa si te acercas a un umbral o lo cruzas. *Por confirmar: si el Instituto cuenta para el tramo.*

### Fee y facturación
- **Fee**: según el escalado (hoy 18 % sobre la inversión), más la tasa de Google (≈2 %).
- **Facturación**: desde octubre de 2025, **factura automática mensual** con el fee previsto repartido en los meses que quedan (por la factura electrónica, que obliga a emitir antes de cerrar el mes). Mensualmente se envía el detalle de facturado, consumido y pendiente. Los remanentes pasan al año siguiente sin facturar. El Instituto se factura aparte.
- **Origen**: [Facturación automática](https://basecamp.com/1771388/projects/17192035/todos/511453462) · [Presupuesto 2026 + facturas](https://basecamp.com/1771388/projects/17192035/todos/515429553) · **Estado**: vigente
- **Interno, no compartir**: el margen histórico ha sido muy variable (3-5 % algunos años; ~35 % estimado en 2025).

### Los saldos de las plataformas los recarga Cristian
- **Regla**: nosotros vigilamos el saldo y le pedimos que recargue con margen (Google Ads Clínica y Estética, Meta, TikTok).
- **Por qué**: las cuentas están a nombre del cliente. Se han quedado sin saldo varias veces.
- **Estado**: vigente

### La reserva presupuestaria necesita aprobación de Cristian
- **Regla**: sirve para pushes y para formatos nuevos (por ejemplo, anuncios en IA o ChatGPT cuando lleguen a España), pero cada uso se propone y él lo aprueba.
- **Origen**: [2026 - Informe Abril](https://basecamp.com/1771388/projects/17192035/todos/517431691) · **Estado**: vigente

### Las campañas internacionales se lanzan desde la misma cuenta de Clínica
- **Origen**: confirmado con Google en noviembre de 2024 ([competidores blefaroplastia](https://basecamp.com/1771388/projects/17192035/todos/501260094)) · **Estado**: vigente

## Comunicación
### Con Cristian, todo por Basecamp
- **Regla**: si urge, se le avisa por WhatsApp. Escribe en castellano y catalán; se le puede responder en el idioma en que escriba. Pide soluciones, no preguntas.
- **Origen**: acuerdo común de BarraquerKB y práctica habitual · **Estado**: vigente

### Con Dubái (Akram), emails breves
- **Regla**: emails cortos mejor que llamadas para dudas puntuales.
- **Origen**: [[2025-12-18 - Dubai - migracion HubSpot]]

### Precios, fee y condiciones: nada sin validar internamente
- **Regla**: se valida antes con Ari / César. Los cambios de presupuesto fuera de lo pactado, con Ari / Nina.
- **Origen**: [[Instrucciones - Barraquer]] · **Estado**: vigente
