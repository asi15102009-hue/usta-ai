"""
database.py — Архитектор модулу үчүн SQLite database.

Бул файл УСТА AI'дын калган бөлүгүнө (foundation/wall/roof) такыр тийбейт —
өзүнчө, өз алдынча модуль. SQLite тандалды, себеби ал Python'до курулмасынан эле
бар (кошумча орнотуу талап кылбайт) жана MVP үчүн жетиштүү.

Долбоордун geometry'сы (бөлмөлөр, дубалдар) JSON түрүндө сакталат — бул сүрөт
эмес, кайра иштетүүгө боло турган структураланган маалымат (SRS 38-бөлүм талабы).
"""

import os
import sqlite3
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "architect.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT DEFAULT '',
    project_type TEXT NOT NULL DEFAULT 'reference',  -- 'editable' | 'reference'
    style TEXT DEFAULT '',
    floors INTEGER DEFAULT 1,
    area REAL DEFAULT 0,
    rooms INTEGER DEFAULT 0,
    bedrooms INTEGER DEFAULT 0,
    bathrooms INTEGER DEFAULT 0,
    windows INTEGER DEFAULT 0,
    doors INTEGER DEFAULT 0,
    garage INTEGER DEFAULT 0,
    terrace INTEGER DEFAULT 0,
    balcony INTEGER DEFAULT 0,
    pool INTEGER DEFAULT 0,
    basement INTEGER DEFAULT 0,
    roof_type TEXT DEFAULT '',
    shape TEXT DEFAULT '',
    tags TEXT DEFAULT '',
    source_name TEXT DEFAULT '',
    source_url TEXT DEFAULT '',
    license TEXT DEFAULT '',
    geometry TEXT DEFAULT NULL,
    status TEXT DEFAULT 'active',
    created_at TEXT DEFAULT (datetime('now'))
);
"""


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Схема жок болсо түзөт. Колдонуучунун маалыматтарын жоготпойт
    (CREATE TABLE IF NOT EXISTS) — app.py ар жолу иштегенде коопсуз чакырылат."""
    conn = get_connection()
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()


def row_to_dict(row: sqlite3.Row) -> dict:
    d = dict(row)
    for bool_field in ("garage", "terrace", "balcony", "pool", "basement"):
        d[bool_field] = bool(d.get(bool_field))
    if d.get("tags"):
        d["tags"] = [t.strip() for t in d["tags"].split(",") if t.strip()]
    else:
        d["tags"] = []
    if d.get("geometry"):
        try:
            d["geometry"] = json.loads(d["geometry"])
        except (json.JSONDecodeError, TypeError):
            d["geometry"] = None
    return d
