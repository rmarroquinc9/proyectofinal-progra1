class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        self.tamaño = 0
    
    def apilar(self, dato):
        nuevo_nodo = NodoPila(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        self.tamaño += 1
    
    def desapilar(self):
        if self.tope is None:
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamaño -= 1
        return dato
    
    def ver_tope(self):
        return self.tope.dato if self.tope else None
    
    def obtener_todos(self):
        elementos = []
        actual = self.tope
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
    
    def obtener_metricas(self):
        return {
            "tamaño": self.tamaño,
            "vacia": self.tamaño == 0
        }