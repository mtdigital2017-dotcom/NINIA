
from pathlib import Path

import config

from research_engine import ResearchEngine
from knowledge_base import KnowledgeBase


class CorpusProcessor:

    def __init__(self, prompt):

        self.engine = ResearchEngine(prompt)

        self.base = KnowledgeBase(
            config.KNOWLEDGE_BASE
        )

    def procesar_carpeta(self, carpeta):

        carpeta = Path(carpeta)

        pdfs = sorted(
            carpeta.glob("*.pdf")
        )

        print("="*70)
        print("TOTAL PDF:", len(pdfs))
        print("="*70)

        for i, pdf in enumerate(pdfs,1):

            print()

            print(f"[{i}/{len(pdfs)}] {pdf.name}")

            try:

                obj = self.engine.procesar_pdf(
                    str(pdf)
                )

                obj.archivo = pdf.name

                self.base.upsert(
                    obj.to_dict()
                )

                print("   ✅ Guardado")

            except Exception as e:

                print("   ❌ ERROR")

                print(e)

        print()

        print("="*70)

        print("TOTAL DOCUMENTOS EN BASE:")

        print(self.base.total())

        print("="*70)
