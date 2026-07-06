
import re


class NormalizerEngine:

    def __init__(self):

        self.ods = {

            "ods 1":"ODS_1",
            "ods 2":"ODS_2",
            "ods 3":"ODS_3",
            "ods 4":"ODS_4",
            "ods 5":"ODS_5",
            "ods 8":"ODS_8",
            "ods 9":"ODS_9",
            "ods 10":"ODS_10",
            "ods 11":"ODS_11",
            "ods 16":"ODS_16",
            "ods 17":"ODS_17"

        }

        self.organizaciones = {

            "onu":"Naciones Unidas",
            "naciones unidas":"Naciones Unidas",
            "organización de las naciones unidas":"Naciones Unidas",
            "organizacion de las naciones unidas":"Naciones Unidas",
            "consejo de seguridad":"Naciones Unidas",
            "unesco":"UNESCO",
            "unicef":"UNICEF",
            "ocde":"OCDE"

        }

        self.tecnologias = {

            "ia":"Inteligencia Artificial",
            "artificial intelligence":"Inteligencia Artificial",
            "inteligencia artificial":"Inteligencia Artificial",
            "chatgpt":"ChatGPT",
            "gemini":"Gemini"

        }

    def normalizar_lista(self, lista, diccionario):

        salida = []

        for valor in lista:

            x = valor.lower().strip()

            agregado = False

            for clave, destino in diccionario.items():

                if clave in x:

                    salida.append(destino)

                    agregado = True

                    break

            if not agregado:

                salida.append(valor)

        return sorted(list(set(salida)))

