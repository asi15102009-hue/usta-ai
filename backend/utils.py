"""
utils.py
Жалпы валидация жардамчылары. Бардык модулдар (foundation, wall, roof)
ушул жерден validate_fields функциясын колдонушат.
"""


class ValidationError(Exception):
    """Талаа деңгээлиндеги ката коду менен көтөрүлөт: {"length": "required", ...}"""

    def __init__(self, errors: dict):
        self.errors = errors
        super().__init__(str(errors))


def parse_number(value):
    if value is None:
        return None
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return None


def validate_fields(data: dict, field_specs: dict) -> dict:
    errors = {}
    for field, kind in field_specs.items():
        raw = data.get(field)
        if raw is None or str(raw).strip() == "":
            errors[field] = "required"
            continue
        val = parse_number(raw)
        if val is None:
            errors[field] = "format"
            continue
        if kind == "positive" and val <= 0:
            errors[field] = "positive"
        elif kind == "nonnegative" and val < 0:
            errors[field] = "positive"
    return errors


def as_float(data: dict, field: str) -> float:
    return float(data[field])