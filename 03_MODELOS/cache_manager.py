
import json
from pathlib import Path

class CacheManager:

    def __init__(self, carpeta):

        self.carpeta = Path(carpeta)

        self.carpeta.mkdir(
            parents=True,
            exist_ok=True
        )

    def _ruta(self, pdf):

        nombre = Path(pdf).stem + ".json"

        return self.carpeta / nombre

    def existe(self, pdf):

        return self._ruta(pdf).exists()

    def guardar(self, pdf, objeto):

        with open(
            self._ruta(pdf),
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                objeto,
                f,
                indent=4,
                ensure_ascii=False
            )

    def cargar(self, pdf):

        with open(
            self._ruta(pdf),
            encoding="utf-8"
        ) as f:

            return json.load(f)

