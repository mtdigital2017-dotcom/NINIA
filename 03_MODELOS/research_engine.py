
import os

import config

from document_loader import DocumentLoader
from chunk_engine import ChunkEngine
from llm_extractor import LLMExtractor
from fusion_engine import FusionEngine
from cache_manager import CacheManager
from knowledge_object import KnowledgeObject


class ResearchEngine:

    def __init__(self, prompt):

        self.loader = DocumentLoader()

        self.chunker = ChunkEngine()

        self.llm = LLMExtractor(
            os.environ["GEMINI_API_KEY"]
        )

        self.fusion = FusionEngine()

        self.cache = CacheManager(
            config.DATA / "cache"
        )

        self.prompt = prompt

    def procesar_pdf(self, ruta_pdf):

        # -----------------------------------
        # CACHE
        # -----------------------------------

        if self.cache.existe(ruta_pdf):

            print("⚡ Leyendo desde CACHE")

            datos = self.cache.cargar(ruta_pdf)

            return KnowledgeObject(**datos)

        # -----------------------------------
        # GEMINI
        # -----------------------------------

        print("📖 Leyendo PDF...")

        texto = self.loader.leer(ruta_pdf)

        print("✂️ Dividiendo documento...")

        chunks = self.chunker.dividir(texto)

        print(f"✅ Total chunks: {len(chunks)}")

        objetos = []

        for i, chunk in enumerate(chunks,1):

            print(f"🤖 Chunk {i}/{len(chunks)}")

            prompt = self.prompt.replace(
                "{texto}",
                chunk
            )

            obj = self.llm.extraer(prompt)

            objetos.append(obj)

        print("🧩 Fusionando...")

        final = self.fusion.fusionar(objetos)

        self.cache.guardar(
            ruta_pdf,
            final.to_dict()
        )

        print("💾 Guardado en CACHE")

        return final
