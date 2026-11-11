from comun import *

s = [h1("Anexo — Verbos"), info("Tabla de consulta. Se actualiza con cada clase.")]

# 1. MAPA
s += [Paragraph("1. Mapa de tiempos verbales", H2),
      p("Qué tiempos existen y cuáles vimos. Se completa a medida que avanzamos.")]
s += tabla([["Modo", "Tiempo", "Equivale en español", "Ej. (parlare)", "Visto"],
            ["Indicativo", "<b>presente</b>", "presente", "io parlo", "clase 5 y 7"],
            ["Indicativo", "passato prossimo", "pretérito (hablé / he hablado)", "io ho parlato", "(sono nato, clase 7)"],
            ["Indicativo", "imperfetto", "pretérito imperfecto", "io parlavo", ""],
            ["Indicativo", "futuro semplice", "futuro", "io parlerò", ""],
            ["Condizionale", "presente", "condicional", "io parlerei", ""],
            ["Congiuntivo", "presente", "subjuntivo", "che io parli", ""],
            ["Imperativo", "—", "imperativo", "parla!", ""]],
           [25, 30, 47, 30, 38])
s += sapevi("el <i>passato prossimo</i> se arma con <b>avere</b> o <b>essere</b> + participio "
            "(<i>ho parlato, sono nato</i>). Por eso conviene saber bien esos dos verbos desde ahora.")

# 2. PRESENTE REGULAR
s += [Paragraph("2. Presente indicativo — regulares en -are", H2),
      p("Verbo = <b>radice</b> (no cambia) + <b>desinenza</b> (cambia según la persona). Grupos: <b>-are, -ere, -ire</b>.")]
s += tabla([["Persona", "Desinenza", "parlare", "lavorare", "abitare"],
            ["io", "-o", "parlo", "lavoro", "abito"], ["tu", "-i", "parli", "lavori", "abiti"],
            ["lui / lei / Lei", "-a", "parla", "lavora", "abita"], ["noi", "-iamo", "parliamo", "lavoriamo", "abitiamo"],
            ["voi", "-ate", "parlate", "lavorate", "abitate"], ["loro", "-ano", "parlano", "lavorano", "abitano"]],
           [32, 25, 35, 35, 35])
s += sapevi("en <i>loro</i> el acento va en la raíz: <b>pà</b>rlano, lav<b>ò</b>rano, <b>à</b>bitano. "
            "Es un error típico de hispanohablantes decir \"parlanó\".")

s += [Paragraph("2.1 Casos especiales", H2)]
s += tabla([["", "CERCARE (-care)", "PAGARE (-gare)", "STUDIARE (-iare)", "MANGIARE (-giare)"],
            ["io", "cerco", "pago", "studio", "mangio"], ["tu", "cer<b>chi</b>", "pa<b>ghi</b>", "stud<b>i</b>", "mang<b>i</b>"],
            ["lui / lei / Lei", "cerca", "paga", "studia", "mangia"],
            ["noi", "cer<b>chiamo</b>", "pa<b>ghiamo</b>", "stud<b>iamo</b>", "mang<b>iamo</b>"],
            ["voi", "cercate", "pagate", "studiate", "mangiate"], ["loro", "cercano", "pagano", "studiano", "mangiano"]],
           [30, 35, 35, 35, 35])
s += li("<b>-care / -gare</b>: se agrega <b>h</b> delante de i (tu, noi) para mantener el sonido duro.",
        "<b>-iare</b>: la raíz ya termina en i, no se duplica.")

# 3. IRREGULARES
s += [Paragraph("3. Irregulares", H2), p("No siguen la regla: se aprenden de memoria.")]
s += tabla([["Persona", "ESSERE (ser / estar)", "AVERE (tener)", "FARE (hacer)"],
            ["io", "sono", "ho", "faccio"], ["tu", "sei", "hai", "fai"], ["lui / lei / Lei", "è", "ha", "fa"],
            ["noi", "siamo", "abbiamo", "facciamo"], ["voi", "siete", "avete", "fate"], ["loro", "sono", "hanno", "fanno"]],
           [35, 45, 45, 45])
s += tabla([["Verbo", "Usos vistos", "Ejemplo"],
            ["essere", "origen · nacionalidad · presentar · profesión", "Sono di Córdoba. · Questo è Juan. · Sono insegnante."],
            ["avere", "tener · <b>edad</b>", "Ho una penna. · Ho 30 anni."],
            ["fare", "hacer · <b>profesión</b>", "Che lavoro fai? · Faccio l'operaio."]],
           [22, 60, 88])
s += sapevi("la <b>h</b> de <i>ho, hai, ha, hanno</i> no suena: está para distinguirlos de "
            "<i>o</i> (o), <i>ai</i> (a los), <i>a</i> (a) y <i>anno</i> (año).")

# 4. REFLEXIVOS
s += [Paragraph("4. Reflexivos (-rsi)", H2), p("Van con pronombre antes del verbo, como en español (<i>me</i> llamo).")]
s += tabla([["Persona", "Pronombre", "chiamarsi"],
            ["io", "mi", "chiamo"], ["tu", "ti", "chiami"], ["lui / lei / Lei", "si", "chiama"],
            ["noi", "ci", "chiamiamo"], ["voi", "vi", "chiamate"], ["loro", "si", "chiamano"]],
           [35, 30, 35])

# 5. LISTA
s += [Paragraph("5. Lista de verbos", H2),
      p("Orden alfabético. Tipo: R = regular · I = irregular · Rf = reflexivo. Clase: donde apareció (162 = vocabulario del libro, pág. 162).")]
s += tabla([["Infinitivo", "Español", "Tipo", "Ejemplo", "Clase"],
            ["abitare", "vivir (en un lugar)", "R -are", "Abito a Roma.", "5"],
            ["amare", "amar", "R -are", "Amiamo l'Italia.", "5"],
            ["ascoltare", "escuchar", "R -are", "Ascolto la musica.", "162"],
            ["aspettare", "esperar", "R -are", "Aspetto l'autobus.", "162"],
            ["avere", "tener", "I", "Ho 30 anni.", "3"],
            ["cercare", "buscar", "R -care", "Tu cerchi un lavoro?", "5"],
            ["chiamarsi", "llamarse", "Rf", "Come ti chiami?", "1"],
            ["comprare", "comprar", "R -are", "Compro una pizza.", "162"],
            ["creare", "crear", "R -are", "Federico crea CoContest.", "7"],
            ["dire", "decir", "I", "Come si dice?", "4"],
            ["domandare", "preguntar", "R -are", "Domando all'insegnante.", "162"],
            ["essere", "ser / estar", "I", "Sono argentino.", "2"],
            ["fare", "hacer", "I", "Faccio l'operaio.", "6"],
            ["fermare", "parar, detener", "R -are", "—", "1"],
            ["guardare", "mirar", "R -are", "Guardo la TV.", "162"],
            ["insegnare", "enseñar", "R -are", "Insegna matematica.", "7"],
            ["lavorare", "trabajar", "R -are", "Lavoro in un ufficio.", "6"],
            ["mangiare", "comer", "R -giare", "Che cosa mangi?", "162"],
            ["pagare", "pagar", "R -gare", "Tu paghi.", "5"],
            ["parlare", "hablar", "R -are", "Parlo spagnolo.", "5"],
            ["pensare", "pensar", "R -are", "Penso a te.", "162"],
            ["potere", "poder", "I", "Può ripetere?", "4"],
            ["riempire", "llenar, completar", "-ire", "Riempi questo modulo.", "5"],
            ["ripetere", "repetir", "R -ere", "Può ripetere?", "4"],
            ["salutare", "saludar", "R -are", "Ti saluto.", "3"],
            ["scrivere", "escribir", "R -ere", "Come si scrive?", "4"],
            ["significare", "significar", "R -care", "Che significa?", "4"],
            ["studiare", "estudiar", "R -iare", "Studio italiano.", "5"],
            ["volere", "querer", "I", "Vuoi andare al bar?", "2"]],
           [27, 33, 20, 70, 15])
s += nota("<i>potere, volere, dire</i> son irregulares; los completamos cuando los veamos en clase. "
          "Los ejemplos de los verbos de la pág. 162 son míos, para fijar el significado.")

VERBOS = s
