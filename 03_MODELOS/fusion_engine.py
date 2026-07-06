
"""
=========================================
NINIA FUSION ENGINE
Versión 1.0
=========================================
"""

from knowledge_object import KnowledgeObject


class FusionEngine:

    def fusionar(self, objetos):

        if len(objetos) == 1:
            return objetos[0]

        final = KnowledgeObject()

        final.archivo = objetos[0].archivo
        final.titulo = objetos[0].titulo
        final.tema_principal = objetos[0].tema_principal
        final.organizacion = objetos[0].organizacion
        final.tipo_documento = objetos[0].tipo_documento

        listas = [
            "organizaciones",
            "personas",
            "lugares",
            "riesgos",
            "plataformas",
            "tecnologias",
            "estrategias",
            "recomendaciones",
            "ods",
            "palabras_clave"
        ]

        for atributo in listas:

            valores = []

            for obj in objetos:

                valores.extend(
                    getattr(obj, atributo, [])
                )

            setattr(
                final,
                atributo,
                sorted(list(set(valores)))
            )

        final.clasificacion = objetos[0].clasificacion

        final.confianza = sum(
            obj.confianza
            for obj in objetos
        ) / len(objetos)

        return final
