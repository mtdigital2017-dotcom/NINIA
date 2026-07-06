
"""
=========================================
NINIA LLM INTERFACE
Versión 1.0
=========================================
"""

class LLMInterface:

    def __init__(self):

        print("=========================================")
        print(" NINIA LLM INTERFACE")
        print("=========================================")


    def extraer_conocimiento(self, texto):

        raise NotImplementedError(
            "Debe implementarse en Gemini, OpenAI o Claude."
        )
