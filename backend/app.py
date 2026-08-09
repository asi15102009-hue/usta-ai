"""
app.py — УСТА АИ (Project Atlas) backend
"""

import os

from flask import Flask, request, jsonify, send_from_directory, Response
from flask_cors import CORS

import foundation
import wall
import roof
from utils import ValidationError
from pdf import generate_pdf
from architect import architect_bp
from database import init_db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(os.path.dirname(BASE_DIR), "frontend")

app = Flask(__name__, static_folder=None)
CORS(app)

init_db()
app.register_blueprint(architect_bp)

CALCULATORS = {
    "foundation": foundation.calculate,
    "wall": wall.calculate,
    "roof": roof.calculate,
}


@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(FRONTEND_DIR, path)


@app.route("/api/<module>", methods=["POST"])
def calculate(module):
    if module not in CALCULATORS:
        return jsonify({"ok": False, "error": "unknown_module"}), 404

    data = request.get_json(silent=True) or {}
    try:
        result = CALCULATORS[module](data)
    except ValidationError as e:
        return jsonify({"ok": False, "errors": e.errors}), 422

    return jsonify({"ok": True, "data": result})


@app.route("/api/pdf/<module>", methods=["POST"])
def pdf_report(module):
    if module not in CALCULATORS:
        return jsonify({"ok": False, "error": "unknown_module"}), 404

    body = request.get_json(silent=True) or {}
    lang = body.get("lang", "kg")
    project_name = body.get("project_name", "")
    project_date = body.get("project_date", "")
    inputs = body.get("inputs", {})

    try:
        result = CALCULATORS[module](inputs)
    except ValidationError as e:
        return jsonify({"ok": False, "errors": e.errors}), 422

    pdf_bytes = generate_pdf(module, lang, project_name, project_date, result, inputs)
    filename = f"usta_{module}_{project_date or 'report'}.pdf"
    return Response(
        pdf_bytes,
        mimetype="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)