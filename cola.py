class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0
    
    def encolar(self, dato):
        nuevo = NodoCola(dato)
        if self.frente is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo
        self.tamaño += 1
    
    def desencolar(self):
        if self.frente is None:
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        self.tamaño -= 1
        return dato
    
    def ver_frente(self):
        return self.frente.dato if self.frente else None
    
    def obtener_todos(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
    
    def obtener_metricas(self):
        return {
            "tamaño": self.tamaño,
            "vacia": self.tamaño == 0
        }