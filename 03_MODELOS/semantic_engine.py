
"""
NINIA Semantic Engine
Versión 1.0
"""

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

class SemanticEngine:

    def __init__(self):

        self.modelo = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        self.categorias = {

            "PROTECCION_NNA":
            "Protección de niños niñas y adolescentes en entornos digitales",

            "SALUD_MENTAL":
            "Salud mental bienestar emocional depresión ansiedad suicidio",

            "VIOLENCIA_DIGITAL":
            "Ciberacoso grooming sextorsión violencia digital",

            "AMI":
            "Alfabetización mediática alfabetización informacional pensamiento crítico",

            "REGULACION":
            "Leyes regulación políticas públicas derechos digitales",

            "COOPERACION":
            "Cooperación internacional organismos multilaterales UNICEF UNESCO OCDE ONU",

            "IA":
            "Inteligencia artificial algoritmos sistemas inteligentes"
        }

        self.embeddings = {}

        for nombre, texto in self.categorias.items():

            self.embeddings[nombre] = self.modelo.encode(
                texto,
                convert_to_tensor=True
            )

    def clasificar(self, documento):

        emb_doc = self.modelo.encode(
            documento,
            convert_to_tensor=True
        )

        resultado = {}

        for categoria, emb in self.embeddings.items():

            score = float(cos_sim(emb_doc, emb))

            resultado[categoria] = round(score,3)

        return dict(
            sorted(
                resultado.items(),
                key=lambda x:x[1],
                reverse=True
            )
        )
