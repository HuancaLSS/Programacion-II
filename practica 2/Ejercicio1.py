import math

class AlgebraVectorial:
    def __init__(self, a=None, b=None):
        if a is None and b is None:  
            self.vector_a = [0, 0, 0]
            self.vector_b = [0, 0, 0]
        elif b is None:  
            self.vector_a = a
            self.vector_b = [0, 0, 0]
        else:
            self.vector_a = a
            self.vector_b = b

    def modulo(self, v):
        return math.sqrt(sum([x**2 for x in v]))

    def producto_punto(self, a, b):
        return sum([a[i]*b[i] for i in range(len(a))])

    def producto_cruz(self, a, b):
        return [
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ]

    def es_perpendicular(self):
        return self.producto_punto(self.vector_a, self.vector_b) == 0

    def es_paralela(self):
        cruz = self.producto_cruz(self.vector_a, self.vector_b)
        return cruz == [0, 0, 0]

    def proyeccion(self):
        a, b = self.vector_a, self.vector_b
        factor = self.producto_punto(a, b) / (self.modulo(b) ** 2)
        return [factor * bi for bi in b]

    def componente(self):
        a, b = self.vector_a, self.vector_b
        return self.producto_punto(a, b) / self.modulo(b)


a = [2, 3, 4]
b = [5, 6, 7]

alg = AlgebraVectorial(a, b)

print("Vector a:", a)
print("Vector b:", b)
print("¿Son perpendiculares?:", alg.es_perpendicular())
print("¿Son paralelos?:", alg.es_paralela())
print("Proyección de a sobre b:", alg.proyeccion())
print("Componente de a en dirección b:", alg.componente())
