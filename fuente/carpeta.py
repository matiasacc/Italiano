from comun import *
from letture import LETTURE
from extra import ASCOLTA, ascolta, ASCOLTA_QR, ascolta_qr, ESERCIZI, ejercicios, soluciones
from verbos import VERBOS

# (fecha, tema, libro) para el índice
CLASES = [
    ("23/09", "Saludos, alfabeto, números 0–20, llamarse", "Lezione 0 · 1A (págs. 11–17)"),
    ("30/09", "De dónde sos: essere, nacionalidades, negación", "1B (págs. 18–19)"),
    ("07/10", "Objetos, avere, artículo indeterminado, género", "1C (págs. 20–21)"),
    ("14/10", "Formal / informal: Può ripetere?", "1D + Videocorso (págs. 22–24)"),
    ("21/10", "Lezione 2: edad, verbos en -are, números 21–100", "2A (págs. 27–29)"),
    ("28/10", "Trabajos, fare, artículo determinado", "2B (págs. 30–31)"),
    ("04/11", "Plural de los verbos, preposiciones a / in", "2C (págs. 32–33)"),
    ("11/11", "Datos personales, direcciones, formal (Suo)", "2D (págs. 34–35)"),
    ("18/11", "Al bar: desayuno, prendere, plural, precios", "3A (págs. 39–41)"),
]


def portada(paginas=None):
    s = [Paragraph("ITALIANO", T), Paragraph("Carpeta de clases · Libro: <i>Dieci A1</i> (Alma Edizioni)", SUB),
         Paragraph("Índice", H1), info("Cada clase arranca en página impar, para imprimir en doble faz.")]
    filas = [["Clase", "Fecha", "Tema", "Libro", "Pág."]]
    for i, (f, t, l) in enumerate(CLASES):
        pg = str(paginas[i + 1]) if paginas else ""
        filas.append([str(i + 1), f, t, l, pg])
    filas.append(["Anexo", "", "Verbos: tabla de consulta", "", str(paginas[len(CLASES) + 1]) if paginas else ""])
    filas.append(["Anexo", "", "Soluciones de los ejercicios", "", str(paginas[len(CLASES) + 2]) if paginas else ""])
    s += tabla(filas, [17, 15, 71, 52, 12])
    s += [h2("Cómo leer la carpeta")]
    s += tabla([["Recuadro", "Qué tiene"],
                ["<font color='#1F3A5F'><b>EN CLASE</b></font>", "Lo que anoté en clase, ordenado."],
                ["<font color='#1F3A5F'><b>DEL LIBRO</b></font>", "Teoría, vocabulario y frases de las páginas trabajadas."],
                ["<font color='#AA3333'><b>Corrección</b></font>", "Error del apunte, corregido."],
                ["<font color='#1F3A5F'><b>Nota</b></font>", "Aclaración o regla agregada."],
                ["<font color='#2E7D32'><b>Lo sapevi?</b></font>", "Dato curioso o de contexto."],
                ["<font color='#1F3A5F'><b>LETTURA</b></font>", "Texto o diálogo sobre Italia, con lo visto hasta esa clase."],
                ["<font color='#1F3A5F'><b>DA ASCOLTARE E DA VEDERE</b></font>", "Canciones, películas y videos relacionados."],
                ["<font color='#1F3A5F'><b>METTITI ALLA PROVA</b></font>", "Ejercicios. Soluciones en el anexo."]],
               [55, 115])
    return s


def clases():
    s = []
    # ================================================================ CLASE 1
    s += [h1("Clase 1 — 23/09"), info("Libro: Lezione 0 <i>Lettere e numeri</i> · 1A <i>Buongiorno!</i> (págs. 11–17)"),
          sec("En clase"),
          h2("1. Español e italiano: parecidos, pero no iguales"),
          p("Muchas palabras se parecen al español. Puede pasar que:")]
    s += li("signifiquen lo mismo;",
            "signifiquen otra cosa (falsos amigos): <i>burro</i> = manteca;",
            "cambien de género: <b>la mappa</b> (fem.) — en español, <i>el</i> mapa.")
    s += [p("<b>fermare</b> = parar, detener. · <b>sillabare</b> = deletrear.")]
    s += [p("Hay nombres terminados en <b>-a</b> que son masculinos: <b>Andrea</b> (= Andrés), <i>Nicola, Luca, Mattia</i>.")]
    s += sapevi("en la pág. 25 del libro (<i>Dieci nomi molto usati</i>) se pregunta cuál de estos nombres es femenino: "
                "Andrea, Daniele, Nicola, Simone, Alice, Emanuele. Solo <b>Alice</b>. Todos los demás son masculinos.")

    s += [h2("2. Saludos")]
    s += tabla([["Saludo", "Registro", "Cuándo"],
                ["Ciao!", "informal", "Al llegar y al irse (hola / chau)."],
                ["Salve!", "neutro", "≈ \"¡buenas!\". Sirve cuando no sabés si tutear."],
                ["Buongiorno / Buondì", "formal", "Buen día: a la mañana y hasta el mediodía."],
                ["Buon pomeriggio", "formal", "Tarde temprano."],
                ["Buonasera", "formal", "Desde la tarde-noche."],
                ["Arrivederci", "formal", "Al irse, a cualquier hora."],
                ["Buonanotte", "—", "<b>Solo</b> al despedirse para ir a dormir."]],
               [38, 20, 112])
    s += sapevi("<i>ciao</i> viene del veneciano <i>s'ciào (vostro)</i>, \"(su) esclavo\": era una fórmula de cortesía, "
                "como \"a su servicio\". Con el tiempo quedó como saludo informal.")

    s += [h2("3. Formal e informal")]
    s += tabla([["Registro", "Pronombre", "Con quién"],
                ["<b>informale</b>", "<i>tu</i>", "Amigos, familia, compañeros, chicos."],
                ["<b>formale</b>", "<i>Lei</i>", "Alguien que no conozco, una persona mayor, un superior."]],
               [30, 25, 115])
    s += tabla([["Expresión", "Significado"],
                ["Piacere! — Piacere mio!", "¡Mucho gusto! — El gusto es mío."],
                ["Come, scusa? / Come, scusi?", "¿Cómo, perdón? (informal / formal)"],
                ["Scusi, ...", "Disculpe, ... (para llamar la atención, formal)"]],
               [55, 115])

    s += [h2("4. Come ti chiami? — <i>chiamarsi</i> (llamarse)"),
          p("Es un verbo <b>reflexivo</b>: va con pronombre, igual que en español (<i>me</i> llamo).")]
    s += tabla([["Persona", "Pronombre", "chiamarsi"],
                ["io", "mi", "chiamo"], ["tu", "ti", "chiami"], ["lui / lei / Lei", "si", "chiama"],
                ["noi", "ci", "chiamiamo"], ["voi", "vi", "chiamate"], ["loro", "si", "chiamano"]],
               [45, 30, 40])
    s += corr("<i>loro si <b>chiamano</b></i> (en el apunte quedó \"chiamamo\").")
    s += [p("Ej.: <i>Come ti chiami?</i> — <i>Mi chiamo Andrés.</i> · Formal: <i>Come si chiama?</i>")]

    s += [h2("5. Números ordinales 1.º a 4.º")]
    s += tabla([["", "Masc.", "Fem."], ["1.º", "primo", "prima"], ["2.º", "secondo", "seconda"],
                ["3.º", "terzo", "terza"], ["4.º", "quarto", "quarta"]], [18, 35, 35])

    s += [sec("Del libro"),
          h2("6. Alfabeto (Lezione 0)"),
          p("21 letras propias. <b>J, K, W, X, Y</b> solo aparecen en palabras extranjeras.")]
    s += tabla([["Letra", "Nombre", "Ej.", "Letra", "Nombre", "Ej.", "Letra", "Nombre", "Ej."],
                ["A", "a", "Amore", "H", "acca", "Hotel", "R", "erre", "Roma"],
                ["B", "bi", "Bacio", "I", "i", "Italia", "S", "esse", "Spaghetti"],
                ["C", "ci", "Ciao", "L", "elle", "Lasagna", "T", "ti", "Tiramisù"],
                ["D", "di", "Dieci", "M", "emme", "Mamma", "U", "u", "Uno"],
                ["E", "e", "Espresso", "N", "enne", "Napoli", "V", "vu", "Vespa"],
                ["F", "effe", "Firenze", "O", "o", "Opera", "Z", "zeta", "Zanzara"],
                ["G", "gi", "Grazie", "P", "pi", "Pasta", "", "", ""],
                ["", "", "", "Q", "qu", "Questo", "", "", ""]],
               [12, 15, 26, 12, 15, 26, 12, 15, 26])
    s += tabla([["Extranjeras", "J i lunga", "K kappa", "W doppia vu", "X ics", "Y ipsilon"]],
               [28, 28, 28, 30, 28, 28], encabezado=False)
    s += [p("<b>Come si scrive?</b> — <b>Si scrive</b> ci – a – pi – pi – u – ci – ci – i – enne – o. (= <i>cappuccino</i>)")]
    s += corr("en <i>ciao</i> la <b>i no se pronuncia</b>: solo hace que la c suene \"ch\". Se dice \"chao\". "
              "En general, en italiano se pronuncian todas las letras (en <i>guerra</i> se oye la u).")

    s += [h2("7. Números 0 a 20")]
    s += tabla([["0", "zero", "6", "sei", "11", "undici", "16", "sedici"],
                ["1", "uno", "7", "sette", "12", "dodici", "17", "diciassette"],
                ["2", "due", "8", "otto", "13", "tredici", "18", "diciotto"],
                ["3", "tre", "9", "nove", "14", "quattordici", "19", "diciannove"],
                ["4", "quattro", "10", "dieci", "15", "quindici", "20", "venti"],
                ["5", "cinque", "", "", "", "", "", ""]],
               [9, 22, 9, 22, 9, 26, 9, 26], encabezado=False)
    s += nota("del 11 al 16 la terminación es <b>-dici</b> (undici ... sedici); del 17 al 19 se invierte: "
              "<b>dicia-</b> + número (diciassette, diciotto, diciannove).")

    s += [h2("8. 1A — <i>Buongiorno!</i>: diálogos")]
    s += tabla([["Diálogo del libro", "Qué muestra"],
                ["Buonasera, Filippo Marini. — Sara Ferrari. Piacere. — Piacere mio!", "Presentación formal: nombre + apellido."],
                ["Ciao, mi chiamo Ivan, e tu? — Noelia. — Come, scusa? — Noelia.", "Informal; pedir que repitan."],
                ["Come ti chiami? — Roberto. Tu Cristina... No? — No, io mi chiamo Anna! — Ah, sì, scusa!", "Corregir un nombre."]],
               [100, 70])
    s += nota("el pronombre (<i>io, tu</i>) normalmente se omite, como en español: <i>Sono la signora Martini</i> = "
              "<i>Io sono la signora Martini</i>. Se usa para remarcar o contrastar: <i>No, <b>io</b> mi chiamo Anna!</i>")
    s += LETTURE[1]
    s += ascolta(ASCOLTA[1])
    s += ejercicios(ESERCIZI[1])

    # ================================================================ CLASE 2
    s += [h1("Clase 2 — 30/09"), info("Libro: Lezione 1B <i>Di dove sei?</i> (págs. 18–19)"),
          sec("En clase"),
          h2("1. Acento en la última letra"),
          p("Cuando la sílaba tónica es la última, el acento <b>se escribe</b>: <i>papà, università, città, perché, più</i>.")]
    s += tabla([["Italiano", "Español"], ["più", "más"], ["meno", "menos"], ["anche", "también"]], [40, 60])

    s += [h2("2. Verbo <i>essere</i> (ser / estar) — singular")]
    s += tabla([["Persona", "essere", "Ejemplo"],
                ["io", "sono", "Sono argentino."], ["tu", "sei", "Di dove sei?"], ["lui / lei / Lei", "è", "Vito è di Firenze."]],
               [35, 25, 70])

    s += [h2("3. ¿De dónde sos? — <i>Di dove sei?</i>"), p("Se responde con el lugar de nacimiento. Dos formas:")]
    s += tabla([["Forma", "Ejemplo"],
                ["essere + <b>di</b> + ciudad", "Sono di Córdoba. · Sono di San Francisco."],
                ["essere + <b>nacionalidad</b>", "Sono argentino. · Lei è italiana."]],
               [60, 110])
    s += corr("con el país no se usa <i>di</i>: no \"Sono di Italia\", sino <b>Sono italiano</b>.")
    s += [p("Ej.: <i>Vito è di Firenze. — E lei? — Anche lei è di Firenze.</i>")]

    s += [h2("4. Negación: <i>non</i> y <i>no</i>")]
    s += tabla([["", "Uso", "Ejemplo"],
                ["<b>non</b>", "Niega el verbo. Va siempre antes del verbo.", "Non sono francese. · Paolo non è di Londra, è di Roma."],
                ["<b>no</b>", "Respuesta negativa.", "Sei italiano? — No, sono argentino."]],
               [15, 65, 90])

    s += [h2("5. <i>e</i> / <i>è</i>")]
    s += tabla([["", "Significado", "Ejemplo"],
                ["e", "y", "Vito <b>e</b> Paolo"], ["è", "es (essere)", "Vito <b>è</b> di Firenze."]],
               [15, 35, 70])

    s += [h2("6. Números ordinales 5.º a 10.º")]
    s += tabla([["5.º", "quinto", "6.º", "sesto", "7.º", "settimo"],
                ["8.º", "ottavo", "9.º", "nono", "10.º", "decimo"]],
               [12, 25, 12, 25, 12, 25], encabezado=False)
    s += nota("cambian la -o por -a en femenino: <i>la quinta lezione</i>.")

    s += [h2("7. Pronunciación de C y G")]
    s += tabla([["Grafía", "Suena", "Ejemplo"],
                ["ca, co, cu", "k", "casa, cosa"], ["ce, ci", "\"che\", \"chi\"", "cena, ciao"],
                ["che, chi", "\"ke\", \"ki\"", "che, chiamo"], ["ga, go, gu", "g dura", "gatto, gusto"],
                ["ge, gi", "\"ye\", \"yi\" (j inglesa de <i>jeans</i>)", "gelato, giorno"],
                ["ghe, ghi", "\"gue\", \"gui\"", "spaghetti"], ["gn", "ñ", "gnomo, bagno"],
                ["gli", "≈ \"lli\" (como la ll de España)", "famiglia"],
                ["sce, sci", "\"she\", \"shi\"", "pesce, sci"]],
               [28, 82, 60])
    s += nota("<i>gli</i> se parece a la \"ll\" de España, <b>no</b> a la \"ll\" rioplatense (\"sh\"). "
              "El sonido \"sh\" rioplatense en italiano se escribe <b>sc</b> + e/i.")

    s += [sec("Del libro"),
          h2("8. Países, capitales y nacionalidades")]
    s += tabla([["Paese", "Capitale", "Nacionalidad", "Paese", "Capitale", "Nacionalidad"],
                ["Italia", "Roma", "italiano/a", "Spagna", "Madrid", "spagnolo/a"],
                ["Argentina", "Buenos Aires", "argentino/a", "Svezia", "Stoccolma", "svedese"],
                ["Perù", "Lima", "peruviano/a", "Tunisia", "Tunisi", "tunisino/a"],
                ["Cina", "Pechino", "cinese", "Brasile", "Brasilia", "brasiliano/a"],
                ["Germania", "Berlino", "tedesco/a", "Stati Uniti", "Washington", "americano/a"],
                ["Russia", "Mosca", "russo/a", "Inghilterra", "Londra", "inglese"]],
               [24, 26, 28, 24, 26, 28])
    s += sapevi("en italiano se traducen los nombres de muchas capitales: <i>Pechino</i> (Pekín), <i>Mosca</i> (Moscú), "
                "<i>Stoccolma</i>, <i>Londra</i>. Y ojo: <i>tedesco</i> (alemán) no se parece a <i>Germania</i>.")

    s += [h2("9. Adjetivos de nacionalidad: dos grupos")]
    s += tabla([["Grupo", "Masculino", "Femenino", "Ejemplos"],
                ["1 (-o / -a)", "italian<b>o</b>", "italian<b>a</b>", "argentino, spagnolo, peruviano, americano, brasiliano"],
                ["2 (-e)", "ingles<b>e</b>", "ingles<b>e</b>", "francese, cinese, svedese, canadese, giapponese"]],
               [25, 28, 28, 89])
    s += [p("Terminaciones típicas: <b>-ano</b> (italiano), <b>-ese</b> (francese), <b>-ino</b> (argentino, tunisino).")]
    s += [p("<i>Stefano è italiano. · Rosa è italiana. · Simon è inglese. · Jennifer è inglese.</i>")]

    s += [h2("10. Diálogo — <i>Sei italiano?</i>")]
    s += tabla([["Italiano", "Español"],
                ["Di dove sei? — Di Brasilia.", "¿De dónde sos? — De Brasilia."],
                ["Ah, sei brasiliana!", "¡Ah, sos brasileña!"],
                ["Sì, e tu sei italiano? — Sì, sono di Roma. E lei è Theresa.", "Sí, ¿y vos sos italiano? — Sí, soy de Roma. Y ella es Theresa."],
                ["Anche tu sei di Roma? — No, di Londra. Io non sono italiana. Sono inglese.",
                 "¿Vos también sos de Roma? — No, de Londres. No soy italiana. Soy inglesa."]],
               [90, 80])
    s += nota("<i>lei</i> (minúscula) = ella · <i>Lei</i> (mayúscula) = usted.")
    s += LETTURE[2]
    s += ascolta(ASCOLTA[2])
    s += ejercicios(ESERCIZI[2])
    s += tarea("pág. 141, ej. 3, 4 y 5 · pág. 185, ej. 7 a 11.")

    # ================================================================ CLASE 3
    s += [h1("Clase 3 — 07/10"), info("Libro: Lezione 1C <i>Che cos'hai nella borsa?</i> (págs. 20–21)"),
          sec("En clase"),
          h2("1. Vocabulario")]
    s += li("<b>il volantino</b> = folleto.",
            "Sustantivos en <b>-tore</b>: masculinos (<i>attore, dottore, pittore</i>). El femenino lo vemos en la clase 4.")

    s += [h2("2. Artículo indeterminado: un, uno, una, un'"),
          p("Para algo general, no identificado: \"elegí <i>un</i> resaltador\" (cualquiera).")]
    s += tabla([["Género", "Artículo", "Cuándo", "Ejemplo"],
                ["Masc.", "<b>un</b>", "vocal o consonante", "un amico, un libro, un quaderno"],
                ["Masc.", "<b>uno</b>", "s + consonante, z, ps, pn, gn, y", "uno studente, uno zaino, uno psicologo, uno yogurt"],
                ["Fem.", "<b>una</b>", "consonante", "una penna, una matita, una chiave"],
                ["Fem.", "<b>un'</b>", "vocal", "un'amica, un'agenda"]],
               [16, 18, 50, 86])
    s += nota("el <b>apóstrofe</b> marca el género delante de vocal: <i>un amico</i> (masc.) / <i>un'amica</i> (fem.).")

    s += [h2("3. Saludar formal / informal")]
    s += tabla([["Informal", "Ti saluto."], ["Formal", "La saluto."]], [30, 80], encabezado=False)

    s += [h2("4. Verbo <i>avere</i> (tener) — singular"),
          p("La <b>h</b> no se pronuncia: <i>ho</i> = \"o\".")]
    s += tabla([["Persona", "avere", "Ejemplo"],
                ["io", "ho", "Ho un quaderno."], ["tu", "hai", "Hai una penna?"], ["lui / lei / Lei", "ha", "Paolo ha un dizionario."]],
               [35, 25, 70])
    s += sapevi("la h de <i>ho, hai, ha</i> está para distinguirlos de <i>o</i> (o), <i>ai</i> (a los) y <i>a</i> (a), "
                "que suenan igual.")

    s += [sec("Del libro"),
          h2("5. Gli oggetti della classe (volantino \"Uno due tre\")")]
    s += tabla([["Objeto", "Español", "Objeto", "Español"],
                ["uno zaino", "mochila", "un dizionario", "diccionario"],
                ["una penna", "birome", "un'agenda", "agenda"],
                ["una matita", "lápiz", "un evidenziatore", "resaltador"],
                ["un quaderno", "cuaderno", "una chiave USB", "pendrive"],
                ["un libro", "libro", "una sedia", "silla"]],
               [35, 35, 40, 35])
    s += [p("<b>Che cos'hai nella borsa / nello zaino?</b> — <b>Ho</b> un quaderno, una penna... · "
            "<b>Hai</b> un libro? — Sì. / No, <b>non ho</b> un libro.")]

    s += [h2("6. ¿Masculino o femenino? Sustantivos")]
    s += tabla([["Termina en", "Género", "Ejemplos"],
                ["-o", "masculino", "zaino, quaderno, dizionario"],
                ["-a", "femenino", "penna, matita, agenda"],
                ["-e", "masc. <b>o</b> fem. (hay que aprenderlo)", "lo studente (m) · la chiave, la lezione (f)"],
                ["-zione", "siempre femenino", "lezione, informazione, stazione"]],
               [25, 55, 90])
    s += sapevi("hay excepciones: <i>la mano</i> es femenino aunque termine en -o, y muchos nombres de varón terminan en -a (Andrea, Luca).")
    s += LETTURE[3]
    s += ascolta(ASCOLTA[3])
    s += ejercicios(ESERCIZI[3])
    s += tarea("pág. 186, ej. 12 (a y b), 13 (traducir), 14 y 15 · Gramática: pág. 140, artículo indeterminado.")

    # ================================================================ CLASE 4
    s += [h1("Clase 4 — 14/10"), info("Libro: Lezione 1D <i>Può ripetere?</i> + Videocorso (págs. 22–24)"),
          sec("En clase"),
          h2("1. Corrección de tarea — vocabulario")]
    s += tabla([["Italiano", "Español", "Ojo"],
                ["la foglia", "hoja (de árbol)", "Solo cambia la última vocal"],
                ["il foglio", "hoja (de papel)", ""],
                ["il tavolo", "mesa", ""],
                ["la scrivania", "escritorio", ""],
                ["il calcolatore", "primer nombre de la computadora", "Ya no se usa"],
                ["la calcolatrice", "calculadora", "Se dice \"calcolatriche\""]],
               [35, 60, 75])

    s += [h2("2. Masculino -tore → femenino -trice")]
    s += tabla([["-tore", "-trice", "Español"],
                ["attore", "attrice", "actor / actriz"], ["scrittore", "scrittrice", "escritor/a"],
                ["direttore", "direttrice", "director/a"], ["calcolatore", "calcolatrice", "(punto 1)"]],
               [40, 40, 60])
    s += corr("<b>attore</b>, con doble t (en el apunte quedó \"actore\").")

    s += [sec("Del libro"),
          h2("3. Formal (<i>Lei</i>) e informal (<i>tu</i>)"),
          p("En un contexto formal se usa <b>Lei</b> y el verbo va en <b>3.ª persona singular</b>, igual que con <i>lui / lei</i>.")]
    s += tabla([["Informal (tu)", "Formal (Lei)"],
                ["Come ti chiami?", "Come si chiama?"], ["Tu sei di Trieste.", "Lei è di Trieste."],
                ["Hai un documento?", "Ha un documento?"], ["Puoi ripetere?", "Può ripetere?"],
                ["Come, scusa?", "Come, scusi?"], ["E tu?", "E Lei?"]],
               [60, 60])
    s += sapevi("<i>Lei</i> es femenino aunque le hables a un hombre porque viene de <i>la Vostra Signoria</i> "
                "(\"Vuestra Señoría\"). Es como el \"usted\" español, que viene de \"vuestra merced\".")

    s += [h2("4. En la recepción del hotel")]
    s += tabla([["Italiano", "Español"],
                ["Ho una prenotazione.", "Tengo una reserva."],
                ["Come si chiama? — Aldo Stankovic.", "¿Cómo se llama? — Aldo Stankovic."],
                ["Come si scrive il cognome?", "¿Cómo se escribe el apellido?"],
                ["Esse – ti – a – enne – kappa – o – vu – i – ci.", "Deletreo (alfabeto, clase 1)."],
                ["Ha un documento, per favore?", "¿Tiene un documento, por favor?"],
                ["Va bene la carta d'identità?", "¿Está bien el DNI?"],
                ["Camera diciotto.", "Habitación 18."],
                ["Grazie. — Prego. Buonanotte!", "Gracias. — De nada. ¡Buenas noches!"]],
               [80, 90])
    s += nota("<b>il nome</b> = nombre · <b>il cognome</b> = apellido · <b>la residenza</b> = domicilio. "
              "<b>Prego</b> = de nada, y también \"adelante / pase\".")

    s += [h2("5. <i>Dieci domande utili</i>")]
    s += tabla([["Italiano", "Español", "Italiano", "Español"],
                ["Come ti chiami?", "¿Cómo te llamás?", "Sei di Roma?", "¿Sos de Roma?"],
                ["Puoi ripetere?", "¿Podés repetir?", "Anche tu?", "¿Vos también?"],
                ["Di dove sei?", "¿De dónde sos?", "Come si scrive?", "¿Cómo se escribe?"],
                ["Come si dice?", "¿Cómo se dice?", "Come, scusa?", "¿Cómo, perdón?"],
                ["Sei italiano?", "¿Sos italiano?", "Che significa?", "¿Qué significa?"]],
               [36, 40, 36, 40])

    s += [h2("6. Videocorso <i>Io sono Anna</i> (pág. 24)")]
    s += tabla([["Frase", "Para qué sirve"],
                ["Buongiorno. Io mi chiamo Francesca Busi. Piacere.", "Presentarse formal."],
                ["Salve! Io sono Ivano! Sono di Roma.", "Presentarse neutro + origen."],
                ["Il mio nome è Paolo Scherini.", "Otra forma de decir el nombre."],
                ["Come, scusa? Puoi ripetere?", "Pedir que repitan."]],
               [95, 75])
    s += corr("<b>Può</b> ripetere, con acento (en el apunte, \"puo\").")
    s += LETTURE[4]
    s += ascolta(ASCOLTA[4])
    s += ejercicios(ESERCIZI[4])

    # ================================================================ CLASE 5
    s += [h1("Clase 5 — 21/10"), info("Libro: Lezione 2 <i>Persone e professioni</i> · 2A <i>Studio italiano</i> (págs. 27–29)"),
          sec("En clase"),
          h2("1. Corrección de tarea — pronunciación")]
    s += li("<b>pronuncia</b> se dice \"pronúnchia\".",
            "Dos vocales juntas entre palabras: se pierde una y va apóstrofe: <i>Di dove è?</i> → <b>Di dov'è?</b>")

    s += [h2("2. Vocabulario")]
    s += tabla([["Italiano", "Español", "Ojo"],
                ["il modulo", "formulario", "Riempi questo modulo = Llená este formulario"],
                ["la chiocciola", "arroba (@)", "Se dice \"kióchola\". También = caracol"],
                ["il punto", "punto (en mails y webs)", "www = vu – vu – vu"],
                ["l'indirizzo", "dirección", ""],
                ["il CAP", "código postal", ""]],
               [35, 45, 90])
    s += sapevi("en Italia la web se deletrea \"vu – vu – vu\", no \"doppia vu, doppia vu, doppia vu\" (el libro lo marca como error).")

    s += [h2("3. Mayúsculas (gramática, pág. 142)")]
    s += tabla([["Con mayúscula", "Con minúscula"],
                ["nombre y apellido (Sofia Fantini) · ciudad (Bologna) · país (Italia) · "
                 "después de . ! ? · el pronombre <b>Lei</b>",
                 "nacionalidad (italiana) · profesión (insegnante) · idiomas (l'inglese)"]],
               [95, 75])

    s += [h2("4. Presentar: <i>questo / questa</i>"),
          p("Para presentar a alguien o mostrar algo. Igual para formal e informal.")]
    s += tabla([["", "Masculino", "Femenino"],
                ["Singular", "<b>questo</b> — Questo è Juan.", "<b>questa</b> — Questa è Katy."],
                ["Plural", "<b>questi</b> — Questi sono Juan e Luis.", "<b>queste</b> — Queste sono Katy e Mei."]],
               [25, 72, 73])

    s += [h2("5. Presente indicativo y verbos en -are")]
    s += li("Los verbos terminan en <b>-are, -ere, -ire</b> (= -ar, -er, -ir).",
            "Verbo regular = <b>radice</b> (no cambia) + <b>desinenza</b>: <b>parl</b> + <b>-are</b>.",
            "Irregulares: no siguen la regla (<i>essere, avere, fare</i>).")
    s += tabla([["", "PARLARE", "STUDIARE", "AMARE", "ABITARE"],
                ["io", "parl<b>o</b>", "studi<b>o</b>", "am<b>o</b>", "abit<b>o</b>"],
                ["tu", "parl<b>i</b>", "stud<b>i</b>", "am<b>i</b>", "abit<b>i</b>"],
                ["lui / lei / Lei", "parl<b>a</b>", "studi<b>a</b>", "am<b>a</b>", "abit<b>a</b>"]],
               [30, 35, 35, 35, 35])
    s += nota("<b>studiare:</b> la raíz ya termina en i → <i>tu studi</i> (no se agrega otra i). "
              "<b>abitare</b> = vivir en un lugar. El plural se ve en la clase 7. Tablas completas en el PDF de verbos.")
    s += [p("<b>-care / -gare</b>: se agrega <b>h</b> para mantener el sonido duro: <i>cercare → tu cer<b>chi</b></i>, "
            "<i>pagare → tu pa<b>ghi</b></i>.")]

    s += [h2("6. <i>Perché</i>"),
          p("Una sola palabra para \"¿por qué?\" y \"porque\": <i><b>Perché</b> studi italiano? — <b>Perché</b> amo l'Italia.</i>")]

    s += [h2("7. Organización del Estado")]
    s += tabla([["Italia", "≈ Argentina"], ["regione", "provincia"], ["provincia", "departamento"], ["comune", "municipalidad"]],
               [40, 50])
    s += corr("la municipalidad es el <b>comune</b> (en el apunte, \"municipalidad\").")
    s += sapevi("Italia tiene 20 regiones (ver el mapa del libro). Roma es la capital del país y de la región Lazio.")

    s += [sec("Del libro"),
          h2("8. Tre studenti: preguntas personales")]
    s += tabla([["Pregunta (formal)", "Pregunta (informal)", "Respuesta del libro"],
                ["Come si chiama?", "Come ti chiami?", "Si chiama Juan."],
                ["Quanti anni ha?", "Quanti anni hai?", "Ha 26 anni."],
                ["Di dov'è?", "Di dove sei?", "È spagnolo."],
                ["Dove abita?", "Dove abiti?", "Abita a Madrid."],
                ["Perché studia italiano?", "Perché studi italiano?", "Perché è un interprete."],
                ["Che lingue parla?", "Che lingue parli?", "Parla spagnolo, inglese e tedesco."]],
               [50, 50, 70])
    s += nota("la edad se dice con <b>avere</b>, como en español: <i>Ho 30 anni.</i>")

    s += [h2("9. Números de 20 a 100")]
    s += tabla([["20", "venti", "50", "cinquanta", "80", "ottanta"],
                ["30", "trenta", "60", "sessanta", "90", "novanta"],
                ["40", "quaranta", "70", "settanta", "100", "cento"]],
               [12, 30, 12, 30, 12, 30], encabezado=False)
    s += [p("Se unen decena + unidad: <i>trentadue</i> (32), <i>quarantacinque</i> (45).")]
    s += nota("con <b>uno</b> y <b>otto</b> la decena pierde la vocal: <i>ventuno, ventotto, trentuno</i>. "
              "Con <b>tre</b>, acento: <i>ventitré, trentatré</i>.")
    s += LETTURE[5]
    s += ascolta(ASCOLTA[5])
    s += ejercicios(ESERCIZI[5])
    s += tarea("pág. 26, test · pág. 191, ej. 5 · Gramática: pág. 162 (verbos en -are) y pág. 142 (-care / -gare).")

    # ================================================================ CLASE 6
    s += [h1("Clase 6 — 28/10"), info("Libro: Lezione 2B <i>Che lavoro fai?</i> (págs. 30–31)"),
          sec("En clase"),
          h2("1. Vocabulario")]
    s += tabla([["Italiano", "Español"],
                ["il pronto soccorso", "la guardia. <i>Vado al pronto soccorso.</i> = Voy a la guardia."],
                ["Bravo! / Brava!", "¡Muy bien! Concuerda con la persona (bravo, brava, bravi, brave)."]],
               [40, 130])
    s += sapevi("<i>bravo</i> es un falso amigo: en italiano significa \"bueno, capaz\", no feroz. <i>Un bravo insegnante</i> = un buen profesor.")

    s += [h2("2. Verbo <i>fare</i> (hacer) — irregular")]
    s += tabla([["Persona", "fare"], ["io", "faccio"], ["tu", "fai"], ["lui / lei / Lei", "fa"]], [35, 30])
    s += tabla([["Pregunta", "Respuesta (dos formas)"],
                ["Che lavoro fai? · Che cosa fai? (inf.)<br/>Che lavoro fa? (form.)",
                 "<b>Faccio</b> l'operaio. · <b>Sono</b> insegnante."]],
               [75, 95])
    s += nota("con <i>fare</i> la profesión lleva artículo determinado (<i>faccio <b>l'</b>insegnante</i>). "
              "Con <i>essere</i>, lo más común es sin artículo (<i>sono insegnante</i>).")

    s += [h2("3. Artículo determinado (il, lo, l', la)"),
          p("Para algo <b>específico</b>, que ya se sabe cuál es. Depende del género y de cómo empieza la palabra.")]
    s += tabla([["Género", "Artículo", "Cuándo", "Ejemplo", "Indet."],
                ["Masc.", "<b>il</b>", "consonante", "il cameriere", "un"],
                ["Masc.", "<b>lo</b>", "s + consonante, z, ps, gn, y", "lo studente, lo zaino", "uno"],
                ["Masc.", "<b>l'</b>", "vocal", "l'operaio, l'impiegato", "un"],
                ["Fem.", "<b>la</b>", "consonante", "la segretaria", "una"],
                ["Fem.", "<b>l'</b>", "vocal", "l'insegnante, l'operaia", "un'"]],
               [16, 18, 50, 66, 18])
    s += [p("<b>Usos particulares:</b> con países (<i>Amo <b>l'</b>Italia</i>) y con idiomas (<i>Parlo <b>l'</b>inglese</i> o <i>Parlo inglese</i>).")]

    s += [h2("4. ¿Masculino o femenino?"),
          p("En las palabras en <b>-e</b> (<i>insegnante, cantante</i>) mirá el <b>artículo</b>. "
            "Si es <i>l'</i>, tampoco lo dice: entonces lo indica el <b>adjetivo</b>.")]
    s += tabla([["Por el artículo", "<b>un</b> insegnante (él) · <b>un'</b>insegnante (ella)"],
                ["Por el adjetivo", "L'insegnante di inglese è <b>bravo</b> (él) / è <b>brava</b> (ella)"]],
               [35, 135], encabezado=False)
    s += [p("Las palabras extranjeras suelen ser masculinas: <i>il computer, il bar, lo snowboard</i>.")]

    s += [sec("Del libro"),
          h2("5. Luoghi di lavoro y profesiones (págs. 30 y 162)")]
    s += tabla([["Masculino", "Femenino", "Español", "Lugar de trabajo"],
                ["operaio", "operaia", "obrero/a", "la fabbrica"],
                ["impiegato", "impiegata", "empleado/a", "l'ufficio"],
                ["segretario", "segretaria", "secretario/a", "l'ufficio"],
                ["direttore", "direttrice", "director/a", "l'ufficio"],
                ["architetto", "architetto (o architetta)", "arquitecto/a", "l'ufficio"],
                ["dottore", "dottoressa", "médico/a", "l'ospedale"],
                ["infermiere", "infermiera", "enfermero/a", "l'ospedale"],
                ["cameriere", "cameriera", "mozo / moza", "il ristorante"],
                ["cuoco", "cuoca", "cocinero/a", "il ristorante"],
                ["commesso", "commessa", "vendedor/a", "il negozio"],
                ["gelataio", "gelataia", "heladero/a", "la gelateria"],
                ["insegnante", "insegnante", "profesor/a", "la scuola"],
                ["cantante", "cantante", "cantante", "—"],
                ["modello", "modella", "modelo", "—"]],
               [30, 40, 35, 35])
    s += corr("<b>ufficio</b> (no \"officio\") · <b>operaio</b> (no \"operario\") · <b>direttrice</b> se pronuncia \"direttriche\".")
    s += sapevi("la terminación <b>-aio</b> indica oficio, como \"-ero\": <i>gelataio, fornaio</i> (panadero), <i>giornalaio</i> (diariero).")

    s += [h2("6. Entrevistas — <i>Tu che lavoro fai?</i>")]
    s += tabla([["Diálogo del libro", "Español"],
                ["Lei che lavoro fa? — Lavoro in un ufficio. — Fa la segretaria? — No, sono la direttrice!",
                 "¿Usted de qué trabaja? — En una oficina. — ¿Es secretaria? — ¡No, soy la directora!"],
                ["Io faccio l'operaio, lavoro in una fabbrica. — Per un'azienda famosa? — Sì, per la Pirelli.",
                 "Soy obrero, trabajo en una fábrica. — ¿Para una empresa famosa? — Sí, para Pirelli."],
                ["Sono uno studente, ma lavoro anche. Faccio il cameriere in un ristorante. — Studi e lavori. Bravo!",
                 "Soy estudiante, pero también trabajo: soy mozo. — Estudiás y trabajás. ¡Muy bien!"],
                ["L'insegnante. Lavoro in una scuola di lingue. — Un lavoro interessante!",
                 "Profesora, en una escuela de idiomas. — ¡Un trabajo interesante!"]],
               [90, 80])
    s += sapevi("Pirelli es una empresa de neumáticos fundada en Milán en 1872. "
                "<i>Lavorare per</i> + empresa = trabajar para; <i>lavorare in</i> + lugar = trabajar en.")
    s += LETTURE[6]
    s += ascolta(ASCOLTA[6])
    s += ejercicios(ESERCIZI[6])
    s += tarea("pág. 163, ej. 1 a 4 · pág. 192, ej. 8 (el 9 no) · pág. 191, ej. 1 y 2.")

    # ================================================================ CLASE 7
    s += [h1("Clase 7 — 04/11"), info("Libro: Lezione 2C <i>Tre ragazzi di talento</i> (págs. 32–33) · Gramática pág. 142"),
          sec("En clase"),
          h2("1. Vocabulario: objetos de cada profesión (vocabulario, pág. 163)")]
    s += tabla([["Italiano", "Español", "¿De quién?"],
                ["la pentola", "olla", "il cuoco"],
                ["il piatto", "plato", "il cuoco, il cameriere"],
                ["il metro / la bindella", "cinta métrica", "l'architetto"],
                ["lo stetoscopio", "estetoscopio", "il dottore"],
                ["il microfono", "micrófono", "il cantante"],
                ["l'amministratore delegato", "director ejecutivo (CEO)", "—"]],
               [50, 50, 50])

    s += [h2("2. <i>Che lavoro fanno?</i> (pág. 32)")]
    s += [p("<i>Secondo me</i> = en mi opinión. <i>Secondo me Pietro fa il modello.</i>")]
    s += tabla([["Persona", "Trabajo", "Del texto <i>Talento giovane</i>"],
                ["Pietro Boselli", "professore + modello", "È di Brescia, abita a Londra, insegna matematica. Ha una vita straordinaria: è un modello famoso."],
                ["Isabella Potì", "cuoca", "Ha 22 anni. Dopo Spagna e Francia, ora fa la cuoca in un ristorante a Lecce, in Puglia."],
                ["Federico Schiano", "architetto", "È un architetto romano. A 28 anni ha un'idea geniale e crea CoContest."]],
               [32, 33, 105])
    s += [p("<b>A 28 anni</b> = <b>a los</b> 28 años (no \"tiene 28 años\", que sería <i>ha 28 anni</i>).")]
    s += sapevi("delante de vocal, <i>e</i> suele volverse <b>ed</b> para que suene mejor: el texto dice "
                "<i>Isabella Potì ha 22 anni <b>ed</b> è una ragazza di talento</i>. Pasa lo mismo con <i>a → ad</i>: <i>ad Amalfi</i>.")
    s += corr("mejor <i>... <b>ed</b> è un cuoco</i> que \"e è\" (ver Lo sapevi).")

    s += [h2("3. Preposiciones de lugar: <i>a</i> e <i>in</i>")]
    s += tabla([["Preposición", "Con", "Ejemplo"],
                ["<b>a</b>", "ciudad", "Abito <b>a</b> Roma. · Lavori <b>a</b> Brescia."],
                ["<b>in</b>", "región / país", "Isabella lavora <b>in</b> Puglia. · Lavori <b>in</b> Lombardia. · Lui lavora <b>in</b> Francia."],
                ["<b>in</b>", "calle / plaza", "Abito <b>in</b> via Foscolo."],
                ["<b>di</b>", "ciudad de origen", "Sono <b>di</b> Barcellona."]],
               [25, 35, 110])
    s += corr("<i>Isabella <b>lavora</b></i> y <i>lui <b>lavora</b></i>, con -a (3.ª persona). "
              "<i>Lavori</i> es solo para <i>tu</i>.")
    s += nota("con países en plural va con artículo: <i>Abito <b>negli</b> Stati Uniti</i>.")
    s += [p("Para aprender: <b>Io sono nato a San Francisco, in Argentina.</b> (ciudad → a · país → in)")]
    s += nota("<i>sono nato</i> = nací. Una mujer dice <i>sono <b>nata</b></i>. Es un pasado con <i>essere</i>; lo veremos más adelante.")
    s += sapevi("Brescia está en la región Lombardia y Lecce en Puglia, \"el taco de la bota\".")

    s += [h2("4. Pronombres plurales")]
    s += tabla([["Singular", "Plural"], ["io (yo)", "noi (nosotros/as)"], ["tu (vos)", "voi (ustedes)"],
                ["lui / lei / Lei (él / ella / usted)", "loro (ellos/as)"]], [70, 60])
    s += nota("<b>voi</b> es el \"ustedes\" de todos los días (informal). El \"ustedes\" formal, <i>Loro</i>, casi no se usa.")

    s += [sec("Del libro"),
          h2("5. Plural de los verbos (pág. 33 ej. 2b · gramática pág. 142)")]
    s += tabla([["", "AMARE", "LAVORARE", "AVERE", "ESSERE", "FARE"],
                ["io", "amo", "lavoro", "ho", "sono", "faccio"],
                ["tu", "ami", "lavori", "hai", "sei", "fai"],
                ["lui / lei / Lei", "ama", "lavora", "ha", "è", "fa"],
                ["noi", "am<b>iamo</b>", "lavor<b>iamo</b>", "<b>abbiamo</b>", "<b>siamo</b>", "<b>facciamo</b>"],
                ["voi", "am<b>ate</b>", "lavor<b>ate</b>", "<b>avete</b>", "<b>siete</b>", "<b>fate</b>"],
                ["loro", "am<b>ano</b>", "lavor<b>ano</b>", "<b>hanno</b>", "<b>sono</b>", "<b>fanno</b>"]],
               [28, 26, 28, 28, 28, 28])
    s += nota("en <i>loro amano, lavorano</i> el acento va en la raíz: <b>à</b>mano, lav<b>ò</b>rano (no amanó). "
              "<i>io sono</i> y <i>loro sono</i> son iguales.")

    s += [h2("6. Casos especiales -care, -gare, -iare (pág. 142)")]
    s += tabla([["", "CERCARE", "PAGARE", "STUDIARE"],
                ["io", "cerco", "pago", "studio"], ["tu", "cer<b>chi</b>", "pa<b>ghi</b>", "stud<b>i</b>"],
                ["lui / lei / Lei", "cerca", "paga", "studia"], ["noi", "cer<b>chiamo</b>", "pa<b>ghiamo</b>", "stud<b>iamo</b>"],
                ["voi", "cercate", "pagate", "studiate"], ["loro", "cercano", "pagano", "studiano"]],
               [30, 35, 35, 35])
    s += nota("la <b>h</b> aparece solo delante de <i>i</i> (tu y noi). En -iare no se duplica la i.")

    s += [h2("7. Sustantivo + adjetivo (pág. 142)")]
    s += tabla([["Grupo", "Masc.", "Fem.", "Ejemplo"],
                ["1 (-o / -a)", "piccolo", "piccola", "un ufficio piccolo · un'azienda famosa"],
                ["2 (-e)", "grande", "grande", "un negozio grande · un'idea interessante"]],
               [25, 25, 25, 95])
    s += li("El adjetivo concuerda con el sustantivo y en general va <b>después</b>: <i>un modello famoso, una vita straordinaria</i>.",
            "Las ciudades son femeninas: <i>Roma è antica. · Milano è bella e moderna.</i>")
    s += [h2("8. Tarea resuelta — pág. 33, ej. 1d"),
          p("<i>Abbina le parole delle 5 colonne e forma frasi</i>: nombre + <i>è / ha</i> + artículo + sustantivo + adjetivo, según el texto <i>Talento giovane</i>.")]
    s += tabla([["Frase", "Español"],
                ["Pietro è un professore universitario.", "Pietro es un profesor universitario."],
                ["Pietro è un modello famoso.", "Pietro es un modelo famoso."],
                ["Pietro ha una vita straordinaria.", "Pietro tiene una vida extraordinaria."],
                ["Isabella è una ragazza italiana.", "Isabella es una chica italiana."],
                ["Federico è un architetto romano.", "Federico es un arquitecto romano."],
                ["Federico ha un'idea geniale.", "Federico tiene una idea genial."]],
               [85, 85])
    s += nota("<i>è</i> + profesión o descripción · <i>ha</i> + algo que se tiene (<i>una vita, un'idea</i>). "
              "El adjetivo concuerda: <i>un modell<b>o</b> famos<b>o</b> · una ragazz<b>a</b> italian<b>a</b></i>; "
              "<i>geniale</i> (en -e) sirve para los dos géneros. Y <i>un'idea</i> lleva apóstrofe porque es femenino y empieza con vocal.")
    s += LETTURE[7]
    s += ascolta(ASCOLTA[7])
    s += ejercicios(ESERCIZI[7])
    s += tarea("pág. 33, ej. 1d (resuelta en el punto 8) · pág. 143, ej. 4, 5 y 6 · pág. 192, ej. 9 a 13 · pág. 193, ej. 15 y 16.")
    # ================================================================ CLASE 8
    s += [h1("Clase 8 — 11/11"), info("Libro: Lezione 2D <i>Qual è il tuo numero di telefono?</i> (págs. 34–35) · Vocabulario pág. 162"),
          sec("En clase"),
          h2("1. Los idiomas son masculinos")]
    s += [p("Los nombres de idiomas siempre son <b>masculinos</b>: <i>l'italiano, il cinese, lo spagnolo, il tedesco</i>. "
            "<i>Studio <b>il</b> cinese. · Un corso <b>di</b> cinese.</i>")]
    s += nota("<b>il corso</b> = curso (<i>un corso di lingua</i>). También es el nombre de una avenida principal (punto 3).")

    s += [h2("2. Datos personales (vocabulario, pág. 162)")]
    s += tabla([["Pregunta", "Respuesta / ejemplo"],
                ["Qual è il tuo numero di telefono?", "Il mio numero è 333 8154871."],
                ["Qual è la tua mail?", "s.fantini<b>@</b>gmail<b>.</b>com → esse punto fantini <b>chiocciola</b> gmail <b>punto</b> com"],
                ["Qual è il tuo indirizzo? · Dove abiti?", "Via Giuseppe Verdi 9. · Abito in via Corrientes 334."],
                ["Hai un sito internet?", "Sì: www.studiovinci.com → vu vu vu punto studiovinci punto com"]],
               [62, 108])
    s += tabla([["Italiano", "Español"],
                ["il biglietto da visita", "tarjeta personal"], ["la chiocciola (@)", "arroba (se dice \"kióchola\")"],
                ["il punto (.)", "punto"], ["il CAP", "<b>C</b>odice di <b>A</b>vviamento <b>P</b>ostale = código postal"],
                ["il telefono fisso / il cellulare", "teléfono fijo / celular"], ["il sito web", "página web"]],
               [55, 115])
    s += sapevi("en Japón y otros países de Asia la tarjeta personal se da y se recibe con las dos manos, mirándola un momento: "
                "guardarla sin leerla se considera descortés.")

    s += [h2("3. Calles: via, viale, corso, piazza")]
    s += tabla([["Italiano", "Qué es", "Ejemplo"],
                ["<b>via</b>", "calle (la palabra común; <i>strada</i> es \"calle/camino\" en general)", "via Massa 14"],
                ["<b>viale</b>", "avenida ancha con árboles (en el medio o a los costados)", "viale dei Mille"],
                ["<b>corso</b>", "avenida principal, en general céntrica y comercial", "Corso Vittorio Emanuele"],
                ["<b>piazza</b>", "plaza", "piazza Toti 15"]],
               [22, 95, 53])
    s += nota("en la dirección, el número va <b>después</b> del nombre de la calle, como en Argentina: <i>via Massa <b>14</b></i>.")

    s += [h2("4. Preposiciones: <i>a</i> ciudad · <i>in</i> calle (Focus, pág. 34)")]
    s += tabla([["Pregunta", "Respuesta"],
                ["Dove abiti?", "Abito <b>a</b> Córdoba. · Abito <b>a</b> San Francisco. (ciudad)"],
                ["", "Abito <b>in</b> via Corrientes 334. · <b>In</b> piazza Toti 15. (calle / plaza)"],
                ["Qual è il tuo indirizzo?", "Via Corrientes 334. (<b>sin</b> preposición)"]],
               [50, 120])
    s += nota("con países en plural va <b>negli</b>: <i>Abito <b>negli</b> Stati Uniti</i> (in + gli). Lo pide la tarea, pág. 143.")

    s += [h2("5. Decir el número de teléfono"),
          p("Como en español: cifra por cifra o de a pares.")]
    s += tabla([["Número", "Cifra por cifra", "De a pares"],
                ["06 61713210", "zero – sei · sei – uno – sette – uno – tre – due – uno – zero",
                 "zero sei · sessantuno – settantuno – trentadue – dieci"]],
               [28, 80, 62])
    s += sapevi("en Italia los fijos empiezan con <b>0</b> (06 = Roma, 02 = Milano, 055 = Firenze) y los celulares con <b>3</b> (333, 347...). "
                "El CAP tiene siempre 5 cifras.")

    s += [h2("6. Formal e informal: cuándo y cómo")]
    s += li("<b>Lei</b> con mayúscula = usted.",
            "<b>Formal</b>: con alguien que no conozco y en situaciones de servicio o trabajo (atención al público, un cliente, un jefe).",
            "<b>Informal</b>: con un compañero de trabajo, amigos, familia, aunque estemos en el trabajo.")
    s += tabla([["Informal (tu)", "Formal (Lei)"],
                ["Dove abiti?", "Dove abita?"], ["Dove vai?", "Dove va?"],
                ["Qual è il <b>tuo</b> indirizzo?", "Qual è il <b>Suo</b> indirizzo?"],
                ["Qual è la <b>tua</b> mail?", "Qual è la <b>Sua</b> mail?"],
                ["Quanti anni <b>hai</b>?", "Quanti anni <b>ha</b>?"], ["Che lavoro <b>fai</b>?", "Che lavoro <b>fa</b>?"],
                ["Che cosa ti posso servire?", "Che cosa <b>Le</b> posso servire?"]],
               [80, 80])
    s += nota("<b>tuo / tua</b> → <b>Suo / Sua</b> (con mayúscula). <b>Le</b> = \"le\" (a usted): <i>Che cosa Le posso servire?</i> = ¿Qué le puedo servir?")
    s += corr("en el apunte quedó \"abbene → hai → ha\": es <b>avere</b>: <i>hai</i> (tu) → <i>ha</i> (Lei).")

    s += [sec("Del libro"),
          h2("7. En la secretaría de una escuela de idiomas (pág. 34–35)")]
    s += tabla([["Frase", "Español"],
                ["Buongiorno, <b>vorrei iscrivermi</b> a un corso di cinese.", "Buen día, quisiera inscribirme a un curso de chino."],
                ["Bene, allora adesso facciamo l'iscrizione. Lei si chiama...?", "Bien, entonces ahora hacemos la inscripción. ¿Usted se llama...?"],
                ["Abita a Roma? — Sì.", "¿Vive en Roma? — Sí."],
                ["E qual è il Suo indirizzo? — Piazza Giuseppe Verdi 9.", "¿Y cuál es su dirección? — Piazza Giuseppe Verdi 9."],
                ["Il mio numero di telefono è...", "Mi número de teléfono es..."],
                ["E perché fa questo corso?", "¿Y por qué hace este curso?"]],
               [88, 82])
    s += nota("<b>vorrei</b> = quisiera. Es la forma amable de <i>volere</i> (condicional): se usa para pedir algo. "
              "<b>iscriversi</b> = inscribirse; es reflexivo como <i>chiamarsi</i>: <i>vorrei iscriver<b>mi</b></i>.")

    s += [h2("8. <i>Dieci domande personali</i> (pág. 35)")]
    s += tabla([["Informal", "Formal", "Informal", "Formal"],
                ["Dove abiti?", "Dove abita?", "Perché studi italiano?", "Perché studia italiano?"],
                ["Quanti anni hai?", "Quanti anni ha?", "Qual è il tuo numero?", "Qual è il Suo numero?"],
                ["Che lavoro fai?", "Che lavoro fa?", "Qual è la tua mail?", "Qual è la Sua mail?"],
                ["Dove lavori?", "Dove lavora?", "Qual è il tuo indirizzo?", "Qual è il Suo indirizzo?"],
                ["Che lingue parli?", "Che lingue parla?", "Sei sposato/a?", "È sposato/a?"]],
               [38, 38, 47, 47])
    s += nota("<b>sposato / sposata</b> = casado/a. Es la única de las diez que se responde con <i>sì / no</i>.")
    s += LETTURE[8]
    s += ascolta(ASCOLTA[8])
    s += ejercicios(ESERCIZI[8])
    s += tarea("pág. 143, ej. 8, 9 y 10 · pág. 193, ej. 17 y 18 · pág. 194, ej. 19 a 24 (el 22 es con audio).")
    # ================================================================ CLASE 9
    s += [h1("Clase 9 — 18/11"), info("Libro: Lezione 3 <i>Buon appetito!</i> · 3A <i>Al bar</i> (págs. 39–41)"),
          sec("En clase"),
          h2("1. La colazione (el desayuno)"),
          p("La sílaba fuerte va en MAYÚSCULA en la columna de pronunciación.")]
    s += [p("<b>Mangio</b> (como):")]
    s += pron([["il cornetto", "kor-NET-to", "medialuna"],
               ["la pasta", "PAS-ta", "factura (en el bar); también \"fideos\""],
               ["i biscotti", "bis-KOT-ti", "galletitas dulces"],
               ["i grissini · i cracker", "gris-SI-ni · KREK-ker", "grisines · galletitas saladas"],
               ["i cereali", "che-re-A-li", "cereales"],
               ["pane e burro", "PA-ne e BUR-ro", "pan y manteca"],
               ["lo yogurt", "IO-gurt", "yogur"],
               ["il panino", "pa-NI-no", "sándwich (pan con algo adentro)"],
               ["il toast", "TOST", "tostado"],
               ["l'uovo · le uova", "UO-vo · UO-va", "huevo · huevos"]])
    s += [p("<b>Bevo</b> (tomo):")]
    s += pron([["il caffè · l'espresso", "kaf-FÈ · es-PRES-so", "café (siempre es un espresso)"],
               ["il cappuccino", "kap-pu-CHI-no", "capuchino"],
               ["una tazza di latte", "TAT-tsa di LAT-te", "una taza de leche"],
               ["il tè", "TÈ", "té"],
               ["la spremuta", "spre-MU-ta", "exprimido fresco (de naranja)"],
               ["il succo", "SUK-ko", "jugo envasado, de botella"],
               ["il bicchiere d'acqua", "bik-KIE-re DAK-kua", "vaso de agua"]])
    s += [p("Ej.: <i>Un panino <b>con</b> prosciutto</i> (pro-SHUT-to) = un sándwich de jamón crudo. "
            "<i>A colazione mangio i biscotti e bevo un caffè.</i>")]
    s += corr("<i>A colazione mangio <b>un biscotto</b></i> (uno solo) o <i><b>i / dei</b> biscotti</i> (varios). "
              "\"Un biscotti\" mezcla singular y plural.")
    s += sapevi("el <b>Parmigiano Reggiano</b> (par-mi-YA-no re-DYA-no) tiene denominación de origen: solo se hace en Parma, Reggio Emilia, "
                "Modena y parte de Bologna y Mantova. <i>Parmesan</i> es el nombre que se usa fuera de Italia, muchas veces para imitaciones. "
                "Una rueda pesa unos 40 kg y madura mínimo 12 meses.")

    s += [h2("2. <i>Come stai?</i> (¿Cómo estás?)")]
    s += pron([["Benissimo!", "be-NIS-si-mo", "¡Buenísimo! (superlativo: -issimo = -ísimo)"],
               ["Molto bene", "MOL-to BE-ne", "Muy bien"],
               ["Bene", "BE-ne", "Bien"],
               ["Così così", "ko-SÌ ko-SÌ", "Más o menos (como el <i>so so</i> inglés)"],
               ["Male", "MA-le", "Mal"]])
    s += [p("<i>Come stai?</i> (informal) · <i>Come sta?</i> (formal) · <i>Come va?</i> (¿Cómo va?, sirve para los dos).")]
    s += nota("se responde agradeciendo la pregunta: <i>Bene, <b>grazie</b>. E tu?</i>")

    s += [h2("3. Cortesía: el italiano es más \"educado\"")]
    s += li("<b>per favore</b> y <b>grazie</b> se usan siempre, incluso entre amigos.",
            "<b>vorrei</b> (vor-REI) = quisiera: <i>Vorrei un caffè. · Vorrei farti una domanda</i> (= quisiera hacerte una pregunta).",
            "<b>voglio</b> (VO-llo) = quiero: para pedir algo <b>no se usa</b>, suena muy directo, casi maleducado.")

    s += [h2("4. Al bar: frases clave")]
    s += pron([["Che cosa prendi / prende?", "ke KO-sa PREN-di", "¿Qué tomás / toma?"],
               ["Per me un cappuccino.", "per ME", "Para mí un capuchino."],
               ["Io prendo un caffè.", "PREN-do", "Yo tomo un café."],
               ["Quant'è?", "kuan-TÈ", "¿Cuánto es?"],
               ["Offro io!", "OF-fro I-o", "¡Invito yo!"],
               ["Ecco...", "EK-ko", "Acá tenés / aquí está"],
               ["Dunque...", "DUN-kue", "Entonces... / bueno..."],
               ["Ma come?", "ma KO-me", "¿Pero cómo?"]],
              (50, 35, 85))
    s += nota("<b>Offro io</b>, con el sujeto al final, pone el énfasis en <i>io</i> (\"¡invito YO!\"). "
              "<b>Ecco</b> no tiene traducción exacta: sirve para mostrar o entregar algo (<i>Ecco il caffè!</i>). "
              "Y <b>come me</b> = \"como yo\": después de <i>come</i> y <i>per</i> va <b>me</b>, no <i>io</i> (<i>per me, come me</i>).")
    s += corr("es <b>caffettiera</b> (kaf-fet-TIE-ra), la cafetera. En el apunte quedó \"caffettera\".")
    s += sapevi("la cafetera italiana clásica es la <b>Moka</b>, inventada por Alfonso Bialetti en 1933. "
                "En casa los italianos toman café de moka; el espresso de máquina es del bar.")

    s += [h2("5. Euro y precios")]
    s += li("<b>euro</b> no cambia en plural: <i>un euro, due euro, dieci euro</i>.",
            "1 € = 100 <b>centesimi</b> (chen-TE-si-mi).")
    s += tabla([["Precio", "Se dice"],
                ["0,80 €", "ottanta centesimi"], ["1 €", "un euro"], ["2 €", "due euro"],
                ["2,50 €", "due euro e cinquanta (centesimi)"], ["8,70 €", "otto euro e settanta"]],
               [30, 90])

    s += [h2("6. Plural de los sustantivos")]
    s += tabla([["Singular", "Plural", "Regla", "Ejemplo"],
                ["-o (masc.)", "-i", "cambia", "il cornetto → i cornetti"],
                ["-e (masc. / fem.)", "-i", "cambia", "il bicchiere → i bicchieri · la lezione → le lezioni"],
                ["-a (fem.)", "-e", "cambia", "la cosa → le cose · la casa → le case"],
                ["acento final", "=", "no cambia", "il caffè → i caffè · la città → le città · l'università → le università"],
                ["consonante final / extranjeras", "=", "no cambia", "il bar → i bar · il toast → i toast · lo yogurt → gli yogurt"]],
               [38, 15, 22, 95])
    s += [p("Las palabras extranjeras se perciben como tales y no cambian: <i>il mate → i mate · l'asado → gli asado</i>.")]
    s += nota("el artículo sí cambia: <b>il → i · lo / l' (masc.) → gli · la / l' (fem.) → le</b>. "
              "<i>bicchieri</i> se pronuncia bik-KIE-ri: la <i>ch</i> suena \"k\".")

    s += [sec("Del libro"),
          h2("7. Verbo <i>prendere</i> (tomar) — regular en -ere")]
    s += tabla([["Persona", "prendere", "Se pronuncia", "Desinenza"],
                ["io", "prendo", "PREN-do", "-o"], ["tu", "prendi", "PREN-di", "-i"],
                ["lui / lei / Lei", "prende", "PREN-de", "<b>-e</b>"], ["noi", "prendiamo", "pren-DIA-mo", "-iamo"],
                ["voi", "prendete", "pren-DE-te", "<b>-ete</b>"], ["loro", "prendono", "PREN-do-no", "<b>-ono</b>"]],
               [35, 35, 35, 30])
    s += nota("comparado con <i>parlare</i> solo cambian tres terminaciones: <i>parla → prend<b>e</b> · parlate → prend<b>ete</b> · parlano → prend<b>ono</b></i>. "
              "<i>Prendere</i> es \"tomar\" en el bar: <i>prendo un caffè</i> (no se usa <i>bere</i> para pedir).")

    s += [h2("8. Diálogo <i>Al bar</i> (pág. 41)")]
    s += tabla([["Italiano", "Español"],
                ["Ciao Paolo! — Camilla, ciao! Come va? — Benissimo, e tu come stai? — Bene, grazie.",
                 "¡Hola Paolo! — ¡Camilla, hola! ¿Cómo va? — Buenísimo, ¿y vos cómo estás? — Bien, gracias."],
                ["Prendiamo un caffè? Hai tempo? — Sì, con piacere!", "¿Tomamos un café? ¿Tenés tiempo? — ¡Sí, con gusto!"],
                ["Un cornetto, per favore. Tu che cosa prendi?", "Una medialuna, por favor. ¿Vos qué tomás?"],
                ["Dunque... per me un cornetto e una pasta alla crema.", "Bueno... para mí una medialuna y una factura con crema."],
                ["Ma come, prendi due cose?! — Eh sì, ho fame!", "¿Pero cómo, pedís dos cosas?! — ¡Y sí, tengo hambre!"],
                ["E da bere cosa prendete? — Io prendo un caffè. — Per me un cappuccino.",
                 "¿Y de tomar qué piden? — Yo un café. — Para mí un capuchino."],
                ["E anche due bicchieri d'acqua. Quant'è? — Otto euro e settanta.",
                 "Y también dos vasos de agua. ¿Cuánto es? — Ocho euros con setenta."],
                ["Camilla, aspetta: offro io! — Oh, grazie mille!", "Camilla, esperá: ¡invito yo! — ¡Ay, muchas gracias!"]],
               [88, 82])
    s += nota("<b>ho fame</b> = tengo hambre (con <i>avere</i>, como en español). <b>da bere</b> = para tomar.")

    s += [h2("9. Listino prezzi — Bar Vesuvio (pág. 41)")]
    s += tabla([["Bevande (bebidas)", "€", "Dolce / Salato", "€"],
                ["caffè", "1,00", "cornetto", "1,50"], ["cappuccino", "1,50", "pasta", "2,00"],
                ["latte", "1,20", "panino", "3,10"], ["acqua", "0,50", "toast", "2,90"],
                ["tè · tè freddo", "1,80 · 2,50", "pizzetta", "2,40"], ["spremuta d'arancia", "3,50", "", ""],
                ["birra", "3,30", "", ""]],
               [45, 25, 40, 20])
    s += sapevi("el <b>Mont-Saint-Michel</b> (del ej. 8 de la tarea) es una isla rocosa en Normandía, Francia, con una abadía en la cima. "
                "Con la marea alta queda rodeado de agua; las mareas de esa bahía están entre las más grandes de Europa.")
    s += LETTURE[9]
    s += ascolta_qr(ASCOLTA_QR[9], "c9")
    s += ejercicios(ESERCIZI[9])
    s += tarea("pág. 36, Videocorso, ej. 1 a 4 (con el video) · pág. 38, Test de la Lezione 2 · pág. 195, ej. 1 a 5.")
    return s


if __name__ == "__main__":
    inicios = construir(portada() + clases() + VERBOS + soluciones(), "Italiano_carpeta.pdf", "Italiano — Carpeta de clases", "Italiano — Carpeta de clases")
    inicios = construir(portada(inicios) + clases() + VERBOS + soluciones(), "Italiano_carpeta.pdf", "Italiano — Carpeta de clases", "Italiano — Carpeta de clases")
    print("Inicios:", inicios)
