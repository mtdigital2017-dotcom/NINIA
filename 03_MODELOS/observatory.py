
from collections import Counter

import config

from knowledge_base import KnowledgeBase


class Observatory:

    def __init__(self):

        self.base = KnowledgeBase(
            config.KNOWLEDGE_BASE
        )

        self.docs = self.base.cargar()

    def resumen(self):

        print("="*70)
        print("OBSERVATORIO NINIA")
        print("="*70)

        print("Documentos:", len(self.docs))

        riesgos = Counter()
        organizaciones = Counter()
        tecnologias = Counter()
        ods = Counter()

        for doc in self.docs:

            for r in doc.get("riesgos", []):
                riesgos[r] += 1

            for o in doc.get("organizaciones", []):
                organizaciones[o] += 1

            for t in doc.get("tecnologias", []):
                tecnologias[t] += 1

            for x in doc.get("ods", []):
                ods[x] += 1

        print("\nTOP RIESGOS")
        print("-"*40)
        for x in riesgos.most_common(10):
            print(x)

        print("\nTOP ORGANIZACIONES")
        print("-"*40)
        for x in organizaciones.most_common(10):
            print(x)

        print("\nTOP TECNOLOGÍAS")
        print("-"*40)
        for x in tecnologias.most_common(10):
            print(x)

        print("\nTOP ODS")
        print("-"*40)
        for x in ods.most_common(10):
            print(x)

