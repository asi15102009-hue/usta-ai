"""
foundation.py — Фундамент модулу (FR-001)
"""

from utils import validate_fields, ValidationError

FIELD_SPECS = {
    "length": "positive",
    "width": "positive",
    "height": "positive",
    "rebar_diameter": "positive",
    "rebar_count": "positive",
    "reserve": "nonnegative",
}

GRADE_TABLE = {
    "M100": {"cement": 160, "sand": 0.50, "gravel": 0.85},
    "M150": {"cement": 200, "sand": 0.48, "gravel": 0.80},
    "M200": {"cement": 240, "sand": 0.45, "gravel": 0.75},
    "M250": {"cement": 280, "sand": 0.43, "gravel": 0.72},
    "M300": {"cement": 320, "sand": 0.40, "gravel": 0.70},
    "M400": {"cement": 380, "sand": 0.38, "gravel": 0.65},
}


def calculate(data: dict) -> dict:
    errors = validate_fields(data, FIELD_SPECS)
    grade = data.get("grade", "M200")
    if grade not in GRADE_TABLE:
        errors["grade"] = "format"
    if errors:
        raise ValidationError(errors)

    length = float(data["length"])
    width = float(data["width"])
    height = float(data["height"])
    rebar_diameter = float(data["rebar_diameter"])
    rebar_count = float(data["rebar_count"])
    reserve = float(data["reserve"])
    fun_type = data.get("type", "lentalyk")

    g = GRADE_TABLE[grade]
    reserve_factor = 1 + reserve / 100

    base_volume = length * width * height
    total_volume = base_volume * reserve_factor
    cement_kg = total_volume * g["cement"]
    sand_m3 = total_volume * g["sand"]
    gravel_m3 = total_volume * g["gravel"]

    rebar_kg_per_m = 0.00617 * rebar_diameter ** 2
    rebar_total_length = rebar_count * length * reserve_factor
    rebar_kg = rebar_total_length * rebar_kg_per_m

    perimeter = 2 * (length + width)
    opalubka_m2 = perimeter * height * 2

    return {
        "type": fun_type,
        "grade": grade,
        "concrete_volume_m3": round(total_volume, 2),
        "cement_kg": round(cement_kg, 2),
        "sand_m3": round(sand_m3, 2),
        "gravel_m3": round(gravel_m3, 2),
        "rebar_kg": round(rebar_kg, 2),
        "opalubka_m2": round(opalubka_m2, 2),
    }