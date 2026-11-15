from comun import *

ROSA = colors.HexColor("#6A4C93")


def ascolta(items):
    s = [sec("Da ascoltare e da vedere")]
    s += tabla([["Tipo", "Qué", "Por qué"]] + items, [22, 58, 90])
    return s


ASCOLTA = {
1: [["Canción", "<b>Ciao ciao</b> — La Rappresentante di Lista (Sanremo 2022)", "Repite <i>ciao</i> en todos los tonos: saludo y despedida."],
    ["YouTube", "Canal <b>Easy Italian</b>", "Entrevistas en la calle con subtítulos en italiano. Buscá videos donde la gente se presenta."],
    ["YouTube", "Canal <b>Learn Italian with Lucrezia</b>", "Videos cortos de alfabeto, pronunciación y saludos."]],
2: [["Canción", "<b>L'italiano</b> — Toto Cutugno (1983)", "El estribillo es puro <i>essere</i>: <i>\"sono un italiano, un italiano vero\"</i>."],
    ["Película", "<b>La vita è bella</b> — Roberto Benigni (1997)", "Clásica, y la primera parte tiene muchas presentaciones y saludos. Ganó el Oscar a mejor película extranjera."]],
3: [["Canción", "<b>50 Special</b> — Lunapop (1999)", "Sobre andar en Vespa por las colinas de Bologna: <i>\"...se hai una Vespa Special\"</i> (con <i>avere</i>)."],
    ["Película", "<b>Vacanze romane</b> (<i>Roman Holiday</i>, 1953)", "Audrey Hepburn y Gregory Peck recorren Roma en Vespa. Está en inglés, pero es la escena más famosa de la Vespa."]],
4: [["Película", "<b>Pane e tulipani</b> — Silvio Soldini (2000)", "Una mujer se queda sola en Venecia: conversaciones cotidianas, formales e informales."],
    ["YouTube", "Buscá <i>\"Canal Grande vaporetto\"</i>", "Recorridos en vaporetto por el Canal Grande: el Ponte di Rialto y San Marco de la Lettura."]],
5: [["Canción", "<b>Piazza Grande</b> — Lucio Dalla (1972)", "Dalla era de Bologna. Letra lenta y clara, con muchos verbos en presente."],
    ["Canción", "<b>Bologna</b> — Francesco Guccini (1981)", "Un retrato de la ciudad de la Lettura."],
    ["Práctica", "Contá del 20 al 100 de 10 en 10, y después de 7 en 7", "Para fijar los números: <i>ventuno, ventotto, trentacinque...</i>"]],
6: [["Película", "<b>La classe operaia va in paradiso</b> — Elio Petri (1971)", "La vida de Lulù, un <i>operaio</i> en una fábrica. Palma de Oro en Cannes, 1972."],
    ["Película", "<b>Ferrari</b> — Michael Mann (2023)", "Enzo Ferrari en Modena, en 1957. Está en inglés, pero muestra la Motor Valley de la Lettura."]],
7: [["Canción", "<b>Nel blu dipinto di blu (Volare)</b> — Domenico Modugno (1958)", "Modugno era de Polignano a Mare, en Puglia; ahí tiene una estatua. Una de las canciones italianas más famosas del mundo."],
    ["Película", "<b>Mine vaganti</b> — Ferzan Özpetek (2010)", "Una familia con una fábrica de pasta en Lecce: trabajo, familia y Puglia."]],
8: [["Canción", "<b>Via con me</b> — Paolo Conte (1981)", "Juego de palabras: acá <i>via</i> no es \"calle\" sino \"lejos\" (<i>vieni via con me</i> = vení conmigo, vámonos)."],
    ["Película", "<b>Il postino</b> — Michael Radford y Massimo Troisi (1994)", "Un cartero de una isla del sur lleva las cartas a Pablo Neruda: direcciones, conversaciones y mucho italiano lento y claro."],
    ["Práctica", "Decí en voz alta tu dirección, tu mail y tu número", "<i>Abito a Córdoba, in via... · ...chiocciola gmail punto com · tre – cinque – uno...</i>"]],
}


def ejercicios(items):
    s = [sec("Mettiti alla prova")]
    s += [Paragraph(q, B, bulletText=f"{i+1}.") for i, (q, a) in enumerate(items)]
    s += [Paragraph("<i>Soluciones al final de la carpeta.</i>", INFO)]
    return s


ESERCIZI = {
1: [("Completá: <i>Come ti ____? — Mi ____ Luca.</i>", "chiami · chiamo"),
    ("Preguntá el nombre en forma formal.", "Come si chiama?"),
    ("Escribí en letras: 7 · 13 · 18 · 20.", "sette · tredici · diciotto · venti"),
    ("¿Qué saludo usás a las 23 h para ir a dormir? ¿Y al llegar a una oficina a las 10 h?", "Buonanotte · Buongiorno"),
    ("Deletreá <i>Roma</i> y tu apellido.", "erre – o – emme – a"),
    ("Completá: <i>noi ci ____ · loro si ____</i>.", "chiamiamo · chiamano")],
2: [("Completá con <i>essere</i>: <i>Io ____ argentino. Tu ____ di Roma? Lei ____ inglese.</i>", "sono · sei · è"),
    ("Pasá al femenino: italiano · francese · tedesco · cinese.", "italiana · francese · tedesca · cinese"),
    ("Hacé negativa: <i>Sono spagnolo.</i>", "Non sono spagnolo."),
    ("¿<i>e</i> o <i>è</i>?: <i>Paolo __ Vito · Vito __ di Firenze.</i>", "e · è"),
    ("Corregí: <i>Sono di Italia.</i>", "Sono italiano / italiana."),
    ("¿Cómo suenan? <i>cena · chiamo · gelato · spaghetti · famiglia · pesce</i>",
     "\"chena\" · \"kiamo\" · \"yelato\" · \"spaguetti\" · \"famiglia\" (gli ≈ ll de España) · \"peshe\"")],
3: [("<i>un / uno / una / un'</i>: __ zaino · __ penna · __ agenda · __ libro · __ studente · __ amica.", "uno · una · un' · un · uno · un'"),
    ("Completá con <i>avere</i>: <i>Io ____ un quaderno. Tu ____ una penna? Marco ____ uno zaino.</i>", "ho · hai · ha"),
    ("¿Masculino o femenino? chiave · lezione · matita · dizionario · studente.", "f · f · f · m · m"),
    ("Traducí: <i>No tengo un diccionario.</i>", "Non ho un dizionario."),
    ("¿Por qué <i>ho</i> lleva h si no suena?", "Para distinguirlo de <i>o</i> (o).")],
4: [("Pasá a formal: <i>Come ti chiami? · Di dove sei? · Hai un documento? · Puoi ripetere?</i>",
     "Come si chiama? · Di dov'è? · Ha un documento? · Può ripetere?"),
    ("Femenino: attore · scrittore · direttore.", "attrice · scrittrice · direttrice"),
    ("En el hotel: \"Tengo una reserva\".", "Ho una prenotazione."),
    ("¿Qué se responde a <i>Grazie</i>?", "Prego."),
    ("¿Qué diferencia hay entre <i>il foglio</i> y <i>la foglia</i>?", "il foglio = hoja de papel · la foglia = hoja de árbol")],
5: [("Conjugá: io (parlare) · tu (studiare) · lei (abitare) · tu (cercare) · tu (pagare).", "parlo · studi · abita · cerchi · paghi"),
    ("Escribí: 21 · 38 · 43 · 77 · 100.", "ventuno · trentotto · quarantatré · settantasette · cento"),
    ("<i>questo / questa / questi / queste</i>: __ è Marco · __ è Anna · __ sono Marco e Luca · __ sono Anna e Sofia.",
     "Questo · Questa · Questi · Queste"),
    ("Preguntá la edad en informal y en formal.", "Quanti anni hai? · Quanti anni ha?"),
    ("Corregí las mayúsculas: <i>sono argentino, di córdoba. parlo Spagnolo.</i>", "Sono argentino, di Córdoba. Parlo spagnolo."),
    ("Respondé: <i>Perché studi l'italiano?</i>", "Libre. Ej.: Perché amo l'Italia. / Perché ho una bisnonna italiana.")],
6: [("<i>il / lo / l' / la</i>: __ cameriere · __ studente · __ operaio · __ segretaria · __ insegnante · __ zaino.",
     "il · lo · l' · la · l' · lo"),
    ("Completá con <i>fare</i>: <i>Io ____ l'ingegnere. Tu che lavoro ____? Lei ____ la cuoca.</i>", "faccio · fai · fa"),
    ("¿Dónde trabajan? il cuoco · l'infermiere · il commesso · l'impiegato.", "ristorante · ospedale · negozio · ufficio"),
    ("Femenino: cameriere · commesso · dottore · gelataio.", "cameriera · commessa · dottoressa · gelataia"),
    ("Decí tu trabajo con <i>fare</i> y con <i>essere</i>.", "Ej.: Faccio lo stagista / Sono stagista (= pasante).")],
7: [("Conjugá: noi (lavorare) · voi (abitare) · loro (parlare) · noi (cercare) · loro (essere) · voi (avere) · loro (fare).",
     "lavoriamo · abitate · parlano · cerchiamo · sono · avete · fanno"),
    ("<i>a</i> o <i>in</i>: <i>Abito __ Córdoba. Lavoro __ Argentina. Isabella lavora __ Lecce, __ Puglia. Abito __ via Roma.</i>",
     "a · in · a · in · in"),
    ("Concordá el adjetivo: un ragazzo (italiano) · una ragazza (italiano) · una città (grande) · una vita (straordinario).",
     "italiano · italiana · grande · straordinaria"),
    ("Corregí: <i>Lui lavori in Francia.</i>", "Lui lavora in Francia."),
    ("Traducí: <i>A los 30 años.</i> · <i>Nací en Córdoba, en Argentina.</i>", "A 30 anni. · Sono nato a Córdoba, in Argentina."),
    ("¿<i>e</i> o <i>ed</i>?: <i>Isabella ha 22 anni __ è una cuoca.</i>", "ed")],
8: [("Pasá a formal: <i>Abiti a Roma? · Qual è il tuo indirizzo? · Che lavoro fai? · Quanti anni hai?</i>",
     "Abita a Roma? · Qual è il Suo indirizzo? · Che lavoro fa? · Quanti anni ha?"),
    ("<i>a</i>, <i>in</i> o nada: <i>Abito __ Córdoba. Abito __ via Corrientes 334. Il mio indirizzo è __ via Massa 14. Abito __ Stati Uniti.</i>",
     "a · in · (nada) · negli"),
    ("Leé en voz alta: <i>mario.rossi@gmail.com</i> y <i>www.dieci.it</i>",
     "mario punto rossi chiocciola gmail punto com · vu vu vu punto dieci punto it"),
    ("Completá con <i>tuo / tua / Suo / Sua</i>: <i>Qual è la __ mail?</i> (informal) · <i>Qual è il __ indirizzo?</i> (formal)", "tua · Suo"),
    ("¿<i>via</i>, <i>viale</i>, <i>corso</i> o <i>piazza</i>? Una plaza · una calle común · una avenida con árboles · la avenida principal.",
     "piazza · via · viale · corso"),
    ("Traducí: <i>Quisiera inscribirme a un curso de italiano.</i>", "Vorrei iscrivermi a un corso di italiano.")],
}


def soluciones():
    s = [h1("Anexo — Soluciones"), info("Respuestas de <i>Mettiti alla prova</i>.")]
    for n, items in ESERCIZI.items():
        s += [h2(f"Clase {n}")]
        s += tabla([["N.º", "Respuesta"]] + [[str(i + 1), a] for i, (q, a) in enumerate(items)], [12, 158])
    return s
