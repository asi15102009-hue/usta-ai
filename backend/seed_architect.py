"""
seed_architect.py — Архитектор каталогун мисал долбоорлор менен толтурат.

Бул MVP үчүн 14 мисал долбоор (1000 эмес) — СРС документинин өзүндө
эскертилгендей ("Маалыматтарды frontend'ге миңдеген сүрөт катары катуу
коддоп салба"), маалыматтар database'де сакталат, frontend аларды API
аркылуу алат.

Бир нече долбоордо (project_type='editable') чыныгы structured geometry
бар — алар үчүн 2D план көрсөтүлөт. Калгандары 'reference' — азырынча
метадата гана, план жок (СРС 39-бөлүм: "сүрөт ≠ редакцияланчу долбоор").

Кайра иштетсе да коопсуз: адегенде эски мисал маалыматтарды тазалайт,
андан кийин кайра толтурат (колдонуучунун өз кол менен кошкон
долбоорлоруна тийбейт — алар башка seed_tag менен белгиленген эмес,
бул скрипт "уста-ай-seed" деген tag'ы бар жазууларды гана өчүрөт/түзөт).
"""

import json
from database import get_connection, init_db

SEED_TAG = "уста-ай-seed"


def geometry_simple_rect_house(rooms):
    """rooms: [(name, x, y, w, h), ...] — метрде. Бир кабат үчүн жөнөкөй геометрия."""
    return json.dumps({
        "floors": [{
            "level": 1,
            "rooms": [
                {"name": n, "x": x, "y": y, "w": w, "h": h}
                for (n, x, y, w, h) in rooms
            ],
        }]
    }, ensure_ascii=False)


PROJECTS = [
    dict(title="Rustic House 184", description="Эки кабаттуу рустикалдык үй, гараж жана террасасы менен.",
         project_type="editable", style="Рустикальный", floors=2, area=184, rooms=6, bedrooms=4,
         bathrooms=2, windows=18, doors=10, garage=1, terrace=1, balcony=1, pool=0, basement=0,
         roof_type="Двухскатная", shape="Прямоугольный", tags=f"рустикальный,гараж,терраса,{SEED_TAG}",
         source_name="УСТА AI (мисал)", source_url="", license="Internal sample",
         geometry=geometry_simple_rect_house([
             ("Гостиная", 0, 0, 6, 5), ("Кухня", 6, 0, 4, 5),
             ("Спальня 1", 0, 5, 5, 4), ("Спальня 2", 5, 5, 5, 4),
         ])),
    dict(title="Modern Cube 220", description="Заманбап минималисттик стилдеги квадрат формадагы үй.",
         project_type="editable", style="Минималистичный", floors=2, area=220, rooms=7, bedrooms=4,
         bathrooms=3, windows=22, doors=12, garage=1, terrace=0, balcony=1, pool=1, basement=0,
         roof_type="Плоская", shape="Квадратный", tags=f"минималистичный,бассейн,гараж,{SEED_TAG}",
         source_name="УСТА AI (мисал)", source_url="", license="Internal sample",
         geometry=geometry_simple_rect_house([
             ("Гостиная", 0, 0, 7, 6), ("Кухня", 7, 0, 5, 6),
             ("Кабинет", 0, 6, 4, 4), ("Спальня", 4, 6, 8, 4),
         ])),
    dict(title="Scandi Light 145", description="Скандинавиялык стилдеги жарык, ачык план.",
         project_type="editable", style="Скандинавский", floors=1, area=145, rooms=5, bedrooms=3,
         bathrooms=1, windows=14, doors=7, garage=0, terrace=1, balcony=0, pool=0, basement=0,
         roof_type="Двухскатная", shape="Прямоугольный", tags=f"скандинавский,терраса,одноэтажный,{SEED_TAG}",
         source_name="УСТА AI (мисал)", source_url="", license="Internal sample",
         geometry=geometry_simple_rect_house([
             ("Гостиная", 0, 0, 6, 5), ("Спальня 1", 6, 0, 4, 5),
             ("Кухня", 0, 5, 5, 3), ("Спальня 2", 5, 5, 5, 3),
         ])),
    dict(title="Chalet Mountain 260", description="Тоо шале стилиндеги, чоң мансардасы бар үй.",
         project_type="reference", style="Шале", floors=2, area=260, rooms=8, bedrooms=5,
         bathrooms=3, windows=20, doors=14, garage=1, terrace=1, balcony=1, pool=0, basement=1,
         roof_type="Мансардная", shape="Прямоугольный", tags=f"шале,мансарда,подвал,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Loft Urban 198", description="Лофт стилиндеги, ачык мейкиндик менен.",
         project_type="reference", style="Лофт", floors=1, area=198, rooms=4, bedrooms=2,
         bathrooms=2, windows=16, doors=6, garage=0, terrace=0, balcony=0, pool=0, basement=0,
         roof_type="Плоская", shape="Прямоугольный", tags=f"лофт,одноэтажный,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Hi-Tech Villa 310", description="Хай-тек стилиндеги, бассейни бар люкс вилла.",
         project_type="reference", style="Хай-тек", floors=2, area=310, rooms=9, bedrooms=5,
         bathrooms=4, windows=28, doors=16, garage=1, terrace=1, balcony=1, pool=1, basement=1,
         roof_type="Плоская", shape="Асимметричный", tags=f"хай-тек,бассейн,гараж,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Classic Manor 275", description="Классикалык стилдеги, колонналуу фасад.",
         project_type="reference", style="Классический", floors=2, area=275, rooms=8, bedrooms=5,
         bathrooms=3, windows=24, doors=14, garage=1, terrace=1, balcony=1, pool=0, basement=1,
         roof_type="Четырёхскатная", shape="Прямоугольный", tags=f"классический,гараж,терраса,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Provence Cottage 160", description="Прованс стилиндеги жайлуу коттедж.",
         project_type="editable", style="Прованс", floors=1, area=160, rooms=5, bedrooms=3,
         bathrooms=2, windows=15, doors=8, garage=0, terrace=1, balcony=0, pool=0, basement=0,
         roof_type="Двухскатная", shape="L-образный", tags=f"прованс,терраса,одноэтажный,{SEED_TAG}",
         source_name="УСТА AI (мисал)", source_url="", license="Internal sample",
         geometry=geometry_simple_rect_house([
             ("Гостиная", 0, 0, 5, 5), ("Кухня", 5, 0, 4, 5),
             ("Спальня", 0, 5, 4, 4), ("Ванная", 4, 5, 2, 2),
         ])),
    dict(title="Japanese Zen 175", description="Жапон стилиндеги, минималдуу форма.",
         project_type="reference", style="Японский стиль", floors=1, area=175, rooms=5, bedrooms=3,
         bathrooms=2, windows=16, doors=9, garage=0, terrace=1, balcony=0, pool=0, basement=0,
         roof_type="Односкатная", shape="Прямоугольный", tags=f"японский стиль,терраса,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Neoclassic Estate 340", description="Неоклассикалык стилдеги эстейт, чоң аймак менен.",
         project_type="reference", style="Неоклассический", floors=3, area=340, rooms=10, bedrooms=6,
         bathrooms=4, windows=32, doors=18, garage=1, terrace=1, balcony=1, pool=1, basement=1,
         roof_type="Четырёхскатная", shape="Прямоугольный", tags=f"неоклассический,трёхэтажный,бассейн,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="American Family 230", description="Америкалык стилдеги үй-бүлөлүк үй.",
         project_type="reference", style="Американский стиль", floors=2, area=230, rooms=7, bedrooms=4,
         bathrooms=3, windows=20, doors=12, garage=1, terrace=1, balcony=1, pool=0, basement=0,
         roof_type="Двухскатная", shape="Прямоугольный", tags=f"американский стиль,гараж,терраса,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Baroque Palace 420", description="Барокко стилиндеги люкс резиденция.",
         project_type="reference", style="Барокко", floors=3, area=420, rooms=12, bedrooms=7,
         bathrooms=5, windows=40, doors=22, garage=1, terrace=1, balcony=1, pool=1, basement=1,
         roof_type="Четырёхскатная", shape="Асимметричный", tags=f"барокко,бассейн,трёхэтажный,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
    dict(title="Compact Studio 68", description="Кичине, бир бөлмөлүү компакт үй.",
         project_type="editable", style="Минималистичный", floors=1, area=68, rooms=3, bedrooms=1,
         bathrooms=1, windows=6, doors=3, garage=0, terrace=0, balcony=0, pool=0, basement=0,
         roof_type="Плоская", shape="Квадратный", tags=f"минималистичный,одноэтажный,компакт,{SEED_TAG}",
         source_name="УСТА AI (мисал)", source_url="", license="Internal sample",
         geometry=geometry_simple_rect_house([
             ("Гостиная+Кухня", 0, 0, 6, 5), ("Спальня", 0, 5, 4, 3), ("Ванная", 4, 5, 2, 3),
         ])),
    dict(title="Eastern Courtyard 290", description="Чыгыш стилиндеги, ички короосу бар үй.",
         project_type="reference", style="Восточный стиль", floors=1, area=290, rooms=8, bedrooms=4,
         bathrooms=3, windows=18, doors=14, garage=0, terrace=1, balcony=0, pool=1, basement=0,
         roof_type="Плоская", shape="П-образный", tags=f"восточный стиль,бассейн,{SEED_TAG}",
         source_name="Reference collection", source_url="", license="Reference only — not for editing",
         geometry=None),
]


def seed():
    init_db()
    conn = get_connection()
    conn.execute("DELETE FROM projects WHERE tags LIKE ?", (f"%{SEED_TAG}%",))
    for p in PROJECTS:
        conn.execute(
            """INSERT INTO projects
            (title, description, project_type, style, floors, area, rooms, bedrooms,
             bathrooms, windows, doors, garage, terrace, balcony, pool, basement,
             roof_type, shape, tags, source_name, source_url, license, geometry, status)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (
                p["title"], p["description"], p["project_type"], p["style"], p["floors"],
                p["area"], p["rooms"], p["bedrooms"], p["bathrooms"], p["windows"], p["doors"],
                p["garage"], p["terrace"], p["balcony"], p["pool"], p["basement"],
                p["roof_type"], p["shape"], p["tags"], p["source_name"], p["source_url"],
                p["license"], p["geometry"], "active",
            ),
        )
    conn.commit()
    count = conn.execute("SELECT COUNT(*) FROM projects").fetchone()[0]
    conn.close()
    print(f"Даяр: {len(PROJECTS)} мисал долбоор кошулду. Base'де жалпы: {count} долбоор.")


if __name__ == "__main__":
    seed()
