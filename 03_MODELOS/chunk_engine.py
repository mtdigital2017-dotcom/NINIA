
"""
=========================================
NINIA CHUNK ENGINE
Versión 1.0
=========================================
"""

import re


class ChunkEngine:

    def __init__(self,
                 max_palabras=500):

        self.max_palabras=max_palabras


    def dividir(self,texto):

        texto=re.sub(r"\s+"," ",texto)

        palabras=texto.split()

        chunks=[]

        for i in range(0,len(palabras),self.max_palabras):

            chunk=" ".join(
                palabras[i:i+self.max_palabras]
            )

            chunks.append(chunk)

        return chunks
