---
fecha: 2026-01-26
cliente: Spradling
tipo: reunion
fuente: https://docs.google.com/document/d/1CKCnOwUwebRecUpC73u3jc3Br2kAmDAY5-25B30yMak/edit?usp=drivesdk
---

# Resumen procesado — CRM Sugar (26/01/2026)

Primera reunión técnica sobre la migración al nuevo CRM de Spradling, **SugarCRM** (sustituye a HubSpot/Salesforce en otras geografías). El problema central: con los módulos iniciales (Sales y Service, sin Marketing activo todavía), Sugar no captura automáticamente la fuente de conversión como hacía HubSpot — hay que enviarla desde la propia web vía parámetros UTM, y si no se hace bien, la mayoría de conversiones quedarán mal atribuidas a "directo". Nadie en la reunión (ni Runroom ni Spradling ni el desarrollador Diego) tiene aún claro cómo Sugar maneja esto, así que se decide agendar una reunión con **Redka**, el proveedor/implementador de Sugar, para resolverlo.

Dato técnico útil: la nueva web está construida en Next.js + AWS Amplify, con un backend Python que centraliza toda la comunicación con terceros (seguridad). Este problema de vinculación UTM↔CRM reaparece sin resolver en reuniones posteriores (ver reunión del 01/09/2026) — es un punto de seguimiento recurrente, no puntual.
