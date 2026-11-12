# Instrucciones para Claude — Esade

Esto es lo que debo tener en cuenta (en chat o en la tarea programada diaria) antes de escribir o responder algo sobre este cliente.

## Tono y estilo con el cliente
- Cuenta con varios interlocutores y líneas de trabajo separadas: Analítica y SEO (Sergi/Fer/Olga/Marta, técnico y orientado a datos), Contenidos (Astrid, editorial/blogging), Do Better (blog, externo), y las líneas finalizadas OPENS (Helena Soler, muy orientado a datos/KPIs — ver nota de confirmación pendiente más abajo), BS&LS y Marca (Rosa Martin/Cristina Isern, más institucional). No asumir que lo que aplica a una línea aplica a las demás.

## Cosas que nunca debo hacer o decir
- No mezclar las líneas finalizadas (Marca -julio 2026-, BS&LS, y OPENS según indicó Nina el 22/10/2026 aunque esto último está pendiente de confirmar, ver Contexto y estado) con Analítica y SEO, Contenidos o Do Better al hablar de la cuenta — son equipos de Esade y Runroom distintos.
- No dar por hecho que OPENS está cerrado en la práctica (hay Pendientes de Basecamp muy recientes, de la primera semana de octubre 2026, con tono de trabajo activo) hasta que Nina confirme si es así o si se refería a otra cosa.
- No dar por sentado que un pendiente de una reunión antigua (anterior a septiembre 2026) sigue abierto sin verificarlo primero — varios de los contactos y procesos han cambiado (ej. salida de Sandra Hernández en Do Better, fin de Marca).
- No prometer cambios técnicos del blog (Do Better) que dependan del equipo de TIC de Esade (el calendario y presupuesto de TIC del curso en curso ya está cerrado).
- No sugerir tocar o modificar contenido del blog firmado por profesores sin autorización explícita de Esade (limitación recurrente, no resuelta).

## Aprobaciones necesarias antes de actuar
- Cambios de presupuesto en campañas de OPENS que afecten a varios programas a la vez (p. ej. mover presupuesto del híbrido a Madrid): seguir el patrón ya validado por Helena Soler, pero confirmar con Araceli antes de aplicar cambios no triviales.
- Cualquier compromiso de coste con Financial Times: requiere validación explícita del presupuesto disponible (ha habido tensión repetida por incrementos de presupuesto en estos acuerdos).
- Cambios de tarifa/presupuesto del blog (Do Better, p. ej. el ajuste por IPC) requieren validación de compras (Runroom) antes de comunicarse al cliente.

## Otros
**Equipo "Do Better" (blog de Esade):** Fernando Alonso / Fer Alonso (falonso.ext@runroom.com) y Olga Castillo (olga.ext@runroom.com) son el equipo externo habitual; David Viejo (dviejo.ext@runroom.com) aparece en informes anteriores (backlinks/enlaces tóxicos). Cambio de contacto por parte de Esade (sept. 2026): Sandra Hernández Blanco dejó el puesto a finales de septiembre 2026 (baja de maternidad); sus funciones se reparten entre Dulce (SEO/analítica) y Judith Magran (contenidos periodísticos, junto con Marta).


## Cómo mantener esta carpeta (patrón LLM Wiki)
Esta carpeta sigue el patrón de "wiki persistente" de Karpathy: las fuentes en bruto (Reuniones/Raw, los emails y Basecamp) se leen pero nunca se modifican; esta carpeta es la wiki que Claude mantiene a partir de ellas; este fichero es el "esquema" que dice cómo hacerlo.

- **Ingest** (llega una fuente nueva, p. ej. una transcripción en `Reuniones/Raw/`): léela entera, resume lo clave, guarda la versión trabajada en `Reuniones/Procesadas/`, actualiza las secciones que correspondan de `Esade.md` (no todo al final) y añade a `Pendientes - Esade.md` cualquier tarea nueva que salga de ahí. Registra la entrada en `Log - Esade.md`.
- **Query** (me preguntas algo sobre este cliente): contesto a partir de lo que ya hay en esta carpeta, no repito la búsqueda desde cero. Si la respuesta genera algo que vale la pena conservar (un análisis, una comparación, una decisión), te lo ofrezco para guardarlo aquí en vez de que se quede solo en el chat.
- **Lint** (me pides una revisión): reviso esta carpeta buscando contradicciones entre notas, datos que parezcan desactualizados, huecos de información y referencias cruzadas que falten, y te los señalo.

## Pendientes (formato tablero)
`Pendientes - Esade.md` tiene cuatro secciones, en este orden: `## 🟦 Runroom` (nuestro, en marcha) · `## 🟧 Cliente` (esperando al cliente) · `## 📥 Backlog` (nuestro, sin empezar) · `## ✅ Done`. Se ve como tablero en [[Tareas - Esade]].
- Cada tarea nueva va en la sección que toque, como `- [ ] texto` y, si hay contexto, debajo con sangría. Delante del texto, la línea de trabajo en negrita: **[Analítica y SEO]**, **[Do Better]**, **[Contenidos]**, **[OPENS]** o **[Marca]**.
- No crear otras secciones ni subsecciones.
- Cerrar tareas lo hace Claude (cuando Nina lo dice o Basecamp, correo o un acta lo dejan claro): `[x]` hecha o `[-]` ya no aplica, se mueve a `## ✅ Done` con una línea "Cerrada DD/MM: motivo".
