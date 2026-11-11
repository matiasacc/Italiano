from comun import *


def lettura(titulo, cuerpo, glosario, domande, sap=None):
    s = [sec("Lettura"), h2(titulo)]
    for par in cuerpo:
        s.append(p(par))
    s += tabla([["Parola", "Significado"]] + glosario, [48, 122])
    s += [p("<b>Domande:</b>")] + [Paragraph(q, B, bulletText=f"{i+1}.") for i, q in enumerate(domande)]
    s.append(Spacer(1, 4))
    if sap:
        s += sapevi(sap)
    return s


def dialogo(lineas):
    return "<br/>".join(f"<b>{a}:</b> {b}" for a, b in lineas)


def esc(t):
    return f"<i>{t}</i>"


LETTURE = {
1: lettura("Alla stazione Termini, a Roma",
    [esc("Mattina. Stazione Termini, Roma. Una signora e un signore aspettano il treno."),
     dialogo([("Giulia", "Buongiorno!"), ("Marco", "Buongiorno, signora. Scusi, come si chiama?"),
              ("Giulia", "Mi chiamo Giulia Ferri. E Lei?"), ("Marco", "Marco Bianchi. Piacere!"),
              ("Giulia", "Piacere mio! Scusi, il treno per Firenze?"), ("Marco", "Binario otto."),
              ("Giulia", "Grazie! Arrivederci!"), ("Marco", "Arrivederci, signora!")]),
     esc("Pomeriggio. Due ragazzi al binario."),
     dialogo([("Luca", "Ciao! Io mi chiamo Luca. E tu, come ti chiami?"), ("Sofia", "Sofia."),
              ("Luca", "Come, scusa?"), ("Sofia", "Sofia. Esse – o – effe – i – a."),
              ("Luca", "Ah, Sofia! Piacere! Il tuo treno? Binario sedici?"), ("Sofia", "No, diciassette!"),
              ("Luca", "Il mio è il binario dodici. Ciao, Sofia! Buon viaggio!"), ("Sofia", "Grazie, ciao!")]),
     esc("Sera. Sofia è a Firenze e telefona alla mamma."),
     dialogo([("Mamma", "Pronto?"), ("Sofia", "Ciao, mamma! Sono Sofia."), ("Mamma", "Ciao, amore! Buonasera!"),
              ("Sofia", "Sono a Firenze. Tutto bene!"), ("Mamma", "Bene! Buonanotte, Sofia."),
              ("Sofia", "Buonanotte, mamma! Ciao ciao!")])],
    [["aspettare il treno", "esperar el tren"], ["il binario", "andén"], ["per Firenze", "para / hacia Florencia"],
     ["il tuo / il mio", "el tuyo / el mío"], ["Buon viaggio!", "¡Buen viaje!"], ["telefonare", "llamar por teléfono"],
     ["Pronto?", "¿Hola? (al atender el teléfono)"], ["Tutto bene!", "¡Todo bien!"]],
    ["¿Marco y Giulia se tratan de <i>tu</i> o de <i>Lei</i>? ¿Qué palabras lo muestran?",
     "¿Cómo se deletrea <i>Sofia</i>? ¿De qué andén sale su tren?",
     "¿Por qué Sofia y la mamma dicen <i>Buonanotte</i> y no <i>Buonasera</i> al final?"],
    "Roma Termini es la estación de tren más grande de Italia. Su nombre viene de las <i>Terme di Diocleziano</i>, "
    "unas termas romanas que están justo al lado. <i>Pronto?</i> significa literalmente \"¿listo?\": así se atiende el teléfono en Italia."),

2: lettura("Italiani famosi: di dove sono?",
    ["Leonardo da Vinci è italiano. È di Vinci, un piccolo paese vicino a Firenze. "
     "Galileo Galilei è di Pisa, la città della torre. Dante Alighieri è di Firenze. "
     "Cristoforo Colombo è di Genova. Maria Montessori è italiana, di Chiaravalle, nelle Marche. "
     "Sophia Loren è di Roma.",
     esc("Prima lezione in una scuola di lingue a Firenze."),
     dialogo([("Hans", "Ciao! Sono Hans. Sono tedesco, di Berlino. E tu?"),
              ("Mei", "Io sono Mei. Sono cinese, di Pechino. E lei? Di dov'è?"),
              ("Hans", "Lei è Katy. È americana, di Chicago."),
              ("Mei", "E l'insegnante? È di Firenze?"),
              ("Hans", "No, non è di Firenze. È italiano, ma è di Napoli."),
              ("Mei", "E tu, Pablo, sei spagnolo?"),
              ("Pablo", "No, non sono spagnolo! Sono argentino, di Córdoba.")]),
     "E Lionel Messi? Non è italiano: è argentino, di Rosario. E tu? Di dove sei? "
     "Io sono argentino, di Córdoba. Non sono italiano... ma studio l'italiano!"],
    [["piccolo / piccola", "pequeño/a"], ["il paese", "pueblo (y también país)"], ["vicino a", "cerca de"],
     ["la torre", "torre"], ["prima lezione", "primera clase"], ["ma", "pero"]],
    ["¿De dónde son Galileo y Colombo?", "¿El profesor es de Florencia? ¿De dónde es?",
     "Presentate como Pablo, en las dos formas (<i>di</i> + ciudad y nacionalidad)."],
    "<i>da Vinci</i> no es un apellido: significa \"de Vinci\", el pueblo donde nació Leonardo. "
    "En esa época mucha gente se identificaba por su lugar de origen."),

3: lettura("Una Vespa e uno zaino",
    ["Marco è uno studente di Pontedera, in Toscana. Ha diciannove anni e ha una Vespa: una Vespa blu, vecchia ma bellissima. "
     "Ogni mattina Marco va a scuola in Vespa.",
     "Nello zaino Marco ha un libro di inglese, un quaderno, una penna, una matita, un evidenziatore e un'agenda. "
     "E ha una chiave: la chiave della Vespa! Marco non ha un dizionario: ha una chiave USB con un dizionario.",
     esc("In classe, prima della lezione."),
     dialogo([("Anna", "Ciao, Marco! Hai una penna?"), ("Marco", "Sì, ho una penna e una matita. Ecco!"),
              ("Anna", "Grazie! E hai un dizionario?"), ("Marco", "No, non ho un dizionario. Ho una chiave USB!"),
              ("Anna", "Una chiave USB? Bravo! E la Vespa?"), ("Marco", "La Vespa è fuori. Ho uno zaino, una Vespa... e una lezione di inglese!")]),
     "A Pontedera c'è la fabbrica della Piaggio, e c'è anche un museo: il Museo Piaggio. "
     "Per Marco, la Vespa non è una moto: è un'amica."],
    [["blu", "azul"], ["vecchia", "vieja"], ["ogni mattina", "cada mañana"], ["va a scuola", "va a la escuela"],
     ["la chiave della Vespa", "la llave de la Vespa"], ["Ecco!", "¡Aquí tenés! / ¡Tomá!"], ["fuori", "afuera"],
     ["c'è", "hay (singular)"]],
    ["¿Cuántos años tiene Marco y de dónde es?", "Hacé la lista de lo que Marco tiene en la mochila, con su artículo.",
     "¿Marco tiene diccionario? ¿Qué tiene en su lugar?"],
    "Piaggio fabrica la Vespa en <b>Pontedera</b> desde 1946. Cuentan que, al ver el prototipo, "
    "Enrico Piaggio dijo <i>\"Sembra una vespa!\"</i> (\"¡Parece una avispa!\"), por la forma y por el ruido del motor."),

4: lettura("In un hotel a Venezia",
    [esc("Sera. Una turista arriva in un hotel vicino a Piazza San Marco."),
     dialogo([("Receptionist", "Buonasera, signora!"), ("Turista", "Buonasera. Ho una prenotazione."),
              ("Receptionist", "Come si chiama?"), ("Turista", "Ana López."),
              ("Receptionist", "Come, scusi? Può ripetere?"), ("Turista", "López. Elle – o – pi – e – zeta."),
              ("Receptionist", "Grazie. Lei è spagnola?"), ("Turista", "No, sono argentina, di Mendoza."),
              ("Receptionist", "Ha un documento, per favore?"), ("Turista", "Sì, il passaporto. Va bene?"),
              ("Receptionist", "Certo. Camera quattordici. Ecco la chiave."),
              ("Turista", "Grazie. Scusi, come si dice <i>góndola</i> in italiano?"),
              ("Receptionist", "Si dice <i>gondola</i>, con l'accento sulla o. Prego, e buona permanenza!")]),
     esc("La mattina dopo."),
     dialogo([("Turista", "Buongiorno! Scusi, ha una mappa di Venezia?"),
              ("Receptionist", "Buongiorno, signora López! Sì, ecco una mappa. Questo è il Canal Grande, questo è il Ponte di Rialto."),
              ("Turista", "E Piazza San Marco?"), ("Receptionist", "È qui, vicino all'hotel. Cinque minuti!"),
              ("Turista", "Perfetto, grazie mille!"), ("Receptionist", "Prego! Buona giornata!")]),
     "Venezia è una città speciale: non ha macchine. Ha canali, ponti e gondole. "
     "Il canale più famoso è il Canal Grande; il ponte più famoso è il Ponte di Rialto; "
     "la piazza più famosa è Piazza San Marco. A Venezia l'autobus è una barca: il vaporetto."],
    [["Certo.", "Claro."], ["Buona permanenza!", "¡Que disfrute la estadía!"], ["la mattina dopo", "a la mañana siguiente"],
     ["grazie mille", "muchísimas gracias"], ["Buona giornata!", "¡Que tenga un buen día!"], ["la macchina", "auto"],
     ["il ponte", "puente"], ["più famoso/a", "más famoso/a"], ["la barca", "barco, bote"]],
    ["Buscá en los diálogos todas las frases en registro formal (<i>Lei</i>).", "¿De dónde es la turista? ¿En qué habitación está?",
     "¿Por qué <i>la mappa</i> es un buen ejemplo de la clase 1?"],
    "Venecia está construida sobre más de 100 islas pequeñas en una laguna, unidas por más de 400 puentes. "
    "Las calles se llaman <i>calli</i> y en el centro histórico no circulan autos: todo se mueve a pie o en barco."),

5: lettura("Una studentessa a Bologna",
    ["Mi chiamo Valentina, ho ventiquattro anni e sono argentina, di Córdoba. "
     "Abito a Bologna e studio ingegneria all'università. Abito in un appartamento con due amiche, vicino a Piazza Maggiore.",
     "Perché studio a Bologna? Perché l'Università di Bologna è antichissima: è del 1088! "
     "È l'università più antica del mondo occidentale. E poi Bologna è bellissima: ha molti chilometri di portici "
     "e due torri famose, la Garisenda e la torre degli Asinelli. La torre degli Asinelli è alta quasi cento metri.",
     "Parlo spagnolo, inglese e un po' di italiano. Il mio amico Matteo è di Bologna: parla molto, mangia molto e ama la sua città.",
     dialogo([("Matteo", "Valentina, quanti anni hai?"), ("Valentina", "Ventiquattro. E tu?"),
              ("Matteo", "Ventisei. Perché studi ingegneria?"), ("Valentina", "Perché amo le macchine e le moto. E tu, che cosa studi?"),
              ("Matteo", "Studio lettere. Ma lavoro anche: il sabato faccio il cameriere."),
              ("Valentina", "Studi e lavori? Bravo!")]),
     "E tu, che lingue parli? Perché studi l'italiano?"],
    [["l'appartamento", "departamento"], ["antichissima", "antiquísima"], ["e poi", "y además"],
     ["i portici", "soportales, galerías cubiertas"], ["alta quasi cento metri", "de casi cien metros de alto"],
     ["un po' di", "un poco de"], ["molto", "mucho"], ["lettere", "Letras (la carrera)"], ["il sabato", "los sábados"]],
    ["¿Cuántos años tiene Valentina, de dónde es y qué estudia?", "Nombrá dos razones por las que estudia en Bologna.",
     "Respondé vos: <i>Quanti anni hai? Che lingue parli? Perché studi l'italiano?</i>"],
    "a Bologna la llaman <i>la Dotta, la Grassa e la Rossa</i>: \"la Docta\" por la universidad, "
    "\"la Gorda\" por la comida (de ahí la salsa <i>bolognese</i>, que allá se llama <i>ragù</i>) y \"la Roja\" por el color de sus techos. "
    "Sus pórticos son Patrimonio de la UNESCO desde 2021."),

6: lettura("La Motor Valley",
    ["Luca abita a Modena, in Emilia-Romagna. Ha trentadue anni e fa l'operaio in una fabbrica famosa: la Ferrari, a Maranello. "
     "Sua sorella Chiara è ingegnere: lavora alla Ducati, a Bologna, e disegna le moto.",
     "Enzo Ferrari è di Modena. Da giovane fa il pilota, poi fonda la sua azienda. "
     "Il simbolo della Ferrari è il cavallino rampante, nero su sfondo giallo: il giallo è il colore di Modena.",
     esc("Un giornalista intervista Luca davanti alla fabbrica."),
     dialogo([("Giornalista", "Buongiorno! Lei lavora qui?"), ("Luca", "Sì, faccio l'operaio alla Ferrari."),
              ("Giornalista", "Un lavoro interessante?"), ("Luca", "Sì, molto! La Ferrari è la passione di tutta l'Italia."),
              ("Giornalista", "E la Sua famiglia?"), ("Luca", "Mio padre fa il meccanico, mia madre è insegnante. E mia sorella fa l'ingegnere alla Ducati."),
              ("Giornalista", "Una famiglia di motori!"), ("Luca", "Sì! Qui in Emilia-Romagna i motori sono una tradizione.")]),
     "Anche Ferruccio Lamborghini è di questa zona. Prima fa i trattori, poi fa le macchine sportive. "
     "Ferrari, Lamborghini, Maserati, Ducati: tutte qui, in pochi chilometri."],
    [["sua sorella", "su hermana"], ["l'ingegnere", "el / la ingeniero/a"], ["disegnare", "diseñar, dibujar"],
     ["da giovane", "de joven"], ["fondare", "fundar"], ["il cavallino rampante", "el caballito rampante"],
     ["lo sfondo giallo", "el fondo amarillo"], ["il meccanico", "mecánico"], ["mio padre / mia madre", "mi padre / mi madre"],
     ["il trattore", "tractor"]],
    ["¿Dónde trabaja Luca y qué hace? ¿Y Chiara?", "¿Por qué el fondo del escudo de Ferrari es amarillo?",
     "Decí tu trabajo con las dos formas: <i>Faccio...</i> / <i>Sono...</i>"],
    "a esta zona de Emilia-Romagna la llaman <b>Motor Valley</b>: ahí están Ferrari (Maranello), Lamborghini "
    "(Sant'Agata Bolognese), Maserati (Modena) y Ducati (Borgo Panigale, Bologna). "
    "Lamborghini fabricaba tractores antes de hacer autos deportivos."),

7: lettura("I trulli di Alberobello",
    ["Siamo in Puglia, nel sud dell'Italia: il \"tacco\" dello stivale. Ad Alberobello ci sono case molto speciali: i trulli. "
     "I trulli sono case bianche, di pietra, con il tetto a cono. Sul tetto spesso ci sono simboli dipinti.",
     "Io e Giulia abitiamo a Bari, ma lavoriamo ad Alberobello: facciamo i camerieri in un ristorante dentro un trullo. "
     "Ogni giorno i turisti arrivano da tutto il mondo: amano i trulli, fanno molte foto e mangiano le orecchiette, la pasta tipica della Puglia.",
     dialogo([("Turista", "Scusate, voi abitate in un trullo?"), ("Giulia", "No, abitiamo a Bari, in un appartamento. Ma lavoriamo qui!"),
              ("Turista", "E i trulli sono antichi?"), ("Giulia", "Sì, molti trulli hanno più di duecento anni."),
              ("Turista", "E voi siete di Alberobello?"), ("Giulia", "No, siamo di Lecce. E voi, di dove siete?"),
              ("Turista", "Siamo argentini, di Córdoba. Abitiamo in una casa normale... senza tetto a cono!")]),
     "La Puglia non ha solo i trulli: ha il mare, Lecce con le sue chiese barocche e Polignano a Mare, "
     "la città di Domenico Modugno, il cantante di <i>Volare</i>."],
    [["il tacco dello stivale", "el taco de la bota"], ["ci sono", "hay (plural)"], ["la casa / le case", "casa / casas"],
     ["la pietra", "piedra"], ["il tetto a cono", "techo en forma de cono"], ["dipinto", "pintado"],
     ["dentro", "adentro de"], ["da tutto il mondo", "de todo el mundo"], ["Scusate", "Disculpen (a varios)"],
     ["senza", "sin"], ["la chiesa", "iglesia"]],
    ["¿En qué región está Alberobello y cómo son los trulli?", "¿Dónde viven y dónde trabajan Giulia y su compañero?",
     "Buscá en el texto todos los verbos en plural (noi, voi, loro) y escribí su infinitivo."],
    "los trulli de Alberobello son Patrimonio de la Humanidad de la UNESCO desde 1996. "
    "Se construían en piedra seca, sin argamasa."),
}
