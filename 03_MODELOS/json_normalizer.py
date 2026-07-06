
"""
=========================================
NINIA JSON NORMALIZER
=========================================
"""

class JSONNormalizer:

    MAPEO = {

        "ODS":"ods",

        "AÑO":"anio",
        "Año":"anio",
        "año":"anio",

        "Organización":"organizacion",
        "organización":"organizacion",

        "Competencias_AMI":"competencias_AMI",

        "Nivel_Evidencia":"nivel_evidencia"
    }

    def normalizar(self, datos):

        resultado = {}

        for clave, valor in datos.items():

            nueva = self.MAPEO.get(
                clave,
                clave
            )

            resultado[nueva] = valor

        return resultado
