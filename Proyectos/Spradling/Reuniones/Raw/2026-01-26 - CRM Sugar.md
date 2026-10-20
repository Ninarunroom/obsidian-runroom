---
fecha: 2026-01-26
cliente: Spradling
tipo: reunion
fuente: https://docs.google.com/document/d/1CKCnOwUwebRecUpC73u3jc3Br2kAmDAY5-25B30yMak/edit?usp=drivesdk
---

# CRM Spradling — 26/01/2026

**Invitados:** Nina Gotós, Araceli Iglesias, Magalí Federico (Runroom); Andrea Ferrer, Natalia Cortes (Spradling Europe); Diego Lara Montealegre (desarrollo web, equipo Colombia); "Spradling Group" (Laura, interlocutora sin apellido registrado en las notas)

Nota: la transcripción automática confunde repetidamente "Runroom" con "Ranroom"/"Randroom" — es la misma agencia.

## Resumen
Reunión sobre la transición de tracking al nuevo CRM Sugar. Runroom no ha trabajado antes con Sugar (sí con HubSpot y Salesforce) y no conoce la nueva web, por lo que no sabe cómo se comunican entre sí. Se acordó que Spradling (Andrea Ferrer) gestionaría una reunión con **Redka** (proveedor/implementador de Sugar) para entender cómo configurar el tracking de fuentes de conversión y evitar que se atribuyan por defecto a "directo". Diego Lara Montealegre explicó que la nueva web está en Next.js, desplegada en AWS Amplify, con backend en Python que gestiona la comunicación con terceros (incl. Sugar) por API, y pidió un usuario de prueba en el entorno de pre-producción de Sugar.

## Detalles
- Los módulos de Sugar que se lanzan inicialmente son Sales y Service (no Marketing); bajo estos módulos, la fuente de conversión debe ser enviada desde la propia web/landing, no la captura Sugar automáticamente como sí hacía HubSpot con su código de seguimiento.
- Cuando el módulo de Marketing de Sugar se active, se espera que la conexión sea automática — pero mientras tanto hay que cubrir ese hueco con desarrollo.
- Riesgo técnico clave: si un usuario entra por un anuncio, no convierte, y vuelve más tarde directo (sin UTM), se le atribuirá "directo" en CRM aunque el origen real fuera pago — esto puede inflar artificialmente la atribución "directo" en los reportes de Sugar.
- Solución habitual de Runroom en estos casos: parametrización por URL + captura de UTMs en formularios + (en una fase más avanzada) guardarlas en local storage para no perderlas al navegar.
- Se solicita confirmar con Google la implementación de "enhanced conversions" para usuarios que no aceptan cookies.
- Next.js + AWS Amplify + backend Python: toda comunicación con terceros (Sugar, HubSpot, otras integraciones) pasa por el backend Python por seguridad (no directo desde el frontend).

## Próximos pasos
- Andrea Ferrer: agendar reunión con Redka para entender cómo han resuelto el tracking de conversiones con otros clientes y si el módulo de Marketing lo soluciona.
- Equipo de desarrollo de la nueva web: compartir con Runroom la estructura/lenguaje/diseño de la web (Runroom no la ha desarrollado).
- Araceli Iglesias: preparar listado de necesidades de tracking para llevar a la reunión con Redka.
