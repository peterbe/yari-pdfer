import io
from pathlib import Path

from flask import Flask, send_file

from pdfer.app import json_to_html, html_to_pdf

app = Flask(__name__)


@app.route("/")
def preview_html():
    data = Path("../data")
    assert data.exists(), str(data)
    files = data.glob("*index.json")
    return json_to_html(files)


@app.route("/pdf")
def pdf():
    data = Path("../data")
    assert data.exists(), str(data)
    files = data.glob("*index.json")
    html_string = json_to_html(files)
    buffer = io.BytesIO()
    html_to_pdf(html_string, buffer)
    buffer.seek(0)
    return send_file(
        buffer, attachment_filename="documents.pdf", mimetype="application/pdf"
    )
