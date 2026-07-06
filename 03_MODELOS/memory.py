
"""
=========================================
NINIA MEMORY
Versión 1.0
=========================================
"""

import hashlib
import os


class Memory:

    def __init__(self):

        self.archivo="/content/drive/MyDrive/NINIA/data/procesados.txt"

        os.makedirs(
            "/content/drive/MyDrive/NINIA/data",
            exist_ok=True
        )

        if not os.path.exists(self.archivo):

            open(self.archivo,"w").close()


    def _hash(self,ruta):

        return hashlib.md5(
            ruta.encode()
        ).hexdigest()


    def ya_procesado(self,ruta):

        codigo=self._hash(ruta)

        with open(self.archivo,"r") as f:

            return codigo in f.read()


    def registrar(self,ruta):

        codigo=self._hash(ruta)

        with open(self.archivo,"a") as f:

            f.write(codigo+"\n")
