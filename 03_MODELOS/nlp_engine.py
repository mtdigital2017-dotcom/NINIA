
"""
NINIA NLP ENGINE
Versión 1.0
"""

import spacy

class NLPEngine:

    def __init__(self):

        self.nlp = spacy.load("es_core_news_sm")

    def analizar(self, texto):

        doc = self.nlp(texto)

        entidades=[]

        for ent in doc.ents:

            entidades.append({
                "texto":ent.text,
                "tipo":ent.label_
            })

        return entidades
