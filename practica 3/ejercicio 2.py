import random

# Clase padre
class Juego:
    def __init__(self, numeroDeVidas: int):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0

    def reiniciaPartida(self):
        print("\nNueva partida iniciada. ¡Mucha suerte!")

    def actualizaRecord(self):
        self.record += 1
        print(f" Récord actualizado: {self.record}")

    def quitaVida(self):
        self.numeroDeVidas -= 1
        if self.numeroDeVidas > 0:
            print(f" Te queda(n) {self.numeroDeVidas} vida(s).")
            return True
        else:
            print(" Te has quedado sin vidas. Fin del juego.")
            return False


class JuegoAdivinaNumero(Juego):
    def __init__(self, vidas: int):
        super().__init__(vidas)
        self.numeroAAdivinar = 0

    def validaNumero(self, num: int) -> bool:
        """Valida que el número esté entre 0 y 10."""
        return 0 <= num <= 10

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while self.numeroDeVidas > 0:
            try:
                intento = int(input("Adivina un número entre 0 y 10: "))
            except ValueError:
                print(" Ingresa un número válido.")
                continue

            # Validación con el método polimórfico
            if not self.validaNumero(intento):
                continue

            if intento == self.numeroAAdivinar:
                print(" ¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if intento < self.numeroAAdivinar:
                        print(" El número a adivinar es mayor.")
                    else:
                        print(" El número a adivinar es menor.")
                else:
                    break


# Clase para pares
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, num: int) -> bool:
        if 0 <= num <= 10 and num % 2 == 0:
            return True
        else:
            print(" Solo puedes ingresar números pares entre 0 y 10.")
            return False


# Clase para impares
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, num: int) -> bool:
        if 0 <= num <= 10 and num % 2 != 0:
            return True
        else:
            print(" Solo puedes ingresar números impares entre 0 y 10.")
            return False


# Clase Aplicacion
class Aplicacion:
    def main(self):
        print("Juego Adivina Número")
        juego1 = JuegoAdivinaNumero(vidas=3)
        juego1.juega()

        print("\n Juego Adivina Número Par")
        juego2 = JuegoAdivinaPar(vidas=3)
        juego2.juega()

        print("\n Juego Adivina Número Impar")
        juego3 = JuegoAdivinaImpar(vidas=3)
        juego3.juega()


# Ejecución directa
app = Aplicacion()
app.main()
