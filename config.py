
"""
=========================================
NINIA CONFIG
Versión 1.0
=========================================
"""

from pathlib import Path

# ==========================
# RUTA PRINCIPAL
# ==========================

ROOT = Path("/content/drive/MyDrive/NINIA")

# ==========================
# CARPETAS
# ==========================

DATA = ROOT / "data"

DOCUMENTOS = ROOT / "06_DOCUMENTOS"

PAPERS = DOCUMENTOS / "08_INVESTIGACION" / "Papers"

MODELOS = ROOT / "03_MODELOS"

# ==========================
# BASES
# ==========================

KNOWLEDGE_BASE = DATA / "knowledge_base.json"

INDEX = DATA / "index.json"

MEMORY = DATA / "procesados.txt"

# ==========================
# GOOGLE SHEETS
# ==========================

SHEET_NAME = "NINIA_MASTER"

# ==========================
# VERSION
# ==========================

VERSION = "1.0.0"
