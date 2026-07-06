
"""
NINIA
Google Sheets Manager
Versión 0.1
"""

import gspread
from google.auth import default

class SheetsManager:

    def __init__(self, sheet_id):

        creds, _ = default()

        gc = gspread.authorize(creds)

        self.sheet = gc.open_by_key(sheet_id)

        print("✅ Google Sheets conectado")


    def escribir(self, hoja, fila):

        ws = self.sheet.worksheet(hoja)

        ws.append_row(fila)

        print("Fila agregada correctamente.")
