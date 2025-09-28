from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcular_salario_mensual(self) -> float:
        pass

    def __str__(self):
        return f"Empleado: {self.nombre}"


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre: str, salario_anual: float):
        super().__init__(nombre)
        self.salario_anual = salario_anual

    def calcular_salario_mensual(self) -> float:
        return self.salario_anual / 12

    def __str__(self):
        return (f"Empleado Tiempo Completo: {self.nombre}, "
                f"Salario Anual = {self.salario_anual}, "
                f"Salario Mensual = {self.calcular_salario_mensual():.2f}")


class EmpleadoTiempoHorario(Empleado):
    def __init__(self, nombre: str, horas_trabajadas: float, tarifa_por_hora: float):
        super().__init__(nombre)
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario_mensual(self) -> float:
        return self.horas_trabajadas * self.tarifa_por_hora

    def __str__(self):
        return (f"Empleado Tiempo Horario: {self.nombre}, "
                f"Horas Trabajadas = {self.horas_trabajadas}, "
                f"Tarifa por Hora = {self.tarifa_por_hora}, "
                f"Salario Mensual = {self.calcular_salario_mensual():.2f}")


empleados = []

for i in range(3):
    nombre = input(f"Ingrese nombre del empleado tiempo completo {i+1}: ")
    salario_anual = float(input("Ingrese salario anual: "))
    empleados.append(EmpleadoTiempoCompleto(nombre, salario_anual))

for i in range(2):
    nombre = input(f"Ingrese nombre del empleado por horas {i+1}: ")
    horas = float(input("Ingrese horas trabajadas: "))
    tarifa = float(input("Ingrese tarifa por hora: "))
    empleados.append(EmpleadoTiempoHorario(nombre, horas, tarifa))

print("\n--- Lista de Empleados ---")
for e in empleados:
    print(f"{e.nombre} → Salario Mensual: {e.calcular_salario_mensual():.2f}")
