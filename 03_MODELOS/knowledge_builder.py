
"""
=========================================
NINIA KNOWLEDGE BUILDER v2.0
=========================================
"""

class KnowledgeBuilder:

    def construir(self,
                  archivo,
                  texto,
                  entidades_nlp,
                  categorias):

        conocimiento = {}

        conocimiento["archivo"] = archivo

        conocimiento["palabras"] = len(texto.split())

        conocimiento["organizaciones"] = []
        conocimiento["personas"] = []
        conocimiento["lugares"] = []
        conocimiento["fechas"] = []

        conocimiento["clasificacion"] = categorias

        conocimiento["resumen"] = texto[:1200]

        for entidad in entidades_nlp:

            tipo = entidad["tipo"]

            if tipo == "ORG":
                conocimiento["organizaciones"].append(entidad["texto"])

            elif tipo == "PER":
                conocimiento["personas"].append(entidad["texto"])

            elif tipo in ["LOC", "GPE"]:
                conocimiento["lugares"].append(entidad["texto"])

            elif tipo == "DATE":
                conocimiento["fechas"].append(entidad["texto"])

        conocimiento["organizaciones"] = sorted(set(conocimiento["organizaciones"]))
        conocimiento["personas"] = sorted(set(conocimiento["personas"]))
        conocimiento["lugares"] = sorted(set(conocimiento["lugares"]))
        conocimiento["fechas"] = sorted(set(conocimiento["fechas"]))

        return conocimiento