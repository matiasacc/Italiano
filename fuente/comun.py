"""Estilos y helpers comunes para la carpeta y el PDF de verbos."""
from copy import deepcopy
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm

AZUL = colors.HexColor("#1F3A5F")
GRIS = colors.HexColor("#F2F2F2")
LINEA = colors.HexColor("#BBBBBB")
ROJO = colors.HexColor("#AA3333")
VERDE = colors.HexColor("#2E7D32")

ss = getSampleStyleSheet()
T = ParagraphStyle("T", parent=ss["Title"], textColor=AZUL, fontSize=22, spaceAfter=4)
SUB = ParagraphStyle("SUB", parent=ss["Normal"], alignment=1, textColor=colors.grey, spaceAfter=14)
H1 = ParagraphStyle("H1", parent=ss["Heading1"], textColor=AZUL, fontSize=16, spaceBefore=0, spaceAfter=2)
INFO = ParagraphStyle("INFO", parent=ss["Normal"], textColor=colors.grey, fontSize=9.5, spaceAfter=8)
SEC = ParagraphStyle("SEC", parent=ss["Normal"], textColor=colors.white, backColor=AZUL,
                     fontName="Helvetica-Bold", fontSize=10, borderPadding=(3, 4, 3, 4),
                     spaceBefore=10, spaceAfter=6, keepWithNext=1)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], textColor=AZUL, fontSize=12.5,
                    spaceBefore=9, spaceAfter=4, keepWithNext=1)
P = ParagraphStyle("P", parent=ss["Normal"], fontSize=10.5, leading=14, spaceAfter=4)
B = ParagraphStyle("B", parent=P, leftIndent=12, bulletIndent=2)
C = ParagraphStyle("C", parent=P, spaceAfter=0, fontSize=10, leading=13)


def h1(t): return Paragraph(t, H1)
def info(t): return Paragraph(t, INFO)
def sec(t): return Paragraph(t.upper(), SEC)
def h2(t): return Paragraph(t, H2)
def p(t): return Paragraph(t, P)
def li(*items): return [Paragraph(i, B, bulletText="•") for i in items]


def tabla(filas, anchos, encabezado=True):
    data = [[Paragraph(str(c), C) for c in f] for f in filas]
    if encabezado:
        data[0] = [Paragraph(f"<b>{c}</b>", C) for c in filas[0]]
    t = Table(data, colWidths=[a * mm for a in anchos], hAlign="LEFT", repeatRows=1 if encabezado else 0)
    st = [("GRID", (0, 0), (-1, -1), 0.4, LINEA),
          ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]
    if encabezado:
        st.append(("BACKGROUND", (0, 0), (-1, 0), GRIS))
    t.setStyle(TableStyle(st))
    return [t, Spacer(1, 6)]


def caja(titulo, texto, color=AZUL):
    t = Table([[Paragraph(f"<b>{titulo}</b> {texto}", C)]], colWidths=[170 * mm], hAlign="LEFT")
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.6, color),
                           ("LINEBEFORE", (0, 0), (0, -1), 3, color),
                           ("LEFTPADDING", (0, 0), (-1, -1), 8),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return [t, Spacer(1, 6)]


def nota(t): return caja("Nota:", t)
def corr(t): return caja("Corrección:", t, ROJO)
def tarea(t): return caja("Tarea:", t, colors.grey)
def sapevi(t): return caja("Lo sapevi?", t, VERDE)


def pie_factory(texto):
    def pie(c, d):
        c.saveState()
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.grey)
        c.drawString(20 * mm, 12 * mm, texto)
        c.drawRightString(190 * mm, 12 * mm, f"{d.page}")
        c.restoreState()
    return pie


class Doc(SimpleDocTemplate):
    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name == "H1":
            self.inicios.append(self.page)


def construir(story, archivo, titulo, pie_txt, impar=True):
    """Cada H1 arranca en página nueva; con impar=True, en página impar (doble faz)."""
    pie = pie_factory(pie_txt)

    def armar(blancos):
        out, n = [], 0
        for f in story:
            if isinstance(f, Paragraph) and f.style.name == "H1":
                if n > 0:
                    out.append(PageBreak())
                    if blancos.get(n):
                        out += [Spacer(1, 1), PageBreak()]
                n += 1
            out.append(deepcopy(f))
        return out

    blancos = {}
    for _ in range(30):
        doc = Doc(archivo, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
                  topMargin=18 * mm, bottomMargin=20 * mm, title=titulo)
        doc.inicios = []
        doc.build(armar(blancos), onFirstPage=pie, onLaterPages=pie)
        pares = [i for i, pg in enumerate(doc.inicios) if pg % 2 == 0] if impar else []
        if not pares:
            break
        blancos[pares[0]] = True
    return doc.inicios


def qr_img(url, nombre, size=20 * mm):
    """Genera un QR en qr/<nombre>.png y devuelve el flowable Image."""
    import os
    import qrcode
    from reportlab.platypus import Image
    os.makedirs("qr", exist_ok=True)
    ruta = f"qr/{nombre}.png"
    qrcode.make(url, border=1).save(ruta)
    return Image(ruta, width=size, height=size)


def pron(filas, anchos=(45, 45, 80)):
    """Tabla Italiano | Se pronuncia | Español (sílaba fuerte en mayúscula)."""
    return tabla([["Italiano", "Se pronuncia", "Español"]] + filas, list(anchos))
