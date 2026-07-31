"""
pdf.py — PDF отчет генерациясы (FR-004 / SRS 13-бөлүм)
"""

import io
import os

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from labels import MODULES, COMMON, UNITS

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "fonts")
FONT_REGULAR = "DejaVuSans"
FONT_BOLD = "DejaVuSans-Bold"

_FONTS_REGISTERED = False


def _register_fonts():
    global _FONTS_REGISTERED
    if _FONTS_REGISTERED:
        return
    pdfmetrics.registerFont(TTFont(FONT_REGULAR, os.path.join(ASSETS_DIR, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont(FONT_BOLD, os.path.join(ASSETS_DIR, "DejaVuSans-Bold.ttf")))
    _FONTS_REGISTERED = True


def build_input_rows(module: str, lang: str, raw_result: dict, original_inputs: dict) -> list:
    mod_labels = MODULES[module][lang]
    units = UNITS[lang]
    rows = []

    if module == "foundation":
        rows = [
            (mod_labels["fields"]["type"], mod_labels["type"].get(raw_result["type"], raw_result["type"])),
            (mod_labels["fields"]["grade"], raw_result["grade"]),
            (mod_labels["fields"]["length"], f"{original_inputs['length']} {units['m']}"),
            (mod_labels["fields"]["width"], f"{original_inputs['width']} {units['m']}"),
            (mod_labels["fields"]["height"], f"{original_inputs['height']} {units['m']}"),
            (mod_labels["fields"]["rebar_diameter"], f"{original_inputs['rebar_diameter']} {units['mm']}"),
            (mod_labels["fields"]["rebar_count"], f"{original_inputs['rebar_count']} {units['pcs']}"),
            (mod_labels["fields"]["reserve"], f"{original_inputs['reserve']} {units['pct']}"),
        ]
    elif module == "wall":
        rows = [
            (mod_labels["fields"]["material"], mod_labels["material"].get(raw_result["material"], raw_result["material"])),
            (mod_labels["fields"]["length"], f"{original_inputs['length']} {units['m']}"),
            (mod_labels["fields"]["height"], f"{original_inputs['height']} {units['m']}"),
            (mod_labels["fields"]["thickness"], f"{original_inputs['thickness']} {units['mm']}"),
            (mod_labels["fields"]["seam"], f"{original_inputs['seam']} {units['mm']}"),
            (mod_labels["fields"]["doors"], f"{original_inputs['doors']} {units['m2']}"),
            (mod_labels["fields"]["windows"], f"{original_inputs['windows']} {units['m2']}"),
            (mod_labels["fields"]["reserve"], f"{original_inputs['reserve']} {units['pct']}"),
        ]
    elif module == "roof":
        rows = [
            (mod_labels["fields"]["form"], mod_labels["form"].get(raw_result["form"], raw_result["form"])),
            (mod_labels["fields"]["material"], mod_labels["material"].get(raw_result["material"], raw_result["material"])),
            (mod_labels["fields"]["length"], f"{original_inputs['length']} {units['m']}"),
            (mod_labels["fields"]["width"], f"{original_inputs['width']} {units['m']}"),
            (mod_labels["fields"]["angle"], f"{original_inputs['angle']} {units['deg']}"),
            (mod_labels["fields"]["sves"], f"{original_inputs['sves']} {units['m']}"),
        ]
    return rows


def build_result_rows(module: str, lang: str, raw_result: dict) -> list:
    mod_labels = MODULES[module][lang]
    units = UNITS[lang]
    unit_map = {
        "concrete_volume_m3": "m3", "sand_m3": "m3", "gravel_m3": "m3", "mortar_volume_m3": "m3",
        "cement_kg": "kg", "rebar_kg": "kg", "glue_weight_kg": "kg",
        "opalubka_m2": "m2", "wall_area_m2": "m2", "mesh_area_m2": "m2", "total_area_m2": "m2",
        "covering_material_m2": "m2", "gidro_m2": "m2", "paro_m2": "m2",
        "reyka_m": "m", "stropila_length_m": "m", "konek_m": "m", "zhelob_m": "m",
        "material_count_pcs": "pcs", "stropila_count": "pcs",
    }
    rows = []
    for key, label in mod_labels["results"].items():
        if key not in raw_result:
            continue
        unit_key = unit_map.get(key, "")
        unit = units.get(unit_key, "")
        rows.append((label, f"{raw_result[key]} {unit}".strip()))
    return rows


def generate_pdf(module: str, lang: str, project_name: str, project_date: str,
                  raw_result: dict, original_inputs: dict) -> bytes:
    _register_fonts()
    lang = lang if lang in ("kg", "ru") else "kg"
    common = COMMON[lang]
    mod_labels = MODULES[module][lang]

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, topMargin=18 * mm, bottomMargin=18 * mm,
                             leftMargin=18 * mm, rightMargin=18 * mm)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("TitleKG", parent=styles["Title"], fontName=FONT_BOLD, fontSize=16, leading=20)
    meta_style = ParagraphStyle("MetaKG", parent=styles["Normal"], fontName=FONT_REGULAR, fontSize=11, leading=15)
    h_style = ParagraphStyle("HeadKG", parent=styles["Heading3"], fontName=FONT_BOLD, fontSize=12, spaceBefore=10, spaceAfter=6)
    note_style = ParagraphStyle("NoteKG", parent=styles["Normal"], fontName=FONT_REGULAR, fontSize=9.5, leading=13, textColor=colors.HexColor("#4C5A66"))

    elements = []
    elements.append(Paragraph(f"{common['pdf_title']} — {mod_labels['title']}", title_style))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(f"<b>{common['object']}:</b> {project_name or '—'}", meta_style))
    elements.append(Paragraph(f"<b>{common['date']}:</b> {project_date or '—'}", meta_style))
    elements.append(Spacer(1, 10))

    def make_table(rows, head_color):
        data = [[Paragraph(str(a), meta_style), Paragraph(str(b), meta_style)] for a, b in rows]
        t = Table(data, colWidths=[85 * mm, 85 * mm])
        t.setStyle(TableStyle([
            ("FONTNAME", (0, 0), (-1, -1), FONT_REGULAR),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5DB")),
            ("BACKGROUND", (0, 0), (-1, -1), colors.white),
            ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, colors.HexColor("#F4F6F7")]),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 8),
            ("TOPPADDING", (0, 0), (-1, -1), 5),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ]))
        return t

    elements.append(Paragraph(common["params"], h_style))
    elements.append(make_table(build_input_rows(module, lang, raw_result, original_inputs), "#2B4B63"))

    elements.append(Paragraph(common["results"], h_style))
    elements.append(make_table(build_result_rows(module, lang, raw_result), "#C4441A"))

    elements.append(Paragraph(common["notes"], h_style))
    elements.append(Paragraph(mod_labels["note"], note_style))

    doc.build(elements)
    return buf.getvalue()