---
tipo: datos-panel
cliente: "[[00 Ficha de cliente - Esade Do Better]]"
actualizado: 2026-11-12
alertas_hoy: ["📅 Septiembre y octubre sin las horas de Nina (Paprika ESA010245)", "🔎 Tendencias de búsqueda: 8 días desde el último envío (04/11)"]
curso_inicio: 2026-09
paprika_codigos: {"26/27": "ESA010245"}
horas_plan: [["2026-09", 20, 5]]
remanente_inicial: 0
remanente_horas: 19.25
remanente_mes: "octubre 2026 (provisional: faltan las horas de Nina)"
precio_hora: 77.868
precio_hora_nota: "75,6 € + 3 % IPC (propuesta 26/27)"
variacion_max_pct: 20
umbral_cliente_dias: 7
facturacion_periodo: "factura única del curso"
facturacion_meses: 12
coste_agencia_oc: "OC012692"
coste_agencia_importe: 12720
coste_agencia_precio_hora: 53
facturacion_revision: 2026-11-12
facturacion_cuadra: true
facturacion_nota: "El fee del curso (23.360,4 €) está facturado entero: llegó el pedido de Esade por el total y se facturó de una vez (Nina, 12/11). La OC012692 (12.720 €) no es del cliente: es lo que la agencia SEO factura a Runroom por las horas que dedica (53 €/h)."
---
# Datos de los paneles — Esade Do Better

Nota de datos: los paneles de `4. Seguimiento` leen estas propiedades. Las mantiene Claude (ver [[Instrucciones - Esade Do Better]]); no hace falta abrirla.

- `horas_plan`: horas vendidas desde cada mes, como `[mes, agencia, kam]`. Curso 26/27: **25 h/mes en total, con las de Nina dentro** (Nina, 12/11). El reparto 20 + 5 es **deducido**: la OC de la agencia (12.720 €) a 53 €/h son 240 h, es decir, 20 h/mes. Confirmar con Nina.
- `remanente_inicial`: horas que pasan del curso 25/26. No se lleva control (el Sheet "Do Better - Seguimiento horas" no se actualiza), así que se empieza de 0.
- `remanente_horas`: remanente a cierre del último mes registrado frente a las 25 h/mes: (25 − 20) + (25 − 10,75) = **19,25 h** a cierre de octubre. Provisional: faltan las horas de Nina; con 5 h/mes suyas quedaría en unas 9,25 h.
- `paprika_codigos`: código de Paprika por curso. En agosto, si falta el del curso siguiente, recuérdaselo a Nina.
- `coste_agencia_*`: OC de la agencia SEO a Runroom (coste, no ingreso) y su precio/hora. El panel de Facturación calcula con ellos el coste consumido y el margen.
