---
fecha: 2026-07-28
cliente: Barraquer
tipo: transcripcion
fuente: https://docs.google.com/document/d/1li6-b3o3leqITXQ6lfmzOpmJaUy9pYNIez0SLWTbOT4/edit
---
<!-- Copia literal del documento de Drive (notas de Gemini + transcripción (documento de Ari); texto extraído de la exportación PDF). No modificar. -->

jul 28, 2026

NEW Barraquer landing definición de eventos GTM
Invitado Nina Gotós Araceli Iglesias Carme Alcoverro Magalí Federico
Roger Vidal
Archivos adjuntos

NEW Barraquer landing - definición de eventos GTM

Notas - NEW Barraquer landing - definición de eventos GTM
Registros de la reunión

Transcripción

Resumen
Reunión sobre configuración técnica y estrategia de visibilidad web para integrar un
nuevo centro médico regional.

Configuración de analítica digital
La estrategia de seguimiento mediante Google Tag Manager fue analizada para alinear
mediciones. Las conversiones reales se contabilizarán únicamente al completar los
formularios externos.

Revisión de página destino
El diseño y el contenido de la página fueron validados satisfactoriamente. Se confirmó
que el formulario de contacto permite diferenciar la procedencia de los usuarios entre
ubicaciones.

Integración de centros médicos
Se decidió actualizar la cabecera, el pie de página y la sección de ubicación para listar
ambos centros. Esta medida unifica la navegación y evita confusiones sobre los
servicios disponibles.

Próximos pasos
 [Roger, Araceli] Revisar eventos y conversiones: Coordinar con Marta la revisión

de eventos y conversiones mediante GTM para asegurar el seguimiento
correcto en Google Ads y Hubspot.
 [Nina] Realizar pruebas de conversión: Ejecutar pruebas de conversión tras la
publicación de la landing para verificar la integración correcta con las campañas
y Hubspot.
 [El grupo] Actualizar navegación web: Incluir la ubicación de Barraquer Madrid
en el sitio web, el encabezado y el pie de página para mejorar la navegación del
usuario.

Detalles
● Configuración de analítica y eventos: Araceli Iglesias señala que la

configuración de eventos y Analytics debe ser gestionada por Marta, quien es la
responsable de realizar estos ajustes técnicos (00:00:02). Roger Vidal presenta
la landing page, y el equipo coincide en la necesidad de alinear la medición de
eventos con Marta antes del lanzamiento (00:01:23). Se acuerda que Roger Vidal
coordinará directamente con Marta a través de un hilo de comunicación para
revisar la implementación mediante Google Tag Manager (GTM) (00:06:47).
● Revisión de la landing page: Roger Vidal muestra la versión actual de la
landing page y confirma que el diseño y el contenido están alineados con las
expectativas de Cristian. Durante la revisión, el equipo observa que la visibilidad
de la asociación ha sido ajustada para ser menos prominente según las
preferencias actuales, y se verifican los elementos visuales como logos y
secciones de patologías (00:02:18).
● Seguimiento de usuarios de Madrid: El equipo discute cómo identificar a los
usuarios que provienen de la nueva landing page de Madrid frente a los de
Barcelona. Se confirma que el formulario de contacto incluye un campo para
seleccionar la ubicación, lo cual permite diferenciar la procedencia del usuario
(00:03:48). Además, se destaca la importancia de mantener las etiquetas UTM

durante la navegación para asegurar que el seguimiento de las campañas de
marketing sea consistente (00:04:24).
● Definición de conversiones y pruebas de validación: Araceli Iglesias aclara
que, aunque el clic en "pedir cita" es un evento relevante para el análisis, la
conversión real se registra únicamente cuando el usuario completa y envía el
formulario de Hubspot. El grupo decide realizar pruebas de conversión
exhaustivas una vez que la landing page esté publicada para verificar que tanto
el seguimiento de campañas como la captura de datos en Hubspot funcionen
correctamente (00:06:47).
● Estrategia de visibilidad en el sitio web principal: Roger Vidal solicita
recomendaciones sobre cómo integrar el nuevo centro de Madrid en la web
principal de Barraquer sin alterar la estructura actual ni generar una
competencia no deseada con el centro de Barcelona (00:08:20). Se determina
que la página de "Ubicación" es el lugar más apropiado y natural para incorporar
la información sobre el centro de Madrid (00:09:54).
● Integración en la navegación y servicios: El equipo analiza posibles
problemas de usabilidad, especialmente relacionados con los servicios de
urgencias, los cuales están disponibles en Barcelona pero no en Madrid
(00:11:28) (00:12:47). Se decide descartar la inclusión del anuncio en la sección
de noticias y, en su lugar, se propone actualizar el encabezado y el pie de página
para diferenciar claramente los centros y evitar confusión en los usuarios
(00:10:38) (00:12:12).
● Acuerdos para los siguientes pasos: El equipo concluye la reunión acordando
implementar cambios en la cabecera, el pie de página y la página de ubicación
para listar tanto a Barraquer Barcelona como a Barraquer Madrid (00:14:10).
Roger Vidal se encargará de gestionar los detalles técnicos con Marta, con la
ayuda de Araceli Iglesias para definir el contexto, con el objetivo de agilizar el
proceso sin involucrar a más personas de las necesarias (00:07:45).

Revisa las notas de Gemini para asegurarte de que sean precisas. Obtén sugerencias y
descubre cómo Gemini toma notas
Cómo es la calidad de estas notas específicas? Responde una breve encuesta para
darnos tu opinión; por ejemplo, cuán útiles te resultaron las notas.

jul 28, 2026

NEW Barraquer landing definición de eventos GTM Transcripción
00:00:02
Nina Gotós: Estupendo.
Araceli Iglesias: español. Sí,
Magalí Federico: Bien.
Araceli Iglesias: vale. Nos queda la karma.
Roger Vidal: A ver, ahora enter lo se atraviza el calendario y está mirando al canal. A
ver, le paso.
Araceli Iglesias: Ah.
Magalí Federico: Venga.
Araceli Iglesias: Hola. Hola. Venga, vale. Venga, pues vamos entonces. Hm. la yo, o
sea, no sé cómo empezar esto. Si os parece, yo empiezo diciéndolos lo que hay y a
partir de ahí vemos, ¿vale? Eh, y nos explicaráis vosotros lo de la landing.
Roger Vidal: Vale.
Araceli Iglesias: O sea, nosotros a nivel de conversión, para que lo sepáis, o sea, se
trabaja de dos maneras. Uno, lo que haya configurado, que es que igual en esta
conversación tendría que estar Marta, eh, a nivel de eventos y demás. Hm. Pienso,
Nina, porque nosotros no configuramos nada de Analytics,
Nina Gotós: Ya queréis que intente intente meter
Araceli Iglesias: lo configura Marta. A ver si le puedes robar un

00:01:23
Roger Vidal: O quizás primero podemos mirar la landing y ver realmente qué hay por
allí,
Araceli Iglesias: Sí,
Roger Vidal: porque quizás todo es muy genérico, ¿no? Es que la landing es muy
Araceli Iglesias: claro,
Roger Vidal: chorras.
Araceli Iglesias: pero aunque sean muy chorras, hay que decidir cómo la cómo la
medimos, digamos,
Roger Vidal: Sí, sí. O sea,
Araceli Iglesias: ¿sabes?
Roger Vidal: sí, pero digo eso, si antes de Marta, si quizás alinear nosotros un
momento y quizás solo para Marta es una cosita o dos.
Araceli Iglesias: Puede ser. Vale.
Roger Vidal: Mira,
Araceli Iglesias: No sé, o sea,
Roger Vidal: te enseño,
Araceli Iglesias: la configuración de los eventos la hace Marta siempre,
Roger Vidal: os enseño un momento.
Araceli Iglesias: eh, lo digo por
Roger Vidal: Vale, aquí barra que es esta.
Araceli Iglesias: eso.
Roger Vidal: No tengo claro si ahora que si estaré con es que estoy con una pantalla
grande y no sé si Vale, sí, en principio sí que estoy compartiendo la landing, ¿no?
Araceli Iglesias: Sí.
Roger Vidal: Vale,
Magalí Federico: Sí.
Roger Vidal: pues básicamente no es esta landing a esta punta espiritiva aquí eso
huele, ¿no? A queremos medir cuánta gente clica al pedir cita.

00:02:18
Roger Vidal: Eso sí que algo se huele por aquí.
Araceli Iglesias: Un Vale,
Roger Vidal: principio. Sí,
Araceli Iglesias: vamos a medir los eventos. Esto lo ha visto Cristian ya.
Carme Alcoverro: Mhm.
Araceli Iglesias: Ah, vale.
Roger Vidal: sí,
Araceli Iglesias: No hemos puesto el nombre del hospital a posta o algo así.
Carme Alcoverro: Igual
Roger Vidal: no hemos puesto el nombre del hospital a post
Araceli Iglesias: Ah, memoria del público. Cordón. Vale, es que estoy en chiquitín.
Vale, vale,
Roger Vidal: aquí,
Araceli Iglesias: no lo había visto. Vale,
Roger Vidal: o sea,
Araceli Iglesias: vale.
Roger Vidal: lo estamos terminando aún,
Carme Alcoverro: tienes que hacerle,
Roger Vidal: ¿eh? Pero en principio, hasta aquí, hasta lo que hay ahora, estamos
alineados con Cristian.
Araceli Iglesias: Sí,
Carme Alcoverro: pero no se actualizado.
Araceli Iglesias: igual.
Carme Alcoverro: que seetea
Araceli Iglesias: Ah, vale.

Carme Alcoverro: fuerte,
Roger Vidal: fuerte.
Araceli Iglesias: Es que recuerdo que él quería como que hiciésemos el partnership
que se viese bien y ahora a simple vista no lo he visto.
Carme Alcoverro: No, es que ya no quiere que se vea tanto,

00:03:00
Araceli Iglesias: Ah,
Carme Alcoverro: en plan se ve como más abajo.
Magalí Federico: Ok.
Araceli Iglesias: okay. Vale, vale,
Roger Vidal: Ahora Carma está la última versión en principio.
Carme Alcoverro: Sí, sí,
Roger Vidal: Vale,
Araceli Iglesias: vale, vale,
Roger Vidal: ahora sí.
Carme Alcoverro: sí.
Araceli Iglesias: vale.
Roger Vidal: Entonces aquí vídeos ya tenemos que ahora vemos dónde irá.
Araceli Iglesias: Pedir cita.
Roger Vidal: Aquí un poco de cifras
Carme Alcoverro: Aquí aparece el logo del del otro
Magalí Federico: Ah,
Roger Vidal: aquí.
Magalí Federico: vale.
Carme Alcoverro: hospital.
Magalí Federico: Ah.

Roger Vidal: Luego aquí las patologías.
Araceli Iglesias: Vale.
Roger Vidal: Aquí quizás no sé si bueno que esto en principio ya lo medimos porque
esto no es un evento, esto simplemente no es caminar por la página básicamente a la
página de
Araceli Iglesias: O sea, no sé dónde te lleva eso.
Roger Vidal: barra que estamos dentro del mismo dominio. Ahora aquí se ha puesto la
de Prod y si clico me llegará prod.
Araceli Iglesias: Pero y si sí, pero si alguien de Madrid convierte en glaucoma,
Roger Vidal: Pero
Araceli Iglesias: ¿cómo sé yo que viene de Madrid?
Roger Vidal: si alguien de Madrid convierte en Guca, o sea, si viene aquí,

00:03:48
Araceli Iglesias: Si pide cita aquí, ¿cómo sabemos que es de Madrid?
Roger Vidal: aquí
Magalí Federico: en el formulario. había agregado un campo de de
Araceli Iglesias: Pues no lo
Roger Vidal: viita motivo.
Magalí Federico: lo más
Araceli Iglesias: sé.
Roger Vidal: Claro, aquí no lo sé eso, pero estes formularios se pueden apuntar a
Madrid.
Magalí Federico: abajo.
Carme Alcoverro: Claro,
Araceli Iglesias: A ver,
Carme Alcoverro: es o en la serie tú pones o
Magalí Federico: C en CD

Roger Vidal: Ah,
Araceli Iglesias: CD,
Roger Vidal: mira aquí.
Araceli Iglesias: CD. Ah, vale, vale. Sí que lo ha añadido.
Carme Alcoverro: Barcelona,
Araceli Iglesias: Okay, vale. O sea,
Roger Vidal: Vale,
Araceli Iglesias: ahí si clicas Madrid ya está perfecto. Pues ya está.
Roger Vidal: vale.
Araceli Iglesias: Vale, a ver,
Magalí Federico: Tô
Carme Alcoverro: pero bueno,
Araceli Iglesias: Barraque.
Carme Alcoverro: no sabrá si viene de Stalanding o de dónde viene.
Araceli Iglesias: Claro, aquí hay una cosa importante también, ¿no? Claro, no sabrá,
pero bueno. Bueno,

00:04:24
Carme Alcoverro: Da
Araceli Iglesias: si eso está claro también que, o sea, nosotros vamos a aterrizar las
campañas aquí,
Carme Alcoverro: igual.
Araceli Iglesias: pero luego un usuario puede haberlo visto hoy y convertir al día
siguiente, buscar barraque y convertir por la web principal. O sea, que eso también no
es tan importante, h no es tan importante saber qué convierte como de dónde ha
convertido exactamente.
Roger Vidal: C

Araceli Iglesias: Pero lo que sí que que sí que pienso es el tema de entiendo que esta
landing funciona con toda la lógica de programación del resto de la web.
Roger Vidal: Sí,
Araceli Iglesias: ¿Me explico?
Roger Vidal: está todo
Araceli Iglesias: Vale, o sea, por ejemplo,
Roger Vidal: dentro.
Araceli Iglesias: si enviamos esta landing con UTMs, las va a arrastrar si navega a
otras partes de la web,
Roger Vidal: Lo tenemos lo tenemos que comprobar bien,
Araceli Iglesias: ¿no?
Roger Vidal: pero en principio sí. En principio también lo típico de GTM,
Araceli Iglesias: Vale,
Roger Vidal: de scroll y todo eso, o sea, literal es la misma web. Lo único que hemos
hecho,
Araceli Iglesias: vale, vale.
Roger Vidal: hemos pintado encima.
Araceli Iglesias: Una landing nueva. Vale,
Roger Vidal: Sí.
Araceli Iglesias: perfecto.

00:05:09
Araceli Iglesias: Genial.
Roger Vidal: Vale, aquí tengo esto. Aquí unos señores que aquí también hay lo mismo.
Araceli Iglesias: Vale. Sí,
Roger Vidal: Esto lleva también la vuelta de barraqu.
Araceli Iglesias: también se convierte la gente convierte bastante en doctores.
Roger Vidal: Vale,

Araceli Iglesias: Estos son todos de Madrid,
Roger Vidal: pasamos aquí.
Araceli Iglesias: supongo. Claro.
Roger Vidal: Entendemos que sí.
Carme Alcoverro: Mhm.
Roger Vidal: Ah,
Araceli Iglesias: Sí.
Roger Vidal: pellecitas del mismo.
Araceli Iglesias: Bueno,
Roger Vidal: Ah, nada, nada. ¿Cómo llegar?
Araceli Iglesias: y el teléfono también.
Roger Vidal: No sé si queremos leer
Araceli Iglesias: Sí,
Roger Vidal: y aquí el formulario y ya
Araceli Iglesias: vale.
Magalí Federico: Bien.
Araceli Iglesias: O sea,
Roger Vidal: está.
Araceli Iglesias: las conversiones a priori son las mismas. Esto sí que habría que
pedirle a Marta que revise todo. Es decir, por ejemplo, en pedir cita,
Roger Vidal: Hm.
Araceli Iglesias: nosotros en la cuenta de barraque tenemos una que es first apoy. si
no me equivoco. O sea, esa conversión de Google Ads tendría que estar seteada
cuando pides cita
Magalí Federico: Sí.

00:06:05
Araceli Iglesias: aquí.

Roger Vidal: Vale,
Araceli Iglesias: O sea, yo no sé,
Roger Vidal: o sea,
Araceli Iglesias: eso entiendo que es Marta quien lo tiene que revisar porque esto lo
tiene que lo tiene que mirar con
Roger Vidal: esper,
Araceli Iglesias: GTM.
Roger Vidal: vale, pues sí, supongo que sí, porque a mí también me hablas un poco
chino en este sentido.
Araceli Iglesias: Claro,
Roger Vidal: Ah, vale. Entonces, o sea,
Araceli Iglesias: claro.
Roger Vidal: ¿cómo lo hacemos? Porque esto, claro,
Nina Gotós: No.
Roger Vidal: realmente esto y eso sí lo del hotspot lo va aparte, ¿no? O sea, yo que sé,
o sea,
Araceli Iglesias: Esto es un form de Hubspot,
Roger Vidal: lo que
Araceli Iglesias: entiendo. Si todos los forms de barraque son de Hubspot,
Roger Vidal: sí,
Araceli Iglesias: ¿no? Eh, sí,
Carme Alcoverro: M.
Araceli Iglesias: sí. Esto en teoría si entran con UTMs y demás tiene que funcionar.
Roger Vidal: no sé si para funciona.
Araceli Iglesias: que hacer alguna prueba de conversión, pero vamos,
Roger Vidal: Vale,
Araceli Iglesias: debería entrar todo bien.
Roger Vidal: vale,
Araceli Iglesias: O sea,
Roger Vidal: guay.

00:06:47
Araceli Iglesias: yo aquí Nina cuando esté la landin ya publicada y la previsión de
lanzar sí que habría que hacer pruebas de conversión para entender que entra todo
bien en Hubspot, el niming de campaña y todo, pero la revisión de los eventos
concretamente, yo creo que lo tiene que hacer Marta,
Roger Vidal: Vale.
Araceli Iglesias: que esté todo trackado porque para explicaros un poco, las
conversiones principales de Google Ads se miden poniendo el tac, una vez el usuario
ha enviado el formulario rellenado, la ha enviado, se guarda toda la información, se
envía, ahí tiene que saltar el código de Google Ads. Vale, el resto de conversiones
debería funcionar con el tag de analytics, o sea, por ejemplo, el clic a pedir cita para
nosotros no es una conversión,
Roger Vidal: Vale,
Araceli Iglesias: es un click.
Roger Vidal: no es simplemente para saber cuánta G es un
Araceli Iglesias: Exacto, exacto. ¿Cuánta gente lo hace y luego no acaba convirtiendo
Roger Vidal: lockman la conversión real sería lleno el
Araceli Iglesias: formulario?
Roger Vidal: formulario de HSP, ¿no? Y aquí nosotros queremos saber si lo ha llenado a
través de un Google Ads o lo ha llenado por orgánico.
Araceli Iglesias: Por otra campaña o por lo que sea. Sí,
Roger Vidal: Vale, vale.
Araceli Iglesias: eso lo dirán las UTMS de campaña,

00:07:45
Roger Vidal: Bueno,

Araceli Iglesias: digamos.
Roger Vidal: vale. Ah,
Araceli Iglesias: Vale.
Roger Vidal: pues entiendo que se lo podemos pedir a Marta y me puedo poner yo
con ella y lo miro para no estar cinco personas con Marta,
Araceli Iglesias: Sí,
Roger Vidal: ¿no?
Araceli Iglesias: sí, sí,
Roger Vidal: O sea,
Araceli Iglesias: sí. que si nos necesitáis para cualquier cosa así, o sea, Marta sabe
que la se le puedo poner,
Roger Vidal: vale.
Araceli Iglesias: o sea, si quieres me pones en copia,
Roger Vidal: Sí, exacto. Hacemos un miniilo allá de hacer cuatro cosas.
Araceli Iglesias: le digo las Sí,
Roger Vidal: Yo con Marta ya he mirado un montón de cosas, o sea, tenemos bastante
trato,
Araceli Iglesias: vale,
Roger Vidal: así que que está bastante
Araceli Iglesias: vale, vale. Genial. Sí, pues es eso que simplemente revisar vía GTM,
Roger Vidal: bien.
Araceli Iglesias: que darle acceso en tienda hasta landing, que ya pueda revisar que
todo está correcto, que entiendo que si es la misma configura de la acción de la web
no había,
Roger Vidal: Debería, o sea, que no haya un error,
Araceli Iglesias: no debería haber problema sobre todo a mí me interesa el tema de la
navegación porque como tiene

00:08:20
Roger Vidal: todo está poco.
Araceli Iglesias: mucho punto de fuga en el sentido de que puede clicar muchas
patologías,
Magalí Federico: Ev.
Roger Vidal: Mm.
Araceli Iglesias: eso va a ser importante.
Roger Vidal: Vale. Y otra cosa que nos pidió ayer Cristian a Karma y a mí y quizás esto
nos podéis ayudar más vosotras es el tema de que nos he dicho, "Vale, aparte de que
vamos a hacer campañas, vamos a ponerlo en LinkedIn, bla bla bla bla bla, molaría en la
web algún sitio para llegar aquí. ¿Vosotros tenéis alguna idea con este hijo?
Araceli Iglesias: Mhm.
Roger Vidal: Como vosotros como consultores, ¿dónde lo pondríais?" Eso la típica
pregunta de Cristian que él quiere, o sea, digo, no sé, o sea, dijimos, nos lo vamos a
pensar.
Araceli Iglesias: Ah. Hombre, yo creo que que tendría que ser como un ban, o sea, la
cabecera no la tocaría,
Roger Vidal: Vale, o sea, él dijo,
Araceli Iglesias: yo pienso,
Roger Vidal: él su idea fue en plan, aquí no,
Araceli Iglesias: ¿eh?
Roger Vidal: pero él aquí no lo veía tan raro meterlo en este pequeño de aquí arriba.
Yo mirándolo, o sea, no cuadra nada de lo que hay, en plan,
Araceli Iglesias: Hombre,

00:09:14

Roger Vidal: no parece que hay nada de centros ni nada,
Araceli Iglesias: a mí no ahí,
Roger Vidal: pero mira,
Araceli Iglesias: pero puedes ponerte en la versión castellano porque no sé si es la
misma.
Roger Vidal: sí, espera, mira, me entro a barraque real porque aquí como hay pruebas,
Araceli Iglesias: Ah, barra que sí. Ahora vale.
Roger Vidal: mira aquí no.
Araceli Iglesias: ¿Sabes que el centro? Si clicas el centro que son centros, los centros,
¿no? Eso tendríamos que actualizarlo,
Roger Vidal: Sí, sí,
Magalí Federico: IG
Araceli Iglesias: ¿no?
Roger Vidal: pero aquí precisamente lo dijimos y él él sí que dijo que no quería
meterlo en el en el principal porque tampoco quería competencia en plan
Araceli Iglesias: Bueno,
Roger Vidal: de oye que de repente el de Madrid te más importante de Barcelona
porque si no tenemos que desarrollar todo para el resto de
Araceli Iglesias: ya mutuas,
Roger Vidal: centros.
Araceli Iglesias: ubicación o yo que sé.
Magalí Federico: Ubicación y contacto. Claro, ahí está solo el de Barcelona, ¿no? Si
cliqueas ahí arriba.
Araceli Iglesias: Claro,
Roger Vidal: ¿Dónde?
Magalí Federico: ubicación.
Araceli Iglesias: en en ubicación y contacto.
Roger Vidal: Contacto.
Araceli Iglesias: Claro,

00:09:54
Roger Vidal: A ver,
Magalí Federico: aparece ahí Madrid todavía y no creo que va a aparecer tampoco,
Araceli Iglesias: aquí solo Barcelona,
Roger Vidal: vamos a centro. Sí.
Araceli Iglesias: ¿no? Yo creo que aquí es un sitio donde les diríamos que tendrían
que actualizar y poner pues igual que tenemos la ubicación de
Magalí Federico: ¿no?
Araceli Iglesias: Barcelona,
Carme Alcoverro: No.
Araceli Iglesias: poner el partnership con público don en Madrid, sobre todo es que
vamos a estar es que puede decir es que no quiero darle prioridad, es que ya le estás
dando prioridad, estás creando una landing con navegación y haciendo campañas,
entonces la gente va a venir aquí seguro. Es un poco raro que en la web no aparezca
Madrid, por mucho que tú no quieras.
Magalí Federico: Yo lo añadiría acá segmento nuevo,
Araceli Iglesias: Yo también aquí seguro.
Roger Vidal: Vale,
Magalí Federico: ¿no?
Roger Vidal: en ubicación añadir.
Araceli Iglesias: Sí,
Roger Vidal: Vale,
Araceli Iglesias: sí.
Roger Vidal: luego lo que sí que nos dije que obviamente aparte de las cosas que
hiciese que se Linken, etcétera,
Magalí Federico: Mo.
Roger Vidal: sí que iba a crear una noticia un poco así bonita dando que eso ahí
Araceli Iglesias: Yo no entraría jamás en la sección de

00:10:38
Roger Vidal: dentro.
Araceli Iglesias: noticias.
Roger Vidal: A ver, quizás a ver si hay suerte.
Araceli Iglesias: Claro, yo haría un banner tipo ese,
Roger Vidal: Ah, mira,
Carme Alcoverro: destacadas
Roger Vidal: aquí aparecerá aquí.
Araceli Iglesias: ¿no?
Carme Alcoverro: aquí.
Araceli Iglesias: Tú me dirás, yo haría un banner tipo esto, ¿no? Eh, nuevo, nueva
colaboración, público, no sé hasta cuándo,
Roger Vidal: por aquí el medio en algún
Araceli Iglesias: pero ponerlos. ¿Sabes? Es claro,
Carme Alcoverro: No sé si lo va a querer destacar tanto,
Araceli Iglesias: porque si tú clicas pues que no,
Carme Alcoverro: eh, me da la sensación de que
Roger Vidal: sitio.
Araceli Iglesias: pero es verdad que a nivel usuario,
Carme Alcoverro: no.
Araceli Iglesias: si tú tienes toda la web que vende Barcelona y navegas,
Magalí Federico: No.
Araceli Iglesias: te vuelves al, o sea, si tú entras en la landing que nos habéis
enseñado,
Roger Vidal: Hm.
Araceli Iglesias: te vas a Oftalmología, por ejemplo, o de, no sé, Flaroplastia, te vas a
farloplastia y luego clicas en el logo, no te va a ir a Madrid, te va a ir a la web de
Barcelona.

00:11:28
Araceli Iglesias: Entonces, h, o sea, de alguna manera habría que integrarlo mejor.
Claro, te vienes aquí, luego te viene aquí. ¿Dónde?
Roger Vidal: y te vuelves aquí que yo lo he perdido.
Araceli Iglesias: Ay, ¿dónde está lo de Madrid? No, pero aquí no lo ves. Claro.
Carme Alcoverro: Mhm.
Roger Vidal: Hm.
Araceli Iglesias: Vale, el centro es
Magalí Federico: ubicación contacto seguro y después proponerlo lo del segmento,
Araceli Iglesias: okay.
Magalí Federico: pero probablemente si no lo quiere destacar
Araceli Iglesias: Claro. Pero bueno, a mí me parece un poco raro como usuario de
Madrid volver aquí atrás y no saber cómo volver a la clínica de Madrid. Madrid. No es
que es que
Roger Vidal: Sí,
Magalí Federico: Abajo de todo tenía como ahí en esta parte
Araceli Iglesias: igual ya, pero aquí abajo de todo.
Magalí Federico: igualarlo.
Roger Vidal: aquí tal decía aquí en secciones que diría que esto de secciones es lo
mismo que aparece.
Carme Alcoverro: Sí.
Araceli Iglesias: Sí,
Roger Vidal: Ah, no, es lo mismo aquí. Ah, no, no es lo
Magalí Federico: No, no es lo
Araceli Iglesias: porque otra opción, a ver qué os parece.

00:12:12
Roger Vidal: mismo.
Araceli Iglesias: Si en la parte de arriba de todo,
Magalí Federico: mismo.
Araceli Iglesias: claro, esto mobile no sé cómo se ve, pero en la parte de arriba de
todo donde pone el teléfono, urgencias y tal. Claro, es que teléfono, que teléfono.
Roger Vidal: Sí,
Araceli Iglesias: Eso es el teléfono de Barcelona.
Roger Vidal: mira esto.
Carme Alcoverro: Sí.
Roger Vidal: XR.
Magalí Federico: Sí.
Roger Vidal: Esto se ve aquí.
Araceli Iglesias: Si clicas a la hamburguesa.
Roger Vidal: Es esto de aquí. Si no es esto de aquí.
Araceli Iglesias: No,
Roger Vidal: No,
Araceli Iglesias: no,
Roger Vidal: no es esto tampoco.
Araceli Iglesias: eso no está en la versión mobile,
Roger Vidal: Ah, no es tanto ese mod.
Araceli Iglesias: ¿no? Ah,
Carme Alcoverro: Sí que está porque es lo de teléfono,
Araceli Iglesias: mira. Sí, sí, mira. Ahí,
Carme Alcoverro: urgencias, o sea, se queda,
Araceli Iglesias: ahí.
Carme Alcoverro: se divide, hay una parte que se ve fuera y una que se ve
Roger Vidal: Ah, una parte fuera y una parte dentro.

Araceli Iglesias: Urgencias,
Carme Alcoverro: dentro.

00:12:47
Roger Vidal: Vale,
Araceli Iglesias: teléfono. O sea, ya vale. O sea, yo creo que de alguna manera, claro,
Roger Vidal: claro.
Araceli Iglesias: urgencias, cuando clicas a urgencias te va a llevar a Barcelona. Es que
en Madrid también van a tener urgencias,
Roger Vidal: Atendemos y vamos con ubicación
Carme Alcoverro: que no tengo claro e lo que van a tener
Magalí Federico: No sé,
Araceli Iglesias: ¿sabes?
Roger Vidal: Barcelona.
Magalí Federico: porque en Madrid es más pedir cita que quiere o no sé si son
Carme Alcoverro: solo Madrid es solo cita y no
Magalí Federico: urgencias.
Araceli Iglesias: Ya, vale,
Carme Alcoverro: va por mutua ni nada es como y solo tienen dos médicos,
Araceli Iglesias: vale,
Carme Alcoverro: o sea, no creo que haya urgencias,
Magalí Federico: Claro,
Araceli Iglesias: vale. Saur, urgencias.
Carme Alcoverro: pero si está claro que no se entiende si puede ver de urgencias a
Madrid,
Araceli Iglesias: Nada.
Carme Alcoverro: o sea,

Magalí Federico: claro.
Araceli Iglesias: Claro, se tú llamas, de repente te sale un bulto en el ojo, yo que sé.
Roger Vidal: Hm. Yeah.

00:13:23
Araceli Iglesias: Vale, voy a buscar si yo te estoy captando. Se me hace raro que no
me atienda,
Carme Alcoverro: No.
Araceli Iglesias: ¿sabes? Pero bueno, vale. Okay. Pongamos que urgencias solo son en
Barcelona. Igual podríamos poner urgencias Barcelona. Es que no sé, ¿sabes?
Magalí Federico: Ah,
Araceli Iglesias: Hm. No sé.
Roger Vidal: Ja.
Araceli Iglesias: Igual esto hay que hay que ver a ver qué tal funciona con el
lanzamiento de Madrid. De todos modos,
Magalí Federico: bueno.
Araceli Iglesias: igual aquí arriba podríamos poner Barraquer Barcelona, Barraquer
Madrid. ¿Sabes que si clicas Barra Barcelona te lleva la original? Si clicas barraque
Madrid puedas volver de alguna manera. a la landing que hemos visto, ¿sabes?
Roger Vidal: Aquí te imaginas donde
Araceli Iglesias: No sé. Sí,
Roger Vidal: l aquí
Araceli Iglesias: o sea, en el futero oscurito, digamos,
Roger Vidal: ya es todo.
Carme Alcoverro: o realmente solo Barraque Madrid,
Araceli Iglesias: porque ya sí,
Carme Alcoverro: porque Barraque Barcelona ya es

00:14:10
Araceli Iglesias: sí, es todo. Barraquer Madrid. Sí, podríamos poner Barraquel
Magalí Federico: Sí, en ese y en el de abajo,
Araceli Iglesias: Madrid
Magalí Federico: ya que
Roger Vidal: Está sí o sí.
Araceli Iglesias: en el Foter, ¿no?
Carme Alcoverro: Si en el footer
Roger Vidal: Aquí sí,
Araceli Iglesias: Algo así.
Roger Vidal: aquí es
Magalí Federico: Hm.
Roger Vidal: fácil.
Araceli Iglesias: O sea,
Carme Alcoverro: Ok.
Araceli Iglesias: que también podemos ver una vez lancemos, yo también lo que le
diría que es que una vez lancemos también podemos ver cuál es el comportamiento
natural de los usuarios navegando. Si vemos cosas como yo clico mucho al logo, pues
hay que integrar de alguna manera Madrid de una forma que esté más integrado en
todo el contexto de Barraquer, ¿no? Pero bueno, ahora de momento podemos hacer
así como los mínimos, o sea, como algo higiénico para que la gente por lo menos no se
pierda. Si si navega en la web de Barrqueer no.
Magalí Federico: Hm.
Roger Vidal: Sí, sí, makes sense.
Araceli Iglesias: O sea,
Roger Vidal: Vale,
Araceli Iglesias: vale. Entonces, hemos dicho aquí en el en el de arriba poner
barraque Madrid por si el usuario navega,

00:15:03
Roger Vidal: que sean estas de aquí en la
Araceli Iglesias: en el footer también y en ubicación, ¿no?
Roger Vidal: ubicación.
Araceli Iglesias: Poner un nuevo barraque en Madrid,
Roger Vidal: Exacto.
Araceli Iglesias: no sé qué, Fublio Cordón, no sé qué y enviar landing ahí.
Roger Vidal: Sí, ya dónde estaba la ubicación, pero sí.
Araceli Iglesias: Igual ahí en ubicación se puede poner sin urgencias o sabes,
Magalí Federico: Arriba.
Araceli Iglesias: o sea, igual hay que ser un poco específico también.
Roger Vidal: Hm. Ah. Sí, sí, claro. Aquí centro estalmólico con servicio de urgencias y
el otro
Araceli Iglesias: Claro, Barragué, aquí se puede decir urgencias, eh, visitas médicas,
etcétera,
Roger Vidal: sí.
Araceli Iglesias: y en la de Madrid poner visitas médicas solo o no especificar,
Magalí Federico: Claro.
Araceli Iglesias: yo que sé, algo así, no sé. Es que es un poco anacrónico todo, ¿no?
Roger Vidal: Sí, sí, sí. O sea,
Araceli Iglesias: Anaónico, no,
Roger Vidal: si la pongo por ahí.
Carme Alcoverro: Hm.
Araceli Iglesias: macarrónico.
Roger Vidal: Vale, guay. Vale,
Araceli Iglesias: Vale, pues es todo lo que se me ocurre.

Roger Vidal: pues tiramos con eso y siguientes steps hacemos eso,
Araceli Iglesias: Vale,
Roger Vidal: creamos un hilo, involucramos a a Marta, tú, Ari, si puedes haces un poco
la intro de lo que esperamos de Marta y luego ya pues si me puedo poner yo con ella y
ya está y así no
Araceli Iglesias: sí, claro. Vale,
Roger Vidal: estamos cinco personas.
Araceli Iglesias: genial. Perfecto.
Roger Vidal: S. Bueno,
Araceli Iglesias: Pues seguimos.
Carme Alcoverro: Volve. Gracias.
Araceli Iglesias: Merc.

La transcripción finalizó después de 00:16:27
Esta transcripción editable se generó por computadora y puede contener errores. Los
usuarios también pueden cambiar el texto después de que se cree.
