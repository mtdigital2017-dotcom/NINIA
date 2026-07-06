"""
NINIA
Módulo: Document Loader
Versión: 0.1
"""

import pdfplumber
from docx import Document
from pathlib import Path


class DocumentLoader:

    def __init__(self):
        print("✅ DocumentLoader iniciado")

    def leer(self, archivo):

        archivo = Path(archivo)

        if not archivo.exists():
            raise FileNotFoundError(f"No existe: {archivo}")

        extension = archivo.suffix.lower()

        if extension == ".pdf":
            return self._leer_pdf(archivo)

        if extension == ".docx":
            return self._leer_docx(archivo)

        raise Exception("Formato no soportado")


    def _leer_pdf(self, archivo):

        texto = ""

        with pdfplumber.open(archivo) as pdf:

            for pagina in pdf.pages:

                contenido = pagina.extract_text()

                if contenido:
                    texto += contenido + "\n"

        return texto


    def _leer_docx(self, archivo):

        doc = Document(archivo)

        texto = "\n".join([p.text for p in doc.paragraphs])

        return texto
