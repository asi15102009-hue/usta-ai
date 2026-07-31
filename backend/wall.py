"""
wall.py — Дубал модулу (FR-002)
"""

from utils import validate_fields, ValidationError

FIELD_SPECS = {
    "length": "positive",
    "height": "positive",
    "thickness": "positive",
    "seam": "nonnegative",
    "doors": "nonnegative",
    "windows": "nonnegative",
    "reserve": "nonnegative",
}

BLOCKS = {
    "kirpich": {"lm": 0.25, "hm": 0.065, "tm": 0.12, "binder": "mortar"},
    "pescoblok": {"lm": 0.39, "hm": 0.188, "tm": 0.19, "binder": "mortar"},
    "penoblok": {"lm": 0.60, "hm": 0.20, "tm": 0.30, "binder": "glue"},
    "gazoblok": {"lm": 0.60, "hm": 0.20, "tm": 0.30, "binder": "glue"},
    "shlakoblok": {"lm": 0.39, "hm": 0.188, "tm": 0.19, "binder": "mortar"},
}


def calculate(data: dict) -> dict:
    errors = validate_fields(data, FIELD_SPECS)
    material = data.get("material", "kirpich")
    if material not in BLOCKS:
        errors["material"] = "format"
    if errors:
        raise ValidationError(errors)

    length = float(data["length"])
    height = float(data["height"])
    thickness_mm = float(data["thickness"])
    seam_mm = float(data["seam"])
    doors = float(data["doors"])
    windows = float(data["windows"])
    reserve = float(data["reserve"])
    reserve_factor = 1 + reserve / 100

    b = BLOCKS[material]
    seam_m = seam_mm / 1000
    thickness_m = thickness_mm / 1000

    wall_area = max(length * height - doors - windows, 0)
    layers = max(1, -(-thickness_m // b["tm"]))
    layers = int(layers)
    face_area = (b["lm"] + seam_m) * (b["hm"] + seam_m)
    block_count = (wall_area * layers / face_area) * reserve_factor
    block_count = int(-(-block_count // 1))

    result = {
        "material": material,
        "wall_area_m2": round(wall_area, 2),
        "material_count_pcs": block_count,
        "mesh_area_m2": round(wall_area * 0.4 * reserve_factor, 2),
    }

    if b["binder"] == "mortar":
        mortar_m3 = wall_area * thickness_m * 0.22 * reserve_factor
        result["mortar_volume_m3"] = round(mortar_m3, 3)
        result["binder_type"] = "mortar"
    else:
        glue_kg = wall_area * layers * 1.4 * reserve_factor
        result["glue_weight_kg"] = round(glue_kg, 2)
        result["binder_type"] = "glue"

    return result