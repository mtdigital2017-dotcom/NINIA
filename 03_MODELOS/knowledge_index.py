
"""
=========================================
KNOWLEDGE INDEX
Versión 1.0
=========================================
"""

import json
import os


class KnowledgeIndex:

    def __init__(self):

        self.archivo="/content/drive/MyDrive/NINIA/data/index.json"

        if not os.path.exists(self.archivo):

            with open(self.archivo,"w",encoding="utf-8") as f:

                json.dump({},f,indent=4,ensure_ascii=False)


    def actualizar(self, conocimiento):

        with open(self.archivo,"r",encoding="utf-8") as f:

            indice=json.load(f)

        archivo=conocimiento["archivo"]

        indice[archivo]={

            "palabras":conocimiento["palabras"],

            "organizaciones":conocimiento["organizaciones"],

            "clasificacion":conocimiento["clasificacion"]

        }

        with open(self.archivo,"w",encoding="utf-8") as f:

            json.dump(
                indice,
                f,
                indent=4,
                ensure_ascii=False
            )


    def cargar(self):

        with open(self.archivo,"r",encoding="utf-8") as f:

            return json.load(f)
