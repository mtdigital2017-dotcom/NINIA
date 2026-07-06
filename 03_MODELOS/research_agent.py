
from pipeline import Pipeline
from memory import Memory
from knowledge_base import KnowledgeBase


class ResearchAgent:

    def __init__(self):

        print("="*60)
        print("NINIA RESEARCH AGENT")
        print("="*60)

        self.pipeline = Pipeline()
        self.memory = Memory()
        self.base = KnowledgeBase()

    def analizar_documento(self, ruta_pdf):

        if self.memory.ya_procesado(ruta_pdf):

            print("⚠ Documento ya procesado.")
            return None

        print("Analizando:", ruta_pdf)

        resultado = self.pipeline.procesar_pdf(ruta_pdf)

        self.base.guardar(resultado)

        self.memory.registrar(ruta_pdf)

        print("✅ Guardado en Knowledge Base")

        return resultado

    def analizar_carpeta(self, carpeta):

        return self.pipeline.ejecutar(carpeta)
