"""
architect.py — "Архитектор" модулунун backend бөлүгү (MVP).

Бул модуль өз алдынча Flask Blueprint катары иштейт, учурдагы
foundation/wall/roof модулдарына такыр тийбейт.

MVP чөйрөсү (СРС 42-бөлүм боюнча):
  - долбоор каталогу (database'ден, hardcoded эмес)
  - текст + негизги key-word "интеллектуалдуу" издөө (чыныгы AI/семантикалык
    издөө эмес — бул кийинки этап, СРС 43-бөлүм)
  - dynamic фильтрлер (style, floors, features)
  - долбоор карточкалары/деталдары
  - editable долбоорлор үчүн 2D план (structured geometry негизинде)

Бул модулда ЖОК (атайылап, so деп СРС 39/41-бөлүмдөрдө эскертилгендей,
жасалма функционалдык кошпош үчүн):
  - 2D/3D drag-drop редактор
  - AI-жардамчы менен геометрияны өзгөртүү
  - PDF документация генерациясы
  - admin panel, версия контролу
Булар — Phase 2/3, өзүнчө талкууланат.
"""

import re
from flask import Blueprint, request, jsonify

from database import get_connection, row_to_dict

architect_bp = Blueprint("architect", __name__, url_prefix="/api/architect")

# СРС 7-бөлүмдөгү категориялардын бир бөлүгү — MVP үчүн эң көп колдонуларлары
STYLE_KEYWORDS = {
    "минималист": "Минималистичный", "минимализм": "Минималистичный",
    "классик": "Классический", "неоклассик": "Неоклассический",
    "скандинав": "Скандинавский", "лофт": "Лофт", "хай-тек": "Хай-тек",
    "хайтек": "Хай-тек", "модерн": "Модерн", "рустикальн": "Рустикальный",
    "рустик": "Рустикальный", "шале": "Шале", "прованс": "Прованс",
    "японск": "Японский стиль", "восточн": "Восточный стиль",
}
FEATURE_KEYWORDS = {
    "гараж": "garage", "террас": "terrace", "балкон": "balcony",
    "бассейн": "pool", "подвал": "basement", "цоколь": "basement",
}


def parse_query(q: str) -> dict:
    """
    Эркин текст издөөнү (мис. 'рустикальный двухэтажный дом с гаражом')
    структураланган фильтрлерге айландырат. Бул so аталган "жеңил-салмактуу"
    key-word талдоо — чыныгы NLP/семантика эмес, бирок иштейт жана ак калп
    эмес (fake emес).
    """
    q_lower = q.lower()
    parsed = {"style": None, "floors": None, "features": [], "free_text": q}

    for kw, style in STYLE_KEYWORDS.items():
        if kw in q_lower:
            parsed["style"] = style
            break

    floor_match = re.search(r"(\d+)\s*[- ]?этаж", q_lower)
    if floor_match:
        parsed["floors"] = int(floor_match.group(1))
    elif "одноэтаж" in q_lower or "одно-этаж" in q_lower:
        parsed["floors"] = 1
    elif "двухэтаж" in q_lower or "двух-этаж" in q_lower:
        parsed["floors"] = 2
    elif "трёхэтаж" in q_lower or "трехэтаж" in q_lower:
        parsed["floors"] = 3

    for kw, feature in FEATURE_KEYWORDS.items():
        if kw in q_lower:
            parsed["features"].append(feature)

    return parsed


@architect_bp.route("/projects", methods=["GET"])
def list_projects():
    """
    Query params:
      q          — эркин текст издөө (semantic-lite)
      style      — так стиль боюнча фильтр
      floors     — так кабат саны
      garage / terrace / balcony / pool — "true"/"false"
      page, page_size — pagination (СРС 36-бөлүм: lazy load / pagination)
    """
    q = request.args.get("q", "").strip()
    style_filter = request.args.get("style", "").strip()
    floors_filter = request.args.get("floors", "").strip()
    page = max(1, int(request.args.get("page", 1) or 1))
    page_size = min(50, max(1, int(request.args.get("page_size", 12) or 12)))

    conditions = ["status = 'active'"]
    params = []

    parsed = parse_query(q) if q else None
    parsed_found_something = bool(parsed and (parsed["style"] or parsed["floors"] or parsed["features"]))

    if q and not parsed_found_something:
        # Эч кандай белгилүү стиль/кабат/өзгөчөлүк табылбаса, жөнөкөй текст издөөгө кайтабыз
        conditions.append("(title LIKE ? OR description LIKE ? OR tags LIKE ? OR style LIKE ?)")
        like = f"%{q}%"
        params += [like, like, like, like]

    effective_style = style_filter or (parsed["style"] if parsed else None)
    if effective_style:
        conditions.append("style = ?")
        params.append(effective_style)

    effective_floors = floors_filter or (parsed["floors"] if parsed else None)
    if effective_floors:
        conditions.append("floors = ?")
        params.append(int(effective_floors))

    feature_list = list(parsed["features"]) if parsed else []
    for feature in ("garage", "terrace", "balcony", "pool"):
        val = request.args.get(feature)
        if val is not None:
            if val.lower() == "true":
                feature_list.append(feature)
            conditions.append(f"{feature} = ?")
            params.append(1 if val.lower() == "true" else 0)
    for feature in feature_list:
        if f"{feature} = ?" not in " ".join(conditions):
            conditions.append(f"{feature} = 1")

    where_clause = " AND ".join(conditions)

    conn = get_connection()
    total = conn.execute(f"SELECT COUNT(*) FROM projects WHERE {where_clause}", params).fetchone()[0]
    offset = (page - 1) * page_size
    rows = conn.execute(
        f"SELECT id, title, description, project_type, style, floors, area, rooms, "
        f"bedrooms, bathrooms, windows, doors, garage, terrace, balcony, pool, "
        f"basement, roof_type, shape, tags FROM projects WHERE {where_clause} "
        f"ORDER BY id LIMIT ? OFFSET ?",
        params + [page_size, offset],
    ).fetchall()
    conn.close()

    return jsonify({
        "ok": True,
        "data": {
            "projects": [row_to_dict(r) for r in rows],
            "total": total,
            "page": page,
            "page_size": page_size,
            "parsed_query": parsed,
        },
    })


@architect_bp.route("/projects/<int:project_id>", methods=["GET"])
def get_project(project_id):
    conn = get_connection()
    row = conn.execute("SELECT * FROM projects WHERE id = ?", (project_id,)).fetchone()
    conn.close()
    if row is None:
        return jsonify({"ok": False, "error": "not_found"}), 404
    return jsonify({"ok": True, "data": row_to_dict(row)})


@architect_bp.route("/styles", methods=["GET"])
def list_styles():
    """Фильтр UI үчүн: базада чын-чынына колдонулуп жаткан стилдердин тизмеси."""
    conn = get_connection()
    rows = conn.execute(
        "SELECT DISTINCT style, COUNT(*) as cnt FROM projects "
        "WHERE status = 'active' AND style != '' GROUP BY style ORDER BY style"
    ).fetchall()
    conn.close()
    return jsonify({"ok": True, "data": [{"style": r["style"], "count": r["cnt"]} for r in rows]})
