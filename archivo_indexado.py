import os
import json

class ArchivoIndexado:
    def __init__(self, ruta_datos, ruta_indice):
        self.ruta_datos = ruta_datos
        self.ruta_indice = ruta_indice
        self._inicializar()

    def _inicializar(self):
        for ruta in [self.ruta_datos, self.ruta_indice]:
            if not os.path.exists(ruta):
                with open(ruta, 'w', encoding='utf-8') as f:
                    json.dump([] if ruta == self.ruta_datos else {}, f)

    def guardar_registro(self, registro, clave):
        datos = self.cargar_datos()
        indice = self.cargar_indice()
        indice[clave] = len(datos)
        datos.append(registro)
        self._guardar_datos(datos)
        self._guardar_indice(indice)

    def buscar_por_indice(self, clave):
        indice = self.cargar_indice()
        if clave in indice:
            pos = indice[clave]
            datos = self.cargar_datos()
            if 0 <= pos < len(datos):
                return datos[pos]
        return None

    def cargar_datos(self):
        if not os.path.exists(self.ruta_datos):
            return []
        with open(self.ruta_datos, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _guardar_datos(self, datos):
        with open(self.ruta_datos, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)

    def cargar_indice(self):
        if not os.path.exists(self.ruta_indice):
            return {}
        with open(self.ruta_indice, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _guardar_indice(self, indice):
        with open(self.ruta_indice, 'w', encoding='utf-8') as f:
            json.dump(indice, f, indent=2, ensure_ascii=False)

    def obtener_indice_completo(self):
        return self.cargar_indice()