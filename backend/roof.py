"""
roof.py — Чатыр модулу (FR-003)
"""

import math

from utils import validate_fields, ValidationError

FIELD_SPECS = {
    "length": "positive",
    "width": "positive",
    "angle": "positive",
    "sves": "nonnegative",
}

WASTE = {"metal": 0.05, "ondulin": 0.10, "shifer": 0.10, "cherepitsa": 0.07}
COMPLEX_FACTOR = {"L": 1.3, "G": 1.45, "T": 1.6}


def calculate(data: dict) -> dict:
    errors = validate_fields(data, FIELD_SPECS)
    form = data.get("form", "dvux")
    material = data.get("material", "metal")
    if material not in WASTE:
        errors["material"] = "format"
    if form not in ("odno", "dvux", "chetyre", "L", "G", "T"):
        errors["form"] = "format"
    if errors:
        raise ValidationError(errors)

    length = float(data["length"])
    width = float(data["width"])
    angle = float(data["angle"])
    sves = float(data["sves"])

    rad = math.radians(angle)
    slope = 1 / math.cos(rad)
    L = length + 2 * sves
    has_konek = True

    if form == "odno":
        total_area = L * (width + sves) * slope
        stropila_length = (width + sves) * slope
        has_konek = False
    elif form == "dvux":
        total_area = L * (width / 2 + sves) * slope * 2
        stropila_length = (width / 2 + sves) * slope
    elif form == "chetyre":
        total_area = L * (width + 2 * sves) * slope
        stropila_length = (width / 2 + sves) * slope
    else:
        factor = COMPLEX_FACTOR[form]
        total_area = L * (width / 2 + sves) * slope * 2 * factor
        stropila_length = (width / 2 + sves) * slope

    konek_m = length if has_konek else 0
    waste_pct = WASTE[material]
    covering_material_m2 = total_area * (1 + waste_pct)
    reyka_m = total_area * 2.86
    stropila_count = int(-(-L // 0.6)) + 1
    stropila_total_m = stropila_count * stropila_length
    zhelob_m = 2 * (length + width) + 4 * sves
    gidro_m2 = total_area * 1.15
    paro_m2 = total_area * 1.15

    return {
        "form": form,
        "material": material,
        "total_area_m2": round(total_area, 2),
        "covering_material_m2": round(covering_material_m2, 2),
        "reyka_m": round(reyka_m, 2),
        "stropila_count": stropila_count,
        "stropila_length_m": round(stropila_total_m, 2),
        "konek_m": round(konek_m, 2),
        "zhelob_m": round(zhelob_m, 2),
        "gidro_m2": round(gidro_m2, 2),
        "paro_m2": round(paro_m2, 2),
    }