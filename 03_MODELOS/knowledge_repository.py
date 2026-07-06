
"""
=========================================
NINIA KNOWLEDGE REPOSITORY
Versión 1.0
=========================================
"""

import config

from knowledge_base import KnowledgeBase


class KnowledgeRepository:

    def __init__(self):

        self.base = KnowledgeBase(
            config.KNOWLEDGE_BASE
        )

        self.documentos = self.base.cargar()

    def total(self):

        return len(self.documentos)

    def buscar_por_tema(self, texto):

        texto = texto.lower()

        return [

            d for d in self.documentos

            if texto in d.get(
                "tema_principal",""
            ).lower()

        ]

    def buscar_por_organizacion(self, nombre):

        nombre = nombre.lower()

        return [

            d for d in self.documentos

            if nombre in d.get(
                "organizacion",""
            ).lower()

        ]

    def buscar_por_riesgo(self, riesgo):

        riesgo = riesgo.lower()

        resultado = []

        for d in self.documentos:

            riesgos = [

                r.lower()

                for r in d.get(
                    "riesgos",
                    []
                )

            ]

            if riesgo in riesgos:

                resultado.append(d)

        return resultado

