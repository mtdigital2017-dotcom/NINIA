
"""
=========================================
NINIA ENTITY EXTRACTOR v3
=========================================
"""

import re


class EntityExtractor:

    PATRONES = {

        "organizaciones":[

            r"\bUNESCO\b",
            r"\bUNICEF\b",
            r"\bONU\b",
            r"\bOCDE\b",
            r"\bOMS\b",

            r"Naciones Unidas",
            r"Consejo de Seguridad",
            r"Secretario General",
            r"Carta de las Naciones Unidas",
            r"Convenios de Ginebra"

        ],

        "riesgos":[

            r"desinformación",
            r"desinformacion",
            r"deepfake",
            r"grooming",
            r"ciberacoso",
            r"violencia digital"

        ],

        "plataformas":[

            r"TikTok",
            r"Instagram",
            r"Facebook",
            r"YouTube",
            r"Discord",
            r"Telegram",
            r"Roblox",
            r"\bX\b",
            r"Twitter"

        ],

        "tecnologias":[

            r"inteligencia artificial",
            r"\bIA\b",
            r"ChatGPT",
            r"Gemini"

        ]

    }


    def extraer(self,texto):

        resultado={}

        for categoria,patrones in self.PATRONES.items():

            encontrados=[]

            for patron in patrones:

                encontrados.extend(

                    re.findall(
                        patron,
                        texto,
                        flags=re.IGNORECASE
                    )

                )

            resultado[categoria]=sorted(

                list(
                    set(encontrados)
                )

            )

        return resultado
