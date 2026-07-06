
"""
=========================================
NINIA PIPELINE v2.1
=========================================
"""

import glob

from document_loader import DocumentLoader
from knowledge_engine import KnowledgeEngine
from semantic_engine import SemanticEngine
from knowledge_builder import KnowledgeBuilder
from nlp_engine import NLPEngine


class Pipeline:

    def __init__(self):

        self.loader = DocumentLoader()

        self.nlp = NLPEngine()

        self.semantic = SemanticEngine()

        self.knowledge = KnowledgeEngine()

        self.builder = KnowledgeBuilder()


    def procesar_pdf(self, ruta_pdf):

        texto = self.loader.leer(ruta_pdf)

        entidades = self.nlp.analizar(texto)

        categorias = self.semantic.clasificar(texto)

        kb = self.builder.construir(

            archivo=ruta_pdf.split("/")[-1],

            texto=texto,

            entidades_nlp=entidades,

            categorias=categorias

        )

        return kb


    def ejecutar(self, carpeta):

        pdfs = glob.glob(

            carpeta + "/**/*.pdf",

            recursive=True

        )

        resultados=[]

        for pdf in pdfs:

            resultados.append(

                self.procesar_pdf(pdf)

            )

        return resultados