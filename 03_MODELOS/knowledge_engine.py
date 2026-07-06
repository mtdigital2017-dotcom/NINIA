
"""
NINIA
Knowledge Engine
Versión 0.1
"""

import re
from collections import Counter

class KnowledgeEngine:

    def analizar(self, texto):

        palabras = re.findall(r"\w+", texto.lower())

        total = len(palabras)

        frecuentes = Counter(palabras).most_common(20)

        return {
            "total_palabras": total,
            "top20": frecuentes
        }

