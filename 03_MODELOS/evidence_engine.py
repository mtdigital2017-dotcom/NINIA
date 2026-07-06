
class EvidenceEngine:

    def __init__(self):

        self.pesos = {

            "metaanálisis":100,
            "revision sistematica":95,
            "guía":90,
            "guia":90,
            "norma":90,
            "resolución":88,
            "resolucion":88,
            "ley":85,
            "decreto":82,
            "artículo científico":80,
            "articulo cientifico":80,
            "paper":80,
            "informe":70,
            "reporte":70,
            "manual":65,
            "blog":20

        }

    def calcular(self, obj):

        tipo = (
            obj.tipo_documento
            or ""
        ).lower()

        for clave, peso in self.pesos.items():

            if clave in tipo:

                return peso

        return 50

