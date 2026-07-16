from pathlib import Path
import math
import textwrap

import pandas as pd
from scipy import stats

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    KeepTogether,
)
from reportlab.graphics.shapes import Circle, Drawing, Line, Polygon, Rect, String, Wedge


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "datos_encuesta_milton_80.csv"
PDF_PATH = BASE_DIR / "TABULACION_INTERPRETACION_DATOS_MILTON.pdf"

ACCENT_REPLACEMENTS = {
    "Tabulacion": "Tabulaci\u00f3n",
    "tabulacion": "tabulaci\u00f3n",
    "interpretacion": "interpretaci\u00f3n",
    "Interpretacion": "Interpretaci\u00f3n",
    "academico": "acad\u00e9mico",
    "academica": "acad\u00e9mica",
    "tecnologica": "tecnol\u00f3gica",
    "tecnologicos": "tecnol\u00f3gicos",
    "tecnologia": "tecnolog\u00eda",
    "motivacion": "motivaci\u00f3n",
    "Motivacion": "Motivaci\u00f3n",
    "disposicion": "disposici\u00f3n",
    "asociacion": "asociaci\u00f3n",
    "desviacion": "desviaci\u00f3n",
    "Desviacion": "Desviaci\u00f3n",
    "proposito": "prop\u00f3sito",
    "Proposito": "Prop\u00f3sito",
    "retencion": "retenci\u00f3n",
    "Retencion": "Retenci\u00f3n",
    "aplicacion": "aplicaci\u00f3n",
    "Aplicacion": "Aplicaci\u00f3n",
    "explicacion": "explicaci\u00f3n",
    "concentracion": "concentraci\u00f3n",
    "Concentracion": "Concentraci\u00f3n",
    "participacion": "participaci\u00f3n",
    "Participacion": "Participaci\u00f3n",
    "evaluacion": "evaluaci\u00f3n",
    "Evaluacion": "Evaluaci\u00f3n",
    "planificacion": "planificaci\u00f3n",
    "Planificacion": "Planificaci\u00f3n",
    "investigacion": "investigaci\u00f3n",
    "Investigacion": "Investigaci\u00f3n",
    "comprension": "comprensi\u00f3n",
    "Comprension": "Comprensi\u00f3n",
    "relacion": "relaci\u00f3n",
    "Relacion": "Relaci\u00f3n",
    "educacion": "educaci\u00f3n",
    "Pedagogico": "Pedag\u00f3gico",
    "pedagogico": "pedag\u00f3gico",
    "didactico": "did\u00e1ctico",
    "sistematica": "sistem\u00e1tica",
    "analisis": "an\u00e1lisis",
    "Analisis": "An\u00e1lisis",
    "numero": "n\u00famero",
    "Autonoma": "Aut\u00f3noma",
    "Informacion": "Informaci\u00f3n",
    "Comunicacion": "Comunicaci\u00f3n",
    "Metodo": "M\u00e9todo",
    "categorica": "categ\u00f3rica",
    "Sintesis": "S\u00edntesis",
    "Tecnologias": "Tecnolog\u00edas",
    "categoria": "categor\u00eda",
    "Categoria": "Categor\u00eda",
    "percepcion": "percepci\u00f3n",
    "percepcion": "percepci\u00f3n",
    "Distribucion": "Distribuci\u00f3n",
    "Comparacion": "Comparaci\u00f3n",
    "correlaci\u00f3nes": "correlaciones",
    "Graficas": "Gr\u00e1ficas",
    "Grafica": "Gr\u00e1fica",
    "grafica": "gr\u00e1fica",
    "especificos": "espec\u00edficos",
    "podia": "pod\u00eda",
    "mas": "m\u00e1s",
    "Mas": "M\u00e1s",
    "Interes": "Inter\u00e9s",
    "interes": "inter\u00e9s",
    "Atencion": "Atenci\u00f3n",
    "atencion": "atenci\u00f3n",
    "Valoracion": "Valoraci\u00f3n",
    "valoracion": "valoraci\u00f3n",
    "dimension": "dimensi\u00f3n",
    "Dimension": "Dimensi\u00f3n",
    "Expresion": "Expresi\u00f3n",
    "expresion": "expresi\u00f3n",
    "Presentacion": "Presentaci\u00f3n",
    "Presentacion/refuerzo": "Presentaci\u00f3n/refuerzo",
    "linea": "l\u00ednea",
    "dispersion": "dispersi\u00f3n",
    "distribucion": "distribuci\u00f3n",
}


LIKERT_LABELS = {
    1: "Totalmente en desacuerdo / muy bajo",
    2: "En desacuerdo / bajo",
    3: "Ni de acuerdo ni en desacuerdo / medio",
    4: "De acuerdo / alto",
    5: "Totalmente de acuerdo / muy alto",
}

FREQ_MAP = {
    "Nunca": 0.0,
    "1 vez": 1.0,
    "2-3 veces": 2.5,
    "4-5 veces": 4.5,
    "Más de 5 veces": 6.0,
}

QUESTION_SHORT = {
    "4- TIC en planificación": "Planificacion curricular",
    "5- TIC para investigar": "Investigacion de contenidos",
    "6- TIC para evaluar": "Evaluacion formativa",
    "7- TIC para presentar contenidos": "Presentacion/refuerzo",
    "8- TIC ayuda comprensión": "Comprension",
    "9- TIC facilita recordar": "Retencion",
    "10- TIC relaciona con vida diaria": "Relacion con vida diaria",
    "11- Aplicar en ejercicios distintos": "Aplicacion en ejercicios",
    "12- Explicar lo aprendido": "Expresion de lo aprendido",
    "13- Interés inicial": "Interes inicial",
    "14- Atención más que actividades tradicionales": "Atencion comparada",
    "15- Participación activa": "Participacion activa",
    "16- Mantiene concentración": "Concentracion",
    "17- Considera positivo TIC": "Valoracion positiva",
    "18- Aumenta deseo de aprender": "Deseo de aprender",
}

OBJECTIVES = [
    (
        "Objetivo 1. Disponibilidad tecnologica",
        "Determinar la disponibilidad de dispositivos tecnologicos funcionales en el aula.",
        ["1- Disponibilidad de dispositivos", "2- Dispositivos disponibles"],
    ),
    (
        "Objetivo 2. Frecuencia de uso",
        "Identificar la frecuencia semanal con que se emplean las TIC en las actividades escolares.",
        ["3- Frecuencia uso semanal"],
    ),
    (
        "Objetivo 3. Proposito pedagogico",
        "Analizar para que se integran las TIC en la planificacion, investigacion, evaluacion y presentacion de contenidos.",
        [
            "4- TIC en planificación",
            "5- TIC para investigar",
            "6- TIC para evaluar",
            "7- TIC para presentar contenidos",
        ],
    ),
    (
        "Objetivos 4 y 5. Rendimiento academico",
        "Valorar el impacto percibido de las TIC en la comprension, retencion, aplicacion y expresion del aprendizaje.",
        [
            "8- TIC ayuda comprensión",
            "9- TIC facilita recordar",
            "10- TIC relaciona con vida diaria",
            "11- Aplicar en ejercicios distintos",
            "12- Explicar lo aprendido",
        ],
    ),
    (
        "Objetivo 6. Persistencia del aprendizaje",
        "Examinar si el aprendizaje apoyado con TIC se mantiene y puede transferirse a otros ejercicios o explicaciones.",
        [
            "9- TIC facilita recordar",
            "11- Aplicar en ejercicios distintos",
            "12- Explicar lo aprendido",
        ],
    ),
    (
        "Objetivo 7. Interes inicial",
        "Medir el interes inicial que generan las TIC frente a la clase tradicional.",
        ["13- Interés inicial", "14- Atención más que actividades tradicionales"],
    ),
    (
        "Objetivo 8. Compromiso sostenido",
        "Evaluar la participacion activa y la concentracion durante actividades mediadas por TIC.",
        ["15- Participación activa", "16- Mantiene concentración"],
    ),
    (
        "Objetivo 9. Actitud positiva general",
        "Determinar la valoracion general y el deseo de aprender cuando se utilizan herramientas TIC.",
        ["17- Considera positivo TIC", "18- Aumenta deseo de aprender"],
    ),
]


def clean_text(value):
    if pd.isna(value):
        return ""
    return str(value).strip()


def accentize(value):
    text = str(value)
    for plain, accented in ACCENT_REPLACEMENTS.items():
        text = text.replace(plain, accented)
    return text


def likert_level(mean):
    if mean < 1.8:
        return "muy bajo"
    if mean < 2.6:
        return "bajo"
    if mean < 3.4:
        return "moderado"
    if mean < 4.2:
        return "alto"
    return "muy alto"


def corr_level(r):
    ar = abs(r)
    if ar < 0.20:
        return "muy debil"
    if ar < 0.40:
        return "debil"
    if ar < 0.60:
        return "moderada"
    if ar < 0.80:
        return "fuerte"
    return "muy fuerte"


def p_text(p):
    if p < 0.001:
        return "p < .001"
    return f"p = {p:.3f}"


def positive_pct(series):
    return (series.isin([4, 5]).mean() * 100).round(1)


def page_number(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 9)
    canvas.drawRightString(letter[0] - inch, letter[1] - 0.5 * inch, str(doc.page))
    canvas.restoreState()


def make_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="TitleAPA",
            parent=styles["Title"],
            fontName="Times-Bold",
            fontSize=16,
            leading=20,
            alignment=TA_CENTER,
            spaceAfter=18,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading1APA",
            parent=styles["Heading1"],
            fontName="Times-Bold",
            fontSize=13,
            leading=16,
            alignment=TA_CENTER,
            spaceBefore=12,
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Heading2APA",
            parent=styles["Heading2"],
            fontName="Times-Bold",
            fontSize=12,
            leading=15,
            alignment=TA_LEFT,
            spaceBefore=10,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="BodyAPA",
            parent=styles["BodyText"],
            fontName="Times-Roman",
            fontSize=11,
            leading=16,
            firstLineIndent=0.5 * inch,
            alignment=TA_LEFT,
            spaceAfter=6,
        )
    )
    styles.add(
        ParagraphStyle(
            name="NoIndent",
            parent=styles["BodyAPA"],
            firstLineIndent=0,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Note",
            parent=styles["BodyAPA"],
            firstLineIndent=0,
            fontSize=9,
            leading=12,
        )
    )
    return styles


def para(text, style):
    return Paragraph(accentize(text).replace("&", "&amp;"), style)


def table(data, col_widths=None, font_size=9, header=True):
    converted = []
    for row in data:
        converted.append([Paragraph(accentize(cell), ParagraphStyle("cell", fontName="Times-Roman", fontSize=font_size, leading=font_size + 2)) for cell in row])
    t = Table(converted, colWidths=col_widths, hAlign="LEFT", repeatRows=1 if header else 0)
    style = [
        ("FONT", (0, 0), (-1, -1), "Times-Roman", font_size),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, 0), 1, colors.black),
        ("LINEBELOW", (0, -1), (-1, -1), 0.8, colors.black),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        style.extend(
            [
                ("FONT", (0, 0), (-1, 0), "Times-Bold", font_size),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EFEFEF")),
            ]
        )
    t.setStyle(TableStyle(style))
    return t


def add_table_block(story, styles, number, title, rows, col_widths=None, note=None, font_size=9):
    story.append(para(f"<b>Tabla {number}</b>", styles["NoIndent"]))
    story.append(para(f"<i>{title}</i>", styles["NoIndent"]))
    story.append(table(rows, col_widths=col_widths, font_size=font_size))
    if note:
        story.append(para(f"<i>Nota.</i> {note}", styles["Note"]))
    story.append(Spacer(1, 8))


def horizontal_bar_drawing(labels, values, max_value, value_suffix="", value_decimals=1, width=455):
    row_h = 28
    left = 165
    bar_w = width - left - 55
    top = 18
    height = top + row_h * len(labels) + 24
    drawing = Drawing(width, height)
    palette = [
        colors.HexColor("#2F6B8F"),
        colors.HexColor("#6C8F3D"),
        colors.HexColor("#B65F2A"),
        colors.HexColor("#7A5C99"),
        colors.HexColor("#B28B21"),
        colors.HexColor("#3D7E70"),
    ]

    axis_y = height - top + 5
    drawing.add(Line(left, axis_y, left + bar_w, axis_y, strokeColor=colors.HexColor("#777777"), strokeWidth=0.5))
    for tick in [0, max_value / 2, max_value]:
        x = left + (tick / max_value) * bar_w
        drawing.add(Line(x, axis_y - 4, x, axis_y, strokeColor=colors.HexColor("#777777"), strokeWidth=0.5))
        drawing.add(String(x - 8, axis_y + 3, f"{tick:.0f}", fontName="Times-Roman", fontSize=7, fillColor=colors.HexColor("#555555")))

    for i, (label, value) in enumerate(zip(labels, values)):
        y = height - top - (i + 1) * row_h
        bar_len = max(0, min(value / max_value, 1)) * bar_w
        drawing.add(String(2, y + 6, accentize(label)[:38], fontName="Times-Roman", fontSize=8, fillColor=colors.black))
        drawing.add(Rect(left, y + 4, bar_w, 12, strokeColor=colors.HexColor("#D8D8D8"), fillColor=colors.HexColor("#F4F4F4"), strokeWidth=0.4))
        drawing.add(Rect(left, y + 4, bar_len, 12, strokeColor=palette[i % len(palette)], fillColor=palette[i % len(palette)], strokeWidth=0.4))
        value_text = f"{value:.{value_decimals}f}{value_suffix}"
        drawing.add(String(left + bar_len + 4, y + 6, value_text, fontName="Times-Roman", fontSize=8, fillColor=colors.black))

    return drawing


def vertical_bar_drawing(labels, values, max_value, value_suffix="", value_decimals=1, width=455, height=230):
    drawing = Drawing(width, height)
    left, bottom, top = 42, 58, 22
    chart_w, chart_h = width - left - 18, height - bottom - top
    palette = [
        colors.HexColor("#2F6B8F"),
        colors.HexColor("#6C8F3D"),
        colors.HexColor("#B65F2A"),
        colors.HexColor("#7A5C99"),
        colors.HexColor("#B28B21"),
        colors.HexColor("#3D7E70"),
    ]
    drawing.add(Line(left, bottom, left, bottom + chart_h, strokeColor=colors.black, strokeWidth=0.6))
    drawing.add(Line(left, bottom, left + chart_w, bottom, strokeColor=colors.black, strokeWidth=0.6))
    for tick in [0, max_value / 2, max_value]:
        y = bottom + (tick / max_value) * chart_h
        drawing.add(Line(left - 3, y, left + chart_w, y, strokeColor=colors.HexColor("#DDDDDD"), strokeWidth=0.4))
        drawing.add(String(12, y - 3, f"{tick:.0f}", fontName="Times-Roman", fontSize=7, fillColor=colors.HexColor("#555555")))

    slot = chart_w / max(len(labels), 1)
    bar_w = min(34, slot * 0.62)
    for i, (label, value) in enumerate(zip(labels, values)):
        x = left + i * slot + (slot - bar_w) / 2
        bar_h = max(0, min(value / max_value, 1)) * chart_h
        drawing.add(Rect(x, bottom, bar_w, bar_h, strokeColor=palette[i % len(palette)], fillColor=palette[i % len(palette)], strokeWidth=0.4))
        drawing.add(String(x - 3, bottom + bar_h + 4, f"{value:.{value_decimals}f}{value_suffix}", fontName="Times-Roman", fontSize=7))
        short = accentize(label)
        if len(short) > 14:
            short = short[:13] + "."
        drawing.add(String(x - 9, bottom - 16, short, fontName="Times-Roman", fontSize=7))

    return drawing


def grouped_bar_drawing(groups, series_names, series_values, max_value, value_decimals=1, width=455, height=240):
    drawing = Drawing(width, height)
    left, bottom, top = 48, 48, 24
    chart_w, chart_h = width - left - 90, height - bottom - top
    palette = [colors.HexColor("#2F6B8F"), colors.HexColor("#B65F2A"), colors.HexColor("#6C8F3D")]
    drawing.add(Line(left, bottom, left, bottom + chart_h, strokeColor=colors.black, strokeWidth=0.6))
    drawing.add(Line(left, bottom, left + chart_w, bottom, strokeColor=colors.black, strokeWidth=0.6))
    for tick in [0, max_value / 2, max_value]:
        y = bottom + (tick / max_value) * chart_h
        drawing.add(Line(left - 3, y, left + chart_w, y, strokeColor=colors.HexColor("#DDDDDD"), strokeWidth=0.4))
        drawing.add(String(14, y - 3, f"{tick:.0f}", fontName="Times-Roman", fontSize=7, fillColor=colors.HexColor("#555555")))

    group_slot = chart_w / max(len(groups), 1)
    bar_w = min(18, group_slot / (len(series_names) + 1))
    for gi, group in enumerate(groups):
        center = left + gi * group_slot + group_slot / 2
        start = center - (len(series_names) * bar_w) / 2
        for si, name in enumerate(series_names):
            value = series_values[si][gi]
            x = start + si * bar_w
            bar_h = max(0, min(value / max_value, 1)) * chart_h
            drawing.add(Rect(x, bottom, bar_w - 2, bar_h, strokeColor=palette[si % len(palette)], fillColor=palette[si % len(palette)], strokeWidth=0.4))
        drawing.add(String(center - 28, bottom - 16, accentize(group)[:18], fontName="Times-Roman", fontSize=7))

    legend_x = left + chart_w + 12
    for si, name in enumerate(series_names):
        y = bottom + chart_h - si * 16
        drawing.add(Rect(legend_x, y, 8, 8, fillColor=palette[si % len(palette)], strokeColor=palette[si % len(palette)]))
        drawing.add(String(legend_x + 12, y, accentize(name), fontName="Times-Roman", fontSize=7))
    return drawing


def pie_drawing(labels, values, width=455, height=210):
    drawing = Drawing(width, height)
    palette = [
        colors.HexColor("#2F6B8F"),
        colors.HexColor("#B65F2A"),
        colors.HexColor("#6C8F3D"),
        colors.HexColor("#7A5C99"),
        colors.HexColor("#B28B21"),
        colors.HexColor("#3D7E70"),
    ]
    total = sum(values) or 1
    cx, cy, radius = 120, 105, 72
    start = 90
    for i, (label, value) in enumerate(zip(labels, values)):
        angle = value / total * 360
        drawing.add(Wedge(cx, cy, radius, start, start + angle, fillColor=palette[i % len(palette)], strokeColor=colors.white, strokeWidth=1))
        start += angle

    legend_x, legend_y = 225, 150
    for i, (label, value) in enumerate(zip(labels, values)):
        y = legend_y - i * 22
        pct = value / total * 100
        drawing.add(Rect(legend_x, y, 10, 10, fillColor=palette[i % len(palette)], strokeColor=palette[i % len(palette)]))
        drawing.add(String(legend_x + 16, y + 1, f"{accentize(label)}: {pct:.1f}%", fontName="Times-Roman", fontSize=9))
    return drawing


def line_drawing(labels, values, max_value=5, width=455, height=220):
    drawing = Drawing(width, height)
    left, bottom, top = 45, 45, 22
    chart_w, chart_h = width - left - 28, height - bottom - top
    drawing.add(Line(left, bottom, left, bottom + chart_h, strokeColor=colors.black, strokeWidth=0.6))
    drawing.add(Line(left, bottom, left + chart_w, bottom, strokeColor=colors.black, strokeWidth=0.6))
    for tick in [0, max_value / 2, max_value]:
        y = bottom + (tick / max_value) * chart_h
        drawing.add(Line(left - 3, y, left + chart_w, y, strokeColor=colors.HexColor("#DDDDDD"), strokeWidth=0.4))
        drawing.add(String(15, y - 3, f"{tick:.0f}", fontName="Times-Roman", fontSize=7))
    points = []
    for i, value in enumerate(values):
        x = left + i * (chart_w / max(len(values) - 1, 1))
        y = bottom + (value / max_value) * chart_h
        points.append((x, y))
        drawing.add(Circle(x, y, 3.4, fillColor=colors.HexColor("#B65F2A"), strokeColor=colors.HexColor("#B65F2A")))
        drawing.add(String(x - 10, y + 8, f"{value:.2f}", fontName="Times-Roman", fontSize=7))
        drawing.add(String(x - 24, bottom - 15, accentize(labels[i])[:16], fontName="Times-Roman", fontSize=7))
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        drawing.add(Line(x1, y1, x2, y2, strokeColor=colors.HexColor("#2F6B8F"), strokeWidth=1.2))
    return drawing


def radar_drawing(labels, values, max_value=5, width=455, height=260):
    drawing = Drawing(width, height)
    cx, cy, radius = width / 2, height / 2 - 8, 82
    n = len(labels)
    for level in [1, 2, 3, 4, 5]:
        pts = []
        r = radius * level / max_value
        for i in range(n):
            angle = math.pi / 2 + 2 * math.pi * i / n
            pts.extend([cx + r * math.cos(angle), cy + r * math.sin(angle)])
        drawing.add(Polygon(pts, strokeColor=colors.HexColor("#DDDDDD"), fillColor=None, strokeWidth=0.5))
    for i, label in enumerate(labels):
        angle = math.pi / 2 + 2 * math.pi * i / n
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        drawing.add(Line(cx, cy, x, y, strokeColor=colors.HexColor("#DDDDDD"), strokeWidth=0.5))
        lx = cx + (radius + 28) * math.cos(angle)
        ly = cy + (radius + 28) * math.sin(angle)
        drawing.add(String(lx - 28, ly, accentize(label)[:18], fontName="Times-Roman", fontSize=7))
    data_pts = []
    for i, value in enumerate(values):
        angle = math.pi / 2 + 2 * math.pi * i / n
        r = radius * value / max_value
        data_pts.extend([cx + r * math.cos(angle), cy + r * math.sin(angle)])
    drawing.add(Polygon(data_pts, strokeColor=colors.HexColor("#2F6B8F"), fillColor=colors.Color(0.18, 0.42, 0.56, alpha=0.22), strokeWidth=1.2))
    return drawing


def stacked_likert_drawing(labels, rows, width=455):
    row_h = 26
    left = 132
    bar_w = width - left - 20
    height = 30 + row_h * len(labels) + 18
    drawing = Drawing(width, height)
    palette = [
        colors.HexColor("#B65F2A"),
        colors.HexColor("#D9A441"),
        colors.HexColor("#DCDCDC"),
        colors.HexColor("#8CA65A"),
        colors.HexColor("#2F6B8F"),
    ]
    for i, (label, values) in enumerate(zip(labels, rows)):
        y = height - 30 - (i + 1) * row_h
        drawing.add(String(2, y + 6, accentize(label)[:29], fontName="Times-Roman", fontSize=8))
        x = left
        total = sum(values) or 1
        for si, count in enumerate(values):
            seg_w = (count / total) * bar_w
            drawing.add(Rect(x, y + 4, seg_w, 12, fillColor=palette[si], strokeColor=colors.white, strokeWidth=0.4))
            x += seg_w
    legend = ["1", "2", "3", "4", "5"]
    for i, item in enumerate(legend):
        x = left + i * 30
        drawing.add(Rect(x, 8, 8, 8, fillColor=palette[i], strokeColor=palette[i]))
        drawing.add(String(x + 11, 8, item, fontName="Times-Roman", fontSize=7))
    return drawing


def scatter_drawing(x_values, y_values, x_label, y_label, width=455, height=230):
    drawing = Drawing(width, height)
    left, bottom, top = 48, 45, 22
    chart_w, chart_h = width - left - 24, height - bottom - top
    xmin, xmax = min(x_values), max(x_values)
    ymin, ymax = 1, 5
    if xmax == xmin:
        xmax = xmin + 1
    drawing.add(Line(left, bottom, left, bottom + chart_h, strokeColor=colors.black, strokeWidth=0.6))
    drawing.add(Line(left, bottom, left + chart_w, bottom, strokeColor=colors.black, strokeWidth=0.6))
    for tick in [ymin, 3, ymax]:
        y = bottom + ((tick - ymin) / (ymax - ymin)) * chart_h
        drawing.add(Line(left - 3, y, left + chart_w, y, strokeColor=colors.HexColor("#DDDDDD"), strokeWidth=0.4))
        drawing.add(String(18, y - 3, f"{tick:.0f}", fontName="Times-Roman", fontSize=7))
    for i, (xv, yv) in enumerate(zip(x_values, y_values)):
        jitter = ((i % 5) - 2) * 1.8
        x = left + ((xv - xmin) / (xmax - xmin)) * chart_w + jitter
        y = bottom + ((yv - ymin) / (ymax - ymin)) * chart_h
        drawing.add(Circle(x, y, 2.4, fillColor=colors.HexColor("#2F6B8F"), strokeColor=colors.HexColor("#2F6B8F")))

    slope, intercept, r, _, _ = stats.linregress(x_values, y_values)
    x1, x2 = xmin, xmax
    y1, y2 = intercept + slope * x1, intercept + slope * x2
    px1 = left
    px2 = left + chart_w
    py1 = bottom + ((y1 - ymin) / (ymax - ymin)) * chart_h
    py2 = bottom + ((y2 - ymin) / (ymax - ymin)) * chart_h
    drawing.add(Line(px1, py1, px2, py2, strokeColor=colors.HexColor("#B65F2A"), strokeWidth=1.2))
    drawing.add(String(left + chart_w - 58, bottom + chart_h - 12, f"r = {r:.3f}", fontName="Times-Roman", fontSize=8))
    drawing.add(String(left + chart_w / 2 - 35, 16, accentize(x_label), fontName="Times-Roman", fontSize=8))
    drawing.add(String(2, bottom + chart_h + 4, accentize(y_label), fontName="Times-Roman", fontSize=8))
    return drawing


def add_figure_block(story, styles, number, title, drawing, note):
    story.append(para(f"<b>Figura {number}</b>", styles["NoIndent"]))
    story.append(para(f"<i>{title}</i>", styles["NoIndent"]))
    story.append(drawing)
    story.append(para(f"<i>Nota.</i> {note}", styles["Note"]))
    story.append(Spacer(1, 10))


def progress_bar(value, maximum=100, width=160):
    filled = int(round((float(value) / maximum) * 20))
    return "[" + "#" * filled + "-" * (20 - filled) + f"] {float(value):.1f}%"


def main():
    df = pd.read_csv(CSV_PATH)
    df["disp_bin"] = df["1- Disponibilidad de dispositivos"].map({"Sí": 1, "Si": 1, "No": 0, "No sabe": 0}).fillna(0)
    df["freq_num"] = df["3- Frecuencia uso semanal"].map(FREQ_MAP)

    likert_cols = list(QUESTION_SHORT.keys())
    for col in likert_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    dimension_cols = {
        "proposito": [
            "4- TIC en planificación",
            "5- TIC para investigar",
            "6- TIC para evaluar",
            "7- TIC para presentar contenidos",
        ],
        "rendimiento": [
            "8- TIC ayuda comprensión",
            "9- TIC facilita recordar",
            "10- TIC relaciona con vida diaria",
            "11- Aplicar en ejercicios distintos",
            "12- Explicar lo aprendido",
        ],
        "persistencia": [
            "9- TIC facilita recordar",
            "11- Aplicar en ejercicios distintos",
            "12- Explicar lo aprendido",
        ],
        "motivacion": [
            "13- Interés inicial",
            "14- Atención más que actividades tradicionales",
            "15- Participación activa",
            "16- Mantiene concentración",
            "17- Considera positivo TIC",
            "18- Aumenta deseo de aprender",
        ],
        "actitud": [
            "17- Considera positivo TIC",
            "18- Aumenta deseo de aprender",
        ],
    }
    for name, cols in dimension_cols.items():
        df[name] = df[cols].mean(axis=1)

    correlations = [
        ("Disponibilidad TIC", "Rendimiento academico", "disp_bin", "rendimiento"),
        ("Disponibilidad TIC", "Motivacion estudiantil", "disp_bin", "motivacion"),
        ("Frecuencia de uso", "Rendimiento academico", "freq_num", "rendimiento"),
        ("Proposito pedagogico", "Rendimiento academico", "proposito", "rendimiento"),
        ("Motivacion", "Rendimiento academico", "motivacion", "rendimiento"),
    ]

    styles = make_styles()
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=letter,
        rightMargin=inch,
        leftMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
        title="Tabulacion e interpretacion de datos - Milton Raul Nova Gonzalez",
        author="Milton Raul Nova Gonzalez",
    )
    story = []

    story.append(para("Tabulacion e interpretacion de datos sobre el impacto de herramientas TIC en rendimiento academico y motivacion", styles["TitleAPA"]))
    story.append(Spacer(1, 20))
    for line in [
        "Milton Raul Nova Gonzalez",
        "Universidad Autonoma de Santo Domingo (UASD)",
        "Master en Tecnologias de Informacion y Comunicacion (TIC) para Docentes",
        "INF-8018-C9 Seminario de Investigacion TIC",
        "Periodo academico 2025-2026",
        "Fecha: 15 de julio de 2026",
    ]:
        story.append(para(line, styles["NoIndent"]))
    story.append(PageBreak())

    story.append(para("Resumen", styles["Heading1APA"]))
    story.append(
        para(
            "El presente informe tabula e interpreta los datos de una encuesta aplicada a 80 estudiantes de tercer grado en dos centros educativos. "
            "El analisis combina frecuencias, porcentajes, medias, desviaciones estandar y correlaciones de Pearson para responder nueve objetivos vinculados "
            "con disponibilidad tecnologica, frecuencia de uso, proposito pedagogico, rendimiento academico, persistencia del aprendizaje, interes, compromiso "
            "y actitud hacia las TIC. Los resultados muestran una disponibilidad TIC mayoritaria, un uso semanal moderado y efectos percibidos de nivel moderado "
            "sobre el rendimiento y la motivacion. La asociacion mas fuerte se observa entre disponibilidad TIC y motivacion, lo que sugiere que el acceso a recursos "
            "tecnologicos se relaciona con una mejor disposicion estudiantil hacia el aprendizaje, aunque los datos no permiten afirmar causalidad.",
            styles["NoIndent"],
        )
    )
    story.append(para("<i>Palabras clave:</i> TIC, rendimiento academico, motivacion, tercer grado, tabulacion de datos.", styles["NoIndent"]))
    story.append(PageBreak())

    story.append(para("Metodo de tabulacion", styles["Heading1APA"]))
    story.append(
        para(
            "La base de datos analizada corresponde al archivo datos_encuesta_milton_80.csv. Se usaron frecuencias absolutas, porcentajes, medias, desviaciones "
            "estandar y porcentajes positivos en escala Likert, considerando positivas las respuestas 4 y 5. Para la frecuencia semanal se asignaron valores "
            "numericos: Nunca = 0, 1 vez = 1, 2-3 veces = 2.5, 4-5 veces = 4.5 y Mas de 5 veces = 6. Las correlaciones se calcularon mediante Pearson.",
            styles["BodyAPA"],
        )
    )
    story.append(
        para(
            "Leyenda de interpretacion Likert: 1.00-1.79 = muy bajo; 1.80-2.59 = bajo; 2.60-3.39 = moderado; 3.40-4.19 = alto; 4.20-5.00 = muy alto. "
            "Leyenda de correlacion: |r| < .20 = muy debil; .20-.39 = debil; .40-.59 = moderada; .60-.79 = fuerte; .80-1.00 = muy fuerte.",
            styles["NoIndent"],
        )
    )

    n = len(df)
    center_counts = df["Centro educativo"].value_counts().reset_index()
    center_rows = [["Centro educativo", "Frecuencia", "Porcentaje"]]
    for _, row in center_counts.iterrows():
        center_rows.append([row["Centro educativo"], int(row["count"]), f"{row['count'] / n * 100:.1f}%"])
    add_table_block(story, styles, 1, "Distribucion de la muestra por centro educativo", center_rows, [240, 90, 90], f"n = {n}.")

    story.append(para("Resultados por objetivo", styles["Heading1APA"]))

    table_no = 2
    for title, objective_text, cols in OBJECTIVES:
        blocks = []
        blocks.append(para(title, styles["Heading2APA"]))
        blocks.append(para(objective_text, styles["BodyAPA"]))

        if cols == ["1- Disponibilidad de dispositivos", "2- Dispositivos disponibles"]:
            counts = df["1- Disponibilidad de dispositivos"].value_counts().reindex(["Sí", "No", "No sabe"]).fillna(0)
            rows = [["Respuesta", "Frecuencia", "Porcentaje", "Barra"]]
            for label, count in counts.items():
                pct = count / n * 100
                rows.append([label, int(count), f"{pct:.1f}%", progress_bar(pct)])
            blocks.append(para(f"<b>Tabla {table_no}</b>", styles["NoIndent"]))
            blocks.append(para("<i>Disponibilidad de dispositivos funcionales en el aula</i>", styles["NoIndent"]))
            blocks.append(table(rows, [95, 80, 80, 190], font_size=8))
            blocks.append(para("<i>Nota.</i> La categoria Si representa aulas con disponibilidad funcional reportada.", styles["Note"]))
            table_no += 1

            device_counts = {}
            for raw in df["2- Dispositivos disponibles"].dropna():
                for item in str(raw).split(","):
                    item = item.strip()
                    if item and item.lower() not in {"ninguno", "no sabe"}:
                        device_counts[item] = device_counts.get(item, 0) + 1
            device_rows = [["Dispositivo", "Menciones", "Porcentaje sobre n"]]
            for dev, count in sorted(device_counts.items(), key=lambda x: (-x[1], x[0])):
                device_rows.append([dev, count, f"{count / n * 100:.1f}%"])
            blocks.append(para(f"<b>Tabla {table_no}</b>", styles["NoIndent"]))
            blocks.append(para("<i>Tipos de dispositivos disponibles</i>", styles["NoIndent"]))
            blocks.append(table(device_rows, [180, 90, 120], font_size=8))
            blocks.append(para("<i>Nota.</i> La suma de menciones supera n porque una respuesta podia incluir varios dispositivos.", styles["Note"]))
            table_no += 1

            si_pct = counts.get("Sí", 0) / n * 100
            blocks.append(para(f"Interpretacion: el {si_pct:.1f}% de la muestra reporta disponibilidad de dispositivos, por lo que el objetivo se cumple en sentido favorable. Sin embargo, la presencia de respuestas No y No sabe evidencia una brecha de acceso que puede afectar la equidad del uso pedagogico de TIC.", styles["BodyAPA"]))

        elif cols == ["3- Frecuencia uso semanal"]:
            freq_counts = df["3- Frecuencia uso semanal"].value_counts().reindex(["Nunca", "1 vez", "2-3 veces", "4-5 veces", "Más de 5 veces"]).fillna(0)
            rows = [["Frecuencia semanal", "Frecuencia", "Porcentaje", "Valor asignado"]]
            for label, count in freq_counts.items():
                rows.append([label, int(count), f"{count / n * 100:.1f}%", FREQ_MAP[label]])
            mean = df["freq_num"].mean()
            sd = df["freq_num"].std()
            blocks.append(para(f"<b>Tabla {table_no}</b>", styles["NoIndent"]))
            blocks.append(para("<i>Frecuencia semanal de uso de TIC</i>", styles["NoIndent"]))
            blocks.append(table(rows, [135, 80, 80, 95], font_size=8))
            blocks.append(para(f"<i>Nota.</i> Media = {mean:.2f} usos por semana; DE = {sd:.2f}.", styles["Note"]))
            table_no += 1
            blocks.append(para(f"Interpretacion: la frecuencia media es de {mean:.2f} veces por semana, equivalente a un uso moderado. El resultado responde el objetivo indicando que las TIC no son marginales, pero todavia no parecen formar parte de una rutina diaria sistematica.", styles["BodyAPA"]))

        else:
            rows = [["Indicador", "Media", "DE", "% positivo", "Nivel"]]
            means = []
            positives = []
            for col in cols:
                mean = df[col].mean()
                sd = df[col].std()
                pos = positive_pct(df[col])
                means.append(mean)
                positives.append(pos)
                rows.append([QUESTION_SHORT[col], f"{mean:.2f}", f"{sd:.2f}", f"{pos:.1f}%", likert_level(mean)])
            general = pd.concat([df[col] for col in cols], axis=1).mean(axis=1)
            blocks.append(para(f"<b>Tabla {table_no}</b>", styles["NoIndent"]))
            blocks.append(para(f"<i>Indicadores asociados a {title.lower()}</i>", styles["NoIndent"]))
            blocks.append(table(rows, [170, 55, 55, 70, 75], font_size=8))
            blocks.append(para(f"<i>Nota.</i> Escala de 1 a 5. Media general = {general.mean():.2f}; DE general = {general.std():.2f}.", styles["Note"]))
            table_no += 1
            strongest = rows[1 + means.index(max(means))][0]
            weakest = rows[1 + means.index(min(means))][0]
            blocks.append(
                para(
                    f"Interpretacion: la media general fue {general.mean():.2f}, clasificada como nivel {likert_level(general.mean())}. "
                    f"El indicador mas alto fue {strongest}, mientras que el mas bajo fue {weakest}. En consecuencia, el objetivo se responde de forma "
                    f"{likert_level(general.mean())}, con fortalezas especificas y areas que requieren refuerzo pedagogico.",
                    styles["BodyAPA"],
                )
            )
        story.append(KeepTogether(blocks))

    story.append(PageBreak())
    story.append(para("Analisis correlacional", styles["Heading1APA"]))
    corr_rows = [["Relacion analizada", "r de Pearson", "Valor p", "Interpretacion"]]
    for x_label, y_label, x_col, y_col in correlations:
        subset = df[[x_col, y_col]].dropna()
        r, p = stats.pearsonr(subset[x_col], subset[y_col])
        corr_rows.append([f"{x_label} -> {y_label}", f"{r:.3f}", p_text(p), corr_level(r)])
    add_table_block(
        story,
        styles,
        table_no,
        "Correlaciones entre variables principales",
        corr_rows,
        [205, 70, 70, 90],
        "Las correlaciones describen asociacion estadistica y no demuestran causalidad.",
        font_size=8,
    )
    table_no += 1
    story.append(
        para(
            "El analisis correlacional indica que la disponibilidad TIC se asocia de manera fuerte con la motivacion y de manera moderada con el rendimiento academico. "
            "La frecuencia de uso y el proposito pedagogico mantienen relaciones positivas, aunque de menor magnitud. Estos resultados apoyan la idea central de que "
            "las herramientas tecnologicas favorecen el aprendizaje cuando existe acceso y cuando su uso responde a una intencion pedagogica clara.",
            styles["BodyAPA"],
        )
    )

    by_center = df.groupby("Centro educativo").agg(
        n=("Centro educativo", "size"),
        disponibilidad=("disp_bin", "mean"),
        frecuencia=("freq_num", "mean"),
        proposito=("proposito", "mean"),
        rendimiento=("rendimiento", "mean"),
        motivacion=("motivacion", "mean"),
        actitud=("actitud", "mean"),
    )
    center_rows = [["Centro", "n", "Disp. %", "Frec.", "Proposito", "Rend.", "Motiv.", "Actitud"]]
    for idx, row in by_center.iterrows():
        center_rows.append([
            idx,
            int(row["n"]),
            f"{row['disponibilidad'] * 100:.1f}%",
            f"{row['frecuencia']:.2f}",
            f"{row['proposito']:.2f}",
            f"{row['rendimiento']:.2f}",
            f"{row['motivacion']:.2f}",
            f"{row['actitud']:.2f}",
        ])
    add_table_block(
        story,
        styles,
        table_no,
        "Comparacion descriptiva por centro educativo",
        center_rows,
        [145, 30, 55, 50, 55, 50, 50, 50],
        "Las medias se interpretan en escala de 1 a 5, excepto disponibilidad y frecuencia.",
        font_size=7,
    )
    table_no += 1

    story.append(para("Respuesta integrada a los objetivos", styles["Heading1APA"]))
    response_rows = [["Objetivo", "Respuesta sintetica"]]
    response_rows.extend(
        [
            ["1", "Existe disponibilidad mayoritaria de TIC, aunque persiste una brecha de acceso que debe atenderse."],
            ["2", "El uso semanal es moderado; la tecnologia se utiliza, pero no de forma plenamente sistematica."],
            ["3", "El proposito pedagogico es moderado, con necesidad de fortalecer evaluacion, investigacion y planificacion intencional."],
            ["4-5", "El rendimiento academico percibido alcanza nivel moderado; las TIC ayudan, pero su efecto depende de la calidad del diseno didactico."],
            ["6", "La persistencia del aprendizaje es moderada, especialmente en retencion, transferencia y explicacion de lo aprendido."],
            ["7", "El interes inicial es favorable y se eleva cuando las actividades TIC se comparan con estrategias tradicionales."],
            ["8", "El compromiso sostenido es moderado; la participacion supera levemente la concentracion."],
            ["9", "La actitud general hacia las TIC es positiva-moderada y refleja disposicion a continuar aprendiendo con tecnologia."],
        ]
    )
    add_table_block(story, styles, table_no, "Sintesis de respuesta a los objetivos", response_rows, [60, 390], font_size=8)
    table_no += 1

    story.append(PageBreak())
    story.append(para("Graficas por objetivo", styles["Heading1APA"]))
    figure_no = 1

    center_labels = list(center_counts["Centro educativo"])
    center_values = [count / n * 100 for count in center_counts["count"]]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Distribucion porcentual de la muestra por centro educativo",
        pie_drawing(center_labels, center_values),
        "Grafica circular con la distribucion porcentual de la muestra antes de responder los objetivos especificos.",
    )
    figure_no += 1

    disp_counts = df["1- Disponibilidad de dispositivos"].value_counts().reindex(["Sí", "No", "No sabe"]).fillna(0)
    disp_labels = list(disp_counts.index)
    disp_values = [count / n * 100 for count in disp_counts.values]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 1: disponibilidad de dispositivos funcionales en el aula",
        pie_drawing(disp_labels, disp_values),
        "Grafica circular; los porcentajes se calcularon sobre la muestra total de 80 estudiantes.",
    )
    figure_no += 1

    device_counts = {}
    for raw in df["2- Dispositivos disponibles"].dropna():
        for item in str(raw).split(","):
            item = item.strip()
            if item and item.lower() not in {"ninguno", "no sabe"}:
                device_counts[item] = device_counts.get(item, 0) + 1
    device_labels = []
    device_values = []
    for dev, count in sorted(device_counts.items(), key=lambda x: (-x[1], x[0])):
        device_labels.append(dev)
        device_values.append(count / n * 100)
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 1: tipos de dispositivos disponibles",
        vertical_bar_drawing(device_labels, device_values, 100, "%", 1),
        "Grafica de barras verticales; una respuesta podia incluir varios dispositivos, por eso los porcentajes no suman 100%.",
    )
    figure_no += 1

    freq_counts = df["3- Frecuencia uso semanal"].value_counts().reindex(["Nunca", "1 vez", "2-3 veces", "4-5 veces", "Más de 5 veces"]).fillna(0)
    freq_labels = list(freq_counts.index)
    freq_values = [count / n * 100 for count in freq_counts.values]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 2: distribucion porcentual de la frecuencia semanal de uso TIC",
        vertical_bar_drawing(freq_labels, freq_values, 100, "%", 1),
        "Grafica de barras verticales; la categoria de mayor peso fue 4-5 veces por semana.",
    )
    figure_no += 1

    pedagogical_cols = [
        "4- TIC en planificación",
        "5- TIC para investigar",
        "6- TIC para evaluar",
        "7- TIC para presentar contenidos",
    ]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 3: medias del proposito pedagogico",
        radar_drawing([QUESTION_SHORT[col] for col in pedagogical_cols], [df[col].mean() for col in pedagogical_cols], 5),
        "Grafica radial en escala Likert de 1 a 5; muestra la intensidad media de cada uso pedagogico de las TIC.",
    )
    figure_no += 1

    performance_cols = [
        "8- TIC ayuda comprensión",
        "9- TIC facilita recordar",
        "10- TIC relaciona con vida diaria",
        "11- Aplicar en ejercicios distintos",
        "12- Explicar lo aprendido",
    ]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivos 4 y 5: medias de rendimiento academico percibido",
        vertical_bar_drawing([QUESTION_SHORT[col] for col in performance_cols], [df[col].mean() for col in performance_cols], 5, "", 2),
        "Grafica de barras verticales en escala Likert de 1 a 5; integra comprension, retencion, aplicacion y expresion del aprendizaje.",
    )
    figure_no += 1

    persistence_cols = [
        "9- TIC facilita recordar",
        "11- Aplicar en ejercicios distintos",
        "12- Explicar lo aprendido",
    ]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 6: persistencia del aprendizaje",
        line_drawing([QUESTION_SHORT[col] for col in persistence_cols], [df[col].mean() for col in persistence_cols], 5),
        "Grafica de linea; la persistencia se estima con indicadores de recuerdo, transferencia y explicacion de lo aprendido.",
    )
    figure_no += 1

    interest_cols = ["13- Interés inicial", "14- Atención más que actividades tradicionales"]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 7: interes inicial generado por las TIC",
        stacked_likert_drawing([QUESTION_SHORT[col] for col in interest_cols], [[int((df[col] == v).sum()) for v in [1, 2, 3, 4, 5]] for col in interest_cols]),
        "Grafica de barras apiladas Likert; los segmentos representan respuestas de 1 a 5.",
    )
    figure_no += 1

    engagement_cols = ["15- Participación activa", "16- Mantiene concentración"]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 8: compromiso sostenido durante actividades TIC",
        stacked_likert_drawing([QUESTION_SHORT[col] for col in engagement_cols], [[int((df[col] == v).sum()) for v in [1, 2, 3, 4, 5]] for col in engagement_cols]),
        "Grafica de barras apiladas Likert; el compromiso se representa mediante participacion activa y mantenimiento de la concentracion.",
    )
    figure_no += 1

    attitude_cols = ["17- Considera positivo TIC", "18- Aumenta deseo de aprender"]
    add_figure_block(
        story,
        styles,
        figure_no,
        "Objetivo 9: actitud positiva general hacia las TIC",
        stacked_likert_drawing([QUESTION_SHORT[col] for col in attitude_cols], [[int((df[col] == v).sum()) for v in [1, 2, 3, 4, 5]] for col in attitude_cols]),
        "Grafica de barras apiladas Likert; valores 4 y 5 reflejan mejor valoracion de las TIC y mayor deseo de aprender.",
    )
    figure_no += 1

    dimension_means = {
        "Proposito pedagogico": df["proposito"].mean(),
        "Rendimiento academico": df["rendimiento"].mean(),
        "Persistencia": df["persistencia"].mean(),
        "Motivacion": df["motivacion"].mean(),
        "Actitud positiva": df["actitud"].mean(),
    }
    add_figure_block(
        story,
        styles,
        figure_no,
        "Sintesis grafica de medias generales por dimension",
        radar_drawing(list(dimension_means.keys()), list(dimension_means.values()), 5),
        "Grafica radial en escala de 1 a 5; valores mas altos indican mejor percepcion del impacto de las TIC.",
    )
    figure_no += 1

    add_figure_block(
        story,
        styles,
        figure_no,
        "Relacion entre frecuencia de uso TIC y rendimiento academico",
        scatter_drawing(list(df["freq_num"]), list(df["rendimiento"]), "Frecuencia semanal", "Rendimiento"),
        "Grafica de dispersion con linea de tendencia; cada punto representa un estudiante.",
    )
    figure_no += 1

    corr_labels = []
    corr_values = []
    for x_label, y_label, x_col, y_col in correlations:
        subset = df[[x_col, y_col]].dropna()
        r, _ = stats.pearsonr(subset[x_col], subset[y_col])
        corr_labels.append(f"{x_label} / {y_label}".replace("Rendimiento academico", "Rendimiento").replace("Motivacion estudiantil", "Motivacion"))
        corr_values.append(r)
    add_figure_block(
        story,
        styles,
        figure_no,
        "Fuerza de las correlaciones principales",
        horizontal_bar_drawing(corr_labels, corr_values, 1, "", 3),
        "Grafica de barras horizontales; muestra la magnitud de los coeficientes r de Pearson positivos.",
    )
    figure_no += 1

    by_center_fig = df.groupby("Centro educativo").agg(
        rendimiento=("rendimiento", "mean"),
        motivacion=("motivacion", "mean"),
        actitud=("actitud", "mean"),
    )
    center_fig_labels = []
    center_fig_values = []
    for idx, row in by_center_fig.iterrows():
        short_center = "Federico" if "Federico" in idx else "Juan Bautista"
        for metric in ["rendimiento", "motivacion", "actitud"]:
            center_fig_labels.append(f"{short_center} - {metric.title()}")
            center_fig_values.append(row[metric])
    add_figure_block(
        story,
        styles,
        figure_no,
        "Comparacion de medias por centro educativo",
        grouped_bar_drawing(
            list(by_center_fig.index),
            ["Rendimiento", "Motivacion", "Actitud"],
            [
                list(by_center_fig["rendimiento"]),
                list(by_center_fig["motivacion"]),
                list(by_center_fig["actitud"]),
            ],
            5,
            2,
        ),
        "Grafica de barras agrupadas; las medias se interpretan en escala de 1 a 5.",
    )
    figure_no += 1

    story.append(para("Conclusion", styles["Heading1APA"]))
    story.append(
        para(
            "Los datos permiten concluir que las herramientas TIC tienen un impacto percibido moderado en el rendimiento academico y una relacion favorable con la motivacion "
            "de los estudiantes de tercer grado. La evidencia mas consistente es que la disponibilidad tecnologica se vincula con mejores niveles de motivacion y con una mejora "
            "moderada del rendimiento. No obstante, el hallazgo principal no debe entenderse como una defensa del uso tecnologico por si mismo, sino como una invitacion a integrar "
            "las TIC con objetivos pedagogicos definidos, frecuencia razonable, actividades de aplicacion y estrategias que sostengan la concentracion del estudiante.",
            styles["BodyAPA"],
        )
    )

    story.append(para("Limitaciones", styles["Heading1APA"]))
    story.append(
        para(
            "La muestra esta limitada a 80 estudiantes de dos centros educativos y los resultados se basan en percepciones reportadas en encuesta. Por tanto, las correlaciones "
            "no prueban causalidad y deben complementarse en investigaciones futuras con observaciones de aula, calificaciones reales, entrevistas y disenos comparativos o "
            "cuasi-experimentales.",
            styles["BodyAPA"],
        )
    )

    story.append(para("Referencia metodologica", styles["Heading1APA"]))
    story.append(
        para(
            "American Psychological Association. (2020). <i>Publication manual of the American Psychological Association</i> (7.ª ed.). American Psychological Association.",
            styles["NoIndent"],
        )
    )

    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
    print(PDF_PATH)


if __name__ == "__main__":
    main()
