
"""
=========================================
NINIA JSON PARSER
=========================================
"""

import json


class JSONParser:

    def limpiar(self, texto):

        texto = texto.strip()

        if texto.startswith("```json"):
            texto = texto.replace("```json","",1)

        if texto.startswith("```"):
            texto = texto.replace("```","",1)

        if texto.endswith("```"):
            texto = texto[:-3]

        return texto.strip()


    def convertir(self,texto):

        texto = self.limpiar(texto)

        return json.loads(texto)
