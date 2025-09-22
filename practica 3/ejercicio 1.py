import random

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

    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)

        while self.numeroDeVidas > 0:
            try:
                intento = int(input("Adivina un número entre 0 y 10: "))
            except ValueError:
                print(" Ingresa un número válido.")
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

class Aplicacion:
    def main(self):
        juego = JuegoAdivinaNumero(vidas=3)
        juego.juega()

app = Aplicacion()
app.main()
