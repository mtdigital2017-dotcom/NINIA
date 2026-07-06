
"""
=========================================
NINIA GEMINI ADAPTER
Versión 1.0
=========================================
"""

import json
from google import genai


class GeminiAdapter:

    def __init__(self, api_key):

        self.client = genai.Client(api_key=api_key)

    def analizar(self, prompt):

        respuesta = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return respuesta.text
