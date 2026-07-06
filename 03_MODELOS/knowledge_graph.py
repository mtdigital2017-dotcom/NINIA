
from collections import defaultdict

import config

from knowledge_base import KnowledgeBase


class KnowledgeGraph:

    def __init__(self):

        self.base = KnowledgeBase(
            config.KNOWLEDGE_BASE
        )

        self.docs = self.base.cargar()

        self.grafo = defaultdict(set)

    def construir(self):

        for doc in self.docs:

            org = doc.get("organizacion","")

            if not org:
                continue

            for riesgo in doc.get("riesgos",[]):
                self.grafo[org].add(("RIESGO",riesgo))

            for tec in doc.get("tecnologias",[]):
                self.grafo[org].add(("TECNOLOGIA",tec))

            for ods in doc.get("ods",[]):
                self.grafo[org].add(("ODS",ods))

            for estrategia in doc.get("estrategias",[]):
                self.grafo[org].add(("ESTRATEGIA",estrategia))

        return self.grafo

    def mostrar(self, nodo):

        nodo = nodo.strip()

        if nodo not in self.grafo:

            print("Nodo no encontrado")

            return

        print("="*60)
        print(nodo)
        print("="*60)

        for tipo, valor in sorted(self.grafo[nodo]):
            print(f"[{tipo}] {valor}")

