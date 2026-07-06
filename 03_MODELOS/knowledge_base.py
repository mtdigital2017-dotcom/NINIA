
import json
from pathlib import Path

class KnowledgeBase:

    def __init__(self, archivo):

        self.archivo = Path(archivo)

        if not self.archivo.exists():

            self.archivo.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            with open(
                self.archivo,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump([], f)

    def cargar(self):

        with open(
            self.archivo,
            encoding="utf-8"
        ) as f:

            return json.load(f)

    def guardar(self, datos):

        with open(
            self.archivo,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                datos,
                f,
                indent=4,
                ensure_ascii=False
            )

    def agregar(self, objeto):

        base = self.cargar()

        base.append(objeto)

        self.guardar(base)

    def upsert(self, objeto):

        base = self.cargar()

        archivo = objeto.get("archivo","")

        actualizado = False

        for i, doc in enumerate(base):

            if doc.get("archivo","") == archivo:

                base[i] = objeto

                actualizado = True

                break

        if not actualizado:

            base.append(objeto)

        self.guardar(base)

    def total(self):

        return len(self.cargar())

