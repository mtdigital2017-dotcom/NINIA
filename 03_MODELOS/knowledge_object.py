
from dataclasses import dataclass, field, asdict

@dataclass
class KnowledgeObject:

    # Documento
    archivo:str=""
    chunk:int=0

    titulo:str=""
    tipo_documento:str=""

    autores:list=field(default_factory=list)

    organizacion:str=""
    pais:str=""
    region:str=""
    idioma:str=""
    anio:str=""

    tema_principal:str=""
    subtemas:list=field(default_factory=list)

    # Investigación
    problemas:list=field(default_factory=list)
    riesgos:list=field(default_factory=list)
    factores_protectores:list=field(default_factory=list)

    actores:list=field(default_factory=list)
    instituciones:list=field(default_factory=list)

    organizaciones:list=field(default_factory=list)
    personas:list=field(default_factory=list)
    lugares:list=field(default_factory=list)

    plataformas:list=field(default_factory=list)
    tecnologias:list=field(default_factory=list)

    grupo_etario:list=field(default_factory=list)

    estrategias:list=field(default_factory=list)
    intervenciones:list=field(default_factory=list)

    competencias_AMI:list=field(default_factory=list)

    ods:list=field(default_factory=list)

    marco_normativo:list=field(default_factory=list)

    hallazgos:list=field(default_factory=list)

    recomendaciones:list=field(default_factory=list)

    palabras_clave:list=field(default_factory=list)

    nivel_evidencia:str=""

    resumen:str=""

    clasificacion:dict=field(default_factory=dict)

    confianza:float=0.0

    def to_dict(self):
        return asdict(self)
