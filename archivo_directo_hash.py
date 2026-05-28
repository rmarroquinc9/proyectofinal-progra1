import os
import json

class ArchivoDirectoHash:
    def __init__(self, ruta):
        self.ruta = ruta
        if not os.path.exists(ruta):
            with open(ruta, 'w', encoding='utf-8') as f:
                json.dump({}, f)

    def insertar(self, clave, registro):
        datos = self.cargar()
        datos[clave] = registro
        self.guardar(datos)

    def buscar(self, clave):
        return self.cargar().get(clave)

    def eliminar(self, clave):
        datos = self.cargar()
        if clave in datos:
            del datos[clave]
            self.guardar(datos)
            return True
        return False

    def cargar(self):
        if not os.path.exists(self.ruta):
            return {}
        with open(self.ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def guardar(self, datos):
        with open(self.ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)