import math

def promedio(lista):
    return sum(lista) / len(lista)

def desviacion(lista):
    prom = promedio(lista)
    suma = sum((x - prom) ** 2 for x in lista)
    return math.sqrt(suma / (len(lista) - 1))

def main():
    datos = input("Ingrese 10 números separados por espacio: ").split()
    numeros = list(map(float, datos))
    prom = promedio(numeros)
    desv = desviacion(numeros)
    print(f"El promedio es {prom:.2f}")
    print(f"La desviación estándar es {desv:.5f}")

if __name__ == "__main__":
    main()
