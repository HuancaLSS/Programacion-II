import math

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, (int, float)): 
            return Vector3D(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3D):    
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Multiplicación no soportada")

    def __xor__(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normal(self):
        m = self.modulo()
        return Vector3D(self.x/m, self.y/m, self.z/m)

    def proyeccion(self, b):
        escalar = (self * b) / (b.modulo()**2)
        return b * escalar

    def componente(self, b):
        return (self * b) / b.modulo()

    def esPerpendicular(self, b):
        return abs(self * b) < 1e-9

    def esParalelo(self, b):
        return (self ^ b).modulo() < 1e-9

a = Vector3D(1, 0, 0)
b = Vector3D(0, 1, 0)

print("a =", a)
print("b =", b)

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b (dot) =", a * b)
print("a ^ b (cross) =", a ^ b)
print("|a| =", a.modulo())
print("Normal de a =", a.normal())
print("Proyección de a sobre b =", a.proyeccion(b))
print("Componente de a en b =", a.componente(b))
print("¿a ⟂ b?", a.esPerpendicular(b))
print("¿a ∥ b?", a.esParalelo(b))
