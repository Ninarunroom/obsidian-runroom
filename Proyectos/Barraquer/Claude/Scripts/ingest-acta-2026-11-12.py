import sys, os
B = sys.argv[1]
ACTA = "[[2026-11-12 - Status RR - remanente, Madrid y contenidos]]"
DOC = "https://docs.google.com/document/d/1KwOa2-ND1Jp3jMdOULItwlId1BO8vZPsvtlEL-pKoRM/edit"
FUENTE = f"Fuente: [Status RR 12/11]({DOC}) · acta: {ACTA} — detectado 12/11/2026"
errs = []

def edit(rel, pairs):
    p = os.path.join(B, rel)
    t = open(p, encoding="utf-8").read()
    for old, new in pairs:
        if t.count(old) != 1:
            errs.append(f"{rel}: {t.count(old)} coincidencias para {old[:60]!r}")
            continue
        t = t.replace(old, new)
    open(p, "w", encoding="utf-8").write(t)

# 1. Instrucciones: idioma con el cliente
edit("Claude/Instrucciones - Barraquer.md", [(
"- Prefiere comunicación directa y resolutiva, por Basecamp (WhatsApp solo para avisar si urge). Escribe en castellano o catalán.",
"- Prefiere comunicación directa y resolutiva, por Basecamp (WhatsApp solo para avisar si urge). Escribe en castellano o catalán.\n- **Nina habla con Cristian en catalán**: todo lo que vaya al cliente (mensajes de Basecamp con el acta y los next steps, correos) se escribe **en catalán**. Las actas y las notas internas del KB siguen en castellano.")])

# 2. Pendientes
P = "Claude/Datos/Pendientes - Barraquer.md"
nuevas_rr = f"""- [ ] **[Tarea]** Barraquer — Activar el push de patologías y pasar a Cristian los números redondos del remanente (reparto para reforzar España y Madrid)
    - **Entrega:** 19/11/2026 (propuesta)
    - **Responsable:** Ari
    - **Info:** Cristian aprobó el push ("tira") el 12/11. Quedan ≈ 32,8k; Cristian calcula ≈ 27k libres. Se usarán para reforzar España y Madrid, como a final de 2025, sin gastar por gastar.
    - {FUENTE}
- [ ] **[Propuesta]** Barraquer — Propuesta de radio / audio programático para Madrid (one shot, 2.ª-3.ª semana de diciembre)
    - **Entrega:** 26/11/2026 (propuesta)
    - **Responsable:** Nina y Ari
    - **Info:** Con el remanente. Incluir presupuesto, inversión mínima y la creatividad necesaria (falca). Antecedentes: Wiimas, mínimo 3.000 €/mes (21/07); catálogo de medios tradicionales del 85 aniversario (12/02); [Barraquer x DV360: New Formats](https://docs.google.com/presentation/d/1MGpd33Ajr4dvMOVVotcZCC2q_5EStZJnTPyOoXZMd2c/edit) (audio, CTV, DOOH).
    - {FUENTE}
- [ ] **[Propuesta]** Barraquer — Propuesta de contenidos y creatividades: 2-3 posts promocionados al mes (≈ 500 €/mes), calendario de patologías y vídeos cortos
    - **Entrega:** sin fecha definida (propuesta: 27/11/2026)
    - **Responsable:** Ari
    - **Info:** Cristian no puede llevar la estrategia de contenidos tras la salida de Lorena. Ari recupera lo ya hablado sobre creatividades.
    - {FUENTE}
- [ ] **[Tarea]** Barraquer — Comentar con César si conocemos perfiles o agencias externas para cubrir el rol de Lorena (redes, calendario de contenidos, reseñas de Google)
    - **Entrega:** sin fecha definida
    - **Responsable:** Ari
    - {FUENTE}
- [ ] **[Tarea]** Barraquer — Reenviar a Cristian las notas de Gemini y la presentación de cada reunión (no le llegan)
    - **Entrega:** 13/11/2026
    - **Responsable:** Nina
    - **Info:** A partir de ahora, después de cada reunión.
    - {FUENTE}

"""
nueva_cli = f"""- [ ] **[Petición cliente]** Barraquer — Pasar los vídeos cortos (≈ 30 s) de los doctores de Madrid para campañas de consideración
    - **Esperando desde:** 12/11/2026
    - **Info:** Tendrá más vídeos en noviembre.
    - {FUENTE}

"""
edit(P, [
 ("## 🟧 Cliente (esperando a Cristian)", nuevas_rr + "## 🟧 Cliente (esperando a Cristian)"),
 ("## Hechos y por confirmar", nueva_cli + "## Hechos y por confirmar"),
 ("- [ ] **[Petición cliente]** Barraquer — Responder a la propuesta de push en campañas de patologías",
  "- [x] **[Petición cliente]** Barraquer — Responder a la propuesta de push en campañas de patologías"),
 ("    - **Info:** Blefaroplastia, cataratas, presbicia y refractiva. Las de Google están limitadas por presupuesto; las de Meta tienen margen. Hay 30,6k sin activar.",
  "    - **Info:** Blefaroplastia, cataratas, presbicia y refractiva. Las de Google están limitadas por presupuesto; las de Meta tienen margen. Hay 30,6k sin activar.\n    - **Actualización 12/11:** aprobado por Cristian en el status ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]]). Lo activa Ari."),
 ("    - **Actualización 05/11:** hay 7.736,68 € disponibles (dato de Nina). Parece recargado: márcala si lo confirmas.",
  "    - **Actualización 05/11:** hay 7.736,68 € disponibles (dato de Nina). Parece recargado: márcala si lo confirmas.\n    - **Actualización 12/11:** Ari avisa en el status de que **no queda saldo en Clínica**. Cristian tiene que recargar ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]])."),
 ("    - **Info:** Quedó \"pendiente de más debate interno\" el 08/10. Está ligado a la propuesta de push de Ari del 16/10 (15,7k en reserva).",
  "    - **Info:** Quedó \"pendiente de más debate interno\" el 08/10. Está ligado a la propuesta de push de Ari del 16/10 (15,7k en reserva).\n    - **Actualización 12/11:** la apertura de términos de marca no ha funcionado mucho. Ari plantea abrir awareness genérico por patología en estos mercados (sin propuesta formal). El remanente general se dedica a España y Madrid ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]])."),
 ("    - **Esperando desde:** 29/10/2026\n    - Fuente: [2026 - ROI]",
  "    - **Esperando desde:** 29/10/2026\n    - **Actualización 12/11:** Ari recuerda en el status que el documento de inversión revisado (hasta octubre) está en su SharePoint y en Basecamp. Cristian: \"vale\". Sigue faltando el ROI 2026.\n    - Fuente: [2026 - ROI]"),
 ("    - **Esperando desde:** 12/03/2026\n    - Fuente: [Status 30/9](https://basecamp.com/1771388/projects/17192035/todos/520642038) · [2026 - Informe Febrero]",
  "    - **Esperando desde:** 12/03/2026\n    - **Actualización 12/11:** Cristian está revisando la propuesta creativa de Estética. En Estética quedan 2k pendientes (PMax) y el pacing va un 35 % por debajo del año pasado.\n    - Fuente: [Status 30/9](https://basecamp.com/1771388/projects/17192035/todos/520642038) · [2026 - Informe Febrero]"),
])

# 3. Actas procesadas
edit("Claude/Datos/Actas procesadas.md", [(
"[notas:: complemento; notas manuales \"STATUS 2 SEPT\"; ya estaba en 00. Actas reunión]\n",
"[notas:: complemento; notas manuales \"STATUS 2 SEPT\"; ya estaba en 00. Actas reunión]\n"
f"- [id:: 1KwOa2-ND1Jp3jMdOULItwlId1BO8vZPsvtlEL-pKoRM] [fecha:: 2026-11-12] [estado:: procesada] [acta:: {ACTA}] [notas:: procesada a mano (skill despues-reunion-cliente); movida a 00. Actas reunión el 2026-11-12]\n")])

K = "1. Conocer la cuenta/"
# 4. Cronología
edit(K + "Cronología - Barraquer.md", [(
"Saldo de Google Ads recargado (7.736,68 € disponibles el 05/11).",
"Saldo de Google Ads recargado (7.736,68 € disponibles el 05/11). Status del 12/11: octubre con 1.026 leads de pago (983 en octubre de 2025) y un 12 % menos de inversión en clínica; Q4 irá ≈ 28k por debajo de 2025. Aprobado el push de patologías y el uso del remanente (≈ 27k libres) para reforzar España y Madrid; Clínica sin saldo ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]]).")])

# 5. Propuestas y decisiones
edit(K + "Propuestas y decisiones - Barraquer.md", [
 ("| 16/10/2026 | Push de 500 € por campaña en patologías (blefaroplastia, cataratas, presbicia, refractiva) hasta mediados de noviembre, con parte de los 30,6k sin activar | 🟡 | Google limitada por presupuesto; Meta con margen. [Basecamp](https://basecamp.com/1771388/projects/17192035/todos/521039257) |",
  "| 12/11/2026 | Usar el remanente (≈ 32,8k; ≈ 27k libres) para reforzar España y Madrid | 🟢 | Aprobado en el status del 12/11. Como a final de 2025; Cristian no quiere gastar por gastar. Ari pasa los números ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]]) |\n"
  "| 12/11/2026 | Contenidos: 2-3 posts promocionados al mes (≈ 500 €/mes), calendario de patologías y vídeos cortos | 🟡 | Ari prepara la propuesta. Cristian no puede llevarlo tras la salida de Lorena |\n"
  "| 12/11/2026 | Awareness genérico por patología en países nuevos | 🟡 | Idea de Ari: la marca aún no tiene penetración. Sin propuesta formal |\n"
  "| 16/10/2026 | Push de 500 € por campaña en patologías (blefaroplastia, cataratas, presbicia, refractiva) hasta mediados de noviembre, con parte de los 30,6k sin activar | 🟢 | Aprobado por Cristian el 12/11 ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]]). Google limitada por presupuesto; Meta con margen. [Basecamp](https://basecamp.com/1771388/projects/17192035/todos/521039257) |"),
 ("| 21/07/2026 | Radio / audio programático para Madrid (Wiimas, mínimo 3.000 €/mes), septiembre-octubre | 🟡 | Cristian iba a \"revisarlo con calma\". No consta respuesta |",
  "| 21/07/2026 | Radio / audio programático para Madrid (Wiimas, mínimo 3.000 €/mes), septiembre-octubre | 🟡 | Cristian iba a \"revisarlo con calma\". 12/11: Cristian lo recupera como one shot con el remanente; Nina y Ari harán propuesta para la 2.ª-3.ª semana de diciembre |"),
])

# 6. Mercados y canales
edit(K + "Mercados y canales - Barraquer.md", [
 ("- **Pendiente / aplazado**: campañas de competencia; radio (Wiimas); evaluación de continuidad",
  "- **Status 12/11/2026**: según Gemini, quirófano operativo desde el 6 de diciembre y 4 médicos en plantilla (más capacidad que en julio). El CPL de Madrid sube en octubre por competencia (keywords más caras, pérdida de impresiones por presupuesto). Cristian pasará vídeos cortos de los doctores para consideración. Parte del remanente irá a reforzar Madrid; propuesta de radio/audio en diciembre ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]]).\n"
  "- **Pendiente / aplazado**: campañas de competencia; radio (Wiimas); evaluación de continuidad"),
 ("- **Abierto**: pausar o no las campañas de reserva en países nuevos.",
  "- **Status 12/11/2026**: la apertura de términos de marca no ha funcionado mucho; ≈ 3.000 € en awareness, 82 usuarios vieron el vídeo y luego buscaron la marca. Argelia funciona muy bien; Marruecos: visitas presentadas −7,6 %, pero facturación alta. Datos del canal digital de Cristian (transcripción confusa): Mauritania ≈ 31 leads frente a 27, Angola ≈ 30 frente a 24. Ari plantea awareness genérico por patología ([[2026-11-12 - Status RR - remanente, Madrid y contenidos]]).\n"
  "- **Abierto**: pausar o no las campañas de reserva en países nuevos."),
 ("- **Pendiente**: Meta de consideración y PMax genérica en Catalunya (sin creatividades). Saldo bajo (10/2026).",
  "- **Pendiente**: Meta de consideración y PMax genérica en Catalunya (sin creatividades). Saldo bajo (10/2026).\n- **12/11/2026**: pacing un 35 % por debajo del año pasado, con costes un 16 % más bajos; 2k pendientes (PMax). Cristian revisa la propuesta creativa de Estética."),
])

# 7. Personas
edit(K + "Personas - Barraquer.md", [(
"- **Lorena** (equipo de Cristian, contenidos) y **Alex** (audiovisuales): aparecen en la KB web.",
"- **Lorena** (equipo de Cristian: calendario de contenidos, copies, comunidad, reseñas de Google) y **Alex** (audiovisuales): aparecen en la KB web. **Lorena deja Barraquer** (status 12/11/2026); nadie de su equipo puede asumir sus tareas y Ari lo comenta con César por si hay perfiles externos.")])

# 8. Documentos
edit(K + "Documentos - Barraquer.md", [(
"| Informes mensuales (PDF) |",
"| Informe octubre 2026 + RAW data | Informe de la reunión del 12/11 | [Informe](https://drive.google.com/file/d/1HNd-2i6zxCohChaVS-xHXiE9Wig7SdlG/view) · [RAW data](https://drive.google.com/file/d/1FgZs93yO5pGSdmkJnlh41i6NVDdb0yZO/view) |\n"
"| Análisis inversión captación España 2025 vs 2026 | Clínica España (Cataluña + nacional + Madrid), captación vs awareness por mes; nov-dic 2026 son previsión | [Sheet](https://docs.google.com/spreadsheets/d/1tmLMy_j9jKTb3aXfbS3B8K7RayZNCWuyG7KmOt1J5rQ/edit) |\n"
"| Informes mensuales (PDF) |")])

# 9. Log
with open(os.path.join(B, "Claude/Log - Barraquer.md"), "a", encoding="utf-8") as f:
    f.write(f"""
## [2026-11-12] actas | Status RR 12/11 (remanente, Madrid y contenidos)
Acta {ACTA} y transcripción en Raw. Notas de Gemini movidas a 00. Actas reunión. Ingest en Cronología, Propuestas y decisiones, Mercados y canales (Madrid, internacional, Estética), Personas (salida de Lorena) y Documentos (informe de octubre y análisis 2025 vs 2026). Pendientes: 5 tareas nuevas de Runroom y 1 del cliente; cerrada `[x]` "Responder a la propuesta de push de patologías" (aprobado por Cristian en el status); actualizaciones en saldo (Clínica sin saldo), reserva de países nuevos, ROI y creatividades. Mensaje para Basecamp en catalán en 3. Reuniones/Para Basecamp/.

## [2026-11-12] ajustes | Idioma con el cliente
Nina habla con Cristian en catalán: los mensajes al cliente (Basecamp, correos) van en catalán; las actas y el KB, en castellano. Añadido en Tono y estilo.
""")
print("\n".join(errs) if errs else "OK")
