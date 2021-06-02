import json


from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

from jinja2 import Environment, PackageLoader, select_autoescape


def html_to_pdf(html_string, destination="/tmp/example.pdf"):
    font_config = FontConfiguration()
    html = HTML(string=html_string)
    css = CSS(
        string="""
        /*@font-face {
            font-family: Gentium;
            src: url(/typography/Gentium.otf);
        }*/
        @font-face {
            font-display: swap;
            font-family: zillaslab;
            font-style: normal;
            font-weight: bold;
            src: url("./typography/ZillaSlab-Bold.subset.woff2") format("woff2"),
                url("./typography/ZillaSlab-Bold.subset.woff") format("woff");
            }

            @font-face {
            font-display: swap;
            font-family: zillaslab;
            font-style: normal;
            font-weight: normal;
            src: url("./typography/ZillaSlab-Regular.subset.woff2") format("woff2"),
                url("./typography/ZillaSlab-Regular.subset.woff") format("woff");
            }

        @page { size: Letter; margin: 1cm }
        /*h1 { font-family: Gentium }*/
        h1, h2, h3, h4, h5 {
            font-family: zillaslab, palatino, "Palatino Linotype", serif;
        }
        """,
        font_config=font_config,
    )
    html.write_pdf(destination, stylesheets=[css], font_config=font_config)


def json_to_html(json_files):
    documents = []

    for file in json_files:
        with open(file) as f:
            document = json.load(f)["doc"]
            documents.append(document)
        # from pprint import pprint

        # pprint(document["body"])
    env = Environment(loader=PackageLoader("pdfer"), autoescape=select_autoescape())

    template = env.get_template("docs.html")

    html_string = template.render(documents=documents)
    return html_string
