
import glob
import os

from research_agent import ResearchAgent


class MonitoringAgent:

    def __init__(self):

        self.agent = ResearchAgent()


    def ejecutar(self, carpeta):

        pdfs = glob.glob(
            os.path.join(carpeta, "**", "*.pdf"),
            recursive=True
        )

        print("="*70)
        print("PDF encontrados:", len(pdfs))
        print("="*70)

        procesados = 0

        for pdf in pdfs:

            print("\n--------------------------------------------------")
            print(pdf)

            resultado = self.agent.analizar_documento(pdf)

            if resultado is not None:
                procesados += 1

        print("\n========================================")
        print("Proceso terminado")
        print("Documentos nuevos:", procesados)
        print("========================================")
