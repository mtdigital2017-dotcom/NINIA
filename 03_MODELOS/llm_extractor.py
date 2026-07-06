
"""
=========================================
NINIA LLM EXTRACTOR
Versión 3.0
=========================================
"""

import json
from dataclasses import fields

from google import genai

from knowledge_object import KnowledgeObject
from json_normalizer import JSONNormalizer


class LLMExtractor:

    def __init__(self, api_key):

        self.client = genai.Client(
            api_key=api_key
        )

    def extraer(self, prompt):

        respuesta = self.client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        texto = respuesta.text.strip()

        if texto.startswith("```json"):
            texto = texto.replace("```json","",1)

        if texto.startswith("```"):
            texto = texto.replace("```","",1)

        if texto.endswith("```"):
            texto = texto[:-3]

        texto = texto.strip()

        datos = json.loads(texto)

        datos = JSONNormalizer().normalizar(datos)

        campos_validos = {
            f.name
            for f in fields(KnowledgeObject)
        }

        datos = {
            k:v
            for k,v in datos.items()
            if k in campos_validos
        }

        return KnowledgeObject(**datos)
