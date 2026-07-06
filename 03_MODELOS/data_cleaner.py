
import config

from knowledge_base import KnowledgeBase
from knowledge_object import KnowledgeObject
from ranking_engine import RankingEngine


class DataCleaner:

    def __init__(self):

        self.base = KnowledgeBase(
            config.KNOWLEDGE_BASE
        )

        self.rank = RankingEngine()

    def limpiar(self):

        docs = self.base.cargar()

        mejores = {}

        for doc in docs:

            obj = KnowledgeObject(**doc)

            archivo = obj.archivo

            score = self.rank.score(obj)

            if archivo not in mejores:

                mejores[archivo] = (
                    score,
                    doc
                )

            else:

                if score > mejores[archivo][0]:

                    mejores[archivo] = (
                        score,
                        doc
                    )

        salida = [

            x[1]

            for x in mejores.values()

        ]

        self.base.guardar(
            salida
        )

        print()

        print("Documentos originales:", len(docs))

        print("Documentos finales:", len(salida))

