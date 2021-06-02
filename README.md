# Yari PDFer

Make PDFs of MDN Web Docs Yari documents.

## Development

Python >=3.8 and then `pip install -r requirements.txt` and
`pip install -r dev-requirements.txt`.

### CLI

It loads all the `*index.json` files in the `data/` directory (create if needed).

CLI:

```sh
python src/main.py
open /tmp/documents.pdf
```

### Server

It loads all the `*index.json` files in the `data/` directory (create if needed).

Start the with `./server`
and then you can go to <http://localhost:5000> to preview the HTML.
To go directly to the PDF, go to <http://localhost:5000/pdf>
