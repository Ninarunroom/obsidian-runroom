---
tipo: propuesta-interna
cliente: "[[00 Ficha de cliente - Barraquer]]"
estado: en marcha (fase 1 · Google Ads)
actualizado: 2026-11-16
---
# Sistema de alertas de campaña (propuesta)

**Objetivo**: detectar cada día lo que se le pueda pasar a Ari (caídas de CTR o CR, subidas de CPL o de gasto diario frente a lo planificado) y avisar a Nina por email.

## Lo que tenemos hoy
- El Sheet `2026 - Presupuesto Barraquer` tiene pestañas de gasto por campaña (Google Ads, Meta, DV360, LinkedIn), pero:
  - **no se actualizan a diario**: la última foto de Google, Meta y DV360 es del lunes 02/11 y la de LinkedIn, del 23/10;
  - solo traen **gasto** (y, en Meta, impresiones y alcance), sin clics ni conversiones.
- Con eso se puede vigilar el pacing de inversión, pero no la calidad.

## Lo que haría falta
1. **Volcado diario** por campaña y día: gasto, impresiones, clics y conversiones (leads). Opciones:
   - **Script de Google Ads en el MCC**: escribe cada noche en un Sheet. Es gratis y fácil de mantener, pero solo cubre Google Ads.
   - **Ampliar el proceso actual** que rellena las pestañas `*_Spend`, sea cual sea, para que traiga clics y conversiones y se ejecute cada día. Cubre todas las plataformas.
2. **Reglas** que Claude aplicaría cada mañana:
   - CTR o CR de la semana pasada > 25 % por debajo de la media de las 4 anteriores.
   - CPL de la semana pasada > 25 % por encima de su media o del objetivo (≈ 21-23 €).
   - Gasto de ayer > 150 % de la media diaria.
   - Gasto del mes fuera de ±15 % del ritmo planificado en `Detalle_Mensual`.
   - Campaña activa con 0 € ayer.
3. **Aviso**: email "Barraquer · Alertas DD/MM" a Nina, solo si hay alguna.

## Preguntas para Ari
- ¿Quién mantiene hoy las pestañas `*_Spend` y cómo se rellenan?
- ¿Prefiere script de Google Ads o ampliar ese proceso?
- ¿Umbrales y CPL objetivo por línea (clínica, estética, internacional)?

## Decisión 05/11/2026: opción gratuita, por fases
Sin Supermetrics ni Windsor. Cada plataforma vuelca sus datos diarios a un Google Sheet con un script gratuito, y la tarea diaria de Claude lo lee.
- **Fase 1 · Google Ads** (en marcha): script de MCC `Claude/Scripts/barraquer-google-ads-diario.js`. Escribe en el Sheet "Barraquer - Google Ads diario" las pestañas `Diario_Campañas` (campaña × día: inversión, impresiones, clics, conversiones, views, CTR, CPC, CPL, CR, VTR), `Diario_Zonas` (campaña × país/región/provincia × día, ubicación física), `Campañas` (estado, tipo, puja, presupuesto diario) e `Info`. Reescribe los últimos 60 días cada noche.
- **Fase 2 · Meta**: Apps Script con la API de Meta (necesita token de usuario del sistema del Business Manager).
- **Fase 3 · DV360**: Apps Script con el servicio de informes de DV360.
- LinkedIn: no, solo se usaba para Instituto (terminado el 30/09).
Sheet: [Barraquer - Google Ads diario](https://docs.google.com/spreadsheets/d/1KGLV2nSbJ5-pVJaZWfvhq35Fe53iqMvVf3GLUjCtQ80/edit). Reglas activas en Instrucciones (umbrales provisionales: CTR −25 %, CR −25 %, CPL +30 % frente a la media de 7 días; resumen de zonas los lunes). Pendiente: validar umbrales con Ari.

## Estado 16/11/2026
- **Fase 1 · Google Ads funcionando**: el script de Google Ads se ejecuta cada mañana (hoy, 16/11 a las 9:01) y rellena el Sheet [Barraquer - Google Ads diario](https://docs.google.com/spreadsheets/d/19wug698fQSCQhfPtA7WGbkopsl3Hl0wJZQfQkOYIs1o/edit), que es el que lee la tarea diaria. El enlace de arriba (1KGLV2…) no coincide con este: revisar si es una copia antigua.
- **Salida**: en vez de email, Claude genera cada día una nota en [[Claude/Alertas]] («Alertas Google Ads AAAA-MM-DD») con los datos de ayer frente a la media de los 7 días anteriores. Solo hay notificación si algo falla (Sheet sin actualizar, error del script…).
- **Reglas activas (por campaña, ayer frente a la media de 7 días)**: campaña activa sin impresiones 🔴 · 0 conversiones con gasto ≥ 130 % del CPL medio 🔴 · pico de gasto > 150 % · caída de gasto < 50 % · CTR −25 % · CPC +30 % · CPL +30 % · CR −25 % · VTR −30 %.
- **De la propuesta, aún sin aplicar**: CPL frente al objetivo (≈ 21-23 €), pacing mensual frente a `Detalle_Mensual` y resumen de zonas de los lunes.
- **Siguiente**: fase 2 (Meta) y fase 3 (DV360).
