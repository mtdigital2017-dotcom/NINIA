
from evidence_engine import EvidenceEngine


class RankingEngine:

    def __init__(self):

        self.evidence = EvidenceEngine()

    def score(self, obj):

        evidencia = self.evidence.calcular(obj)

        confianza = obj.confianza * 100

        completitud = 0

        campos = [

            obj.titulo,
            obj.tema_principal,
            obj.organizacion,
            obj.riesgos,
            obj.recomendaciones,
            obj.estrategias,
            obj.palabras_clave

        ]

        for campo in campos:

            if campo:

                completitud += 1

        completitud = completitud / len(campos) * 100

        score = (

            evidencia * 0.50 +

            confianza * 0.30 +

            completitud * 0.20

        )

        return round(score,2)

