import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_discriminante(self):
        return self.b**2 - 4 * self.a * self.c

    def get_raiz1(self):
        disc = self.get_discriminante()
        if disc < 0:
            return 0
        return (-self.b + math.sqrt(disc)) / (2 * self.a)

    def get_raiz2(self):
        disc = self.get_discriminante()
        if disc < 0:
            return 0
        return (-self.b - math.sqrt(disc)) / (2 * self.a)


def main():
    datos = input("Ingrese a, b, c: ").split()
    a, b, c = map(float, datos)

    eq = EcuacionCuadratica(a, b, c)
    disc = eq.get_discriminante()

    if disc > 0:
        print(f"La ecuación tiene dos raíces {eq.get_raiz1()} y {eq.get_raiz2()}")
    elif disc == 0:
        print(f"La ecuación tiene una raíz {eq.get_raiz1()}")
    else:
        print("La ecuación no tiene raíces reales")


if __name__ == "__main__":
    main()
