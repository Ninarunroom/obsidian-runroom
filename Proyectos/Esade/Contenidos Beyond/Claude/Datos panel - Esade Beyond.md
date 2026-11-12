---
tipo: datos-panel
cliente: "[[00 Ficha de cliente - Esade Beyond]]"
actualizado: 2026-11-12
alertas_hoy: []
curso_inicio: 2026-09
paprika_codigos: {"26/27": "ESA010244"}
horas_plan: [["2026-09", 23, 0], ["2026-10", 30, 0], ["2026-11", 23, 0], ["2027-01", 38, 0], ["2027-02", 23, 0], ["2027-06", 38, 0], ["2027-07", 23, 0], ["2027-08", 0, 0]]
remanente_inicial: 0
remanente_horas: 16.5
remanente_mes: "octubre 2026"
precio_hora: 77.6
precio_hora_nota: "79,93 €/h estimado desde enero (IPC +3 %, pendiente de compras)"
variacion_max_pct: 20
umbral_cliente_dias: 7
presupuesto_curso: 48390.2
presupuesto_nota: "Máximo = curso 25/26 · validado por Helen el 22/10/2026"
medios_presupuesto: 25441.17
medios_remanente_ly: 2079.47
medios_meses: 11
medios_nota: "⚠️ El Sheet de control usa 2.450 €/mes facturados (y más en oct y nov) y el presupuesto validado 2.312,83 €/mes. Pendiente de aclarar con Nina."
facturacion_revision:
facturacion_cuadra:
facturacion_periodo: por pedidos (sep–dic y ene–ago)
facturacion_nota: "Pedido sep–dic 2026: 16.933,73 € (Helen dijo el 22/10 que lo entraba esa semana). Ene–ago 2027: 31.456,47 € con PV estimado de 79,93 €/h, pendiente de compras. Lo no empezado no se factura."
---
# Datos de los paneles — Esade Contenidos Beyond

Nota de datos: los paneles de `4. Seguimiento` leen estas propiedades. Las mantiene Claude (ver [[Instrucciones - Esade Beyond]]); no hace falta abrirla.

- `horas_plan`: horas presupuestadas desde cada mes, como `[mes, agencia, kam]`. Base: 23 h/mes (7 contenidos + 16 link building) de septiembre a julio; octubre +7 h (toxicidad); enero y junio +15 h (estudio de la competencia); agosto 0. El presupuesto no tiene horas de KAM (por confirmar con Nina).
- `remanente_inicial`: 0. No consta remanente de horas del curso 25/26 (el remanente que pasa es de **medios**: `medios_remanente_ly`).
- `remanente_horas`: horas presupuestadas − consumidas a cierre del último mes registrado (sep 23−15 = 8; oct +30−21,5 → 16,5). *Ver Horas.*
- `variacion_max_pct`: ±20 %, umbral **provisional** de alerta (en Beyond no hay un ± pactado).
- `paprika_codigos`: código por curso. Sale del nombre de la carpeta de Drive (ESA010244); por confirmar. En agosto, si falta el del curso siguiente, recuérdaselo a Nina.
