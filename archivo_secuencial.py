import os
import json

class ArchivoSecuencial:
    def __init__(self, ruta):
        self.ruta = ruta
        if not os.path.exists(ruta):
            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def guardar(self, registros):
        with open(self.ruta, 'w', encoding='utf-8') as f:
            json.dump(registros, f, indent=2, ensure_ascii=False)

    def cargar(self):
        if not os.path.exists(self.ruta):
            return []
        with open(self.ruta, 'r', encoding='utf-8') as f:
            return json.load(f)