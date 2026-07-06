
"""
=========================================
NINIA PROCESSING ENGINE
Versión 4.0
=========================================
"""

from document_loader import DocumentLoader
from chunk_engine import ChunkEngine
from knowledge_object import KnowledgeObject
from semantic_engine import SemanticEngine
from entity_extractor import EntityExtractor
from knowledge_base import KnowledgeBase
import config


class ProcessingEngine:

    def __init__(self):

        self.loader = DocumentLoader()
        self.chunker = ChunkEngine()
        self.semantic = SemanticEngine()
        self.entities = EntityExtractor()

        self.kb = KnowledgeBase(
            config.KNOWLEDGE_BASE
        )

    def procesar(self, ruta_pdf):

        texto = self.loader.leer(ruta_pdf)

        clasificacion = self.semantic.clasificar(texto)

        chunks = self.chunker.dividir(texto)

        objetos = []

        for i, chunk in enumerate(chunks):

            entidades = self.entities.extraer(chunk)

            obj = KnowledgeObject(

                archivo=ruta_pdf.split("/")[-1],

                chunk=i+1,

                resumen=chunk[:500],

                organizaciones=entidades.get("organizaciones",[]),

                riesgos=entidades.get("riesgos",[]),

                plataformas=entidades.get("plataformas",[]),

                tecnologias=entidades.get("tecnologias",[]),

                palabras_clave=sorted(list(set(

                    entidades.get("organizaciones",[]) +

                    entidades.get("riesgos",[]) +

                    entidades.get("plataformas",[]) +

                    entidades.get("tecnologias",[])

                ))),

                clasificacion=clasificacion,

                confianza=0.50

            )

            self.kb.agregar(
                obj.to_dict()
            )

            objetos.append(obj)

        return objetos
