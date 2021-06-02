from pathlib import Path

from pdfer.app import json_to_html, html_to_pdf

if __name__ == "__main__":
    files = Path("data").glob("*index.json")
    html_string = json_to_html(files)
    dest = "/tmp/documents.pdf"
    html_to_pdf(html_string, dest)
    print(f"Generated {dest}")
