# Clase Padre
class Empleado:
    def __init__(self, nombre, ci, salario_base):
        self.nombre = nombre
        self.ci = ci
        self.salario_base = salario_base

    def mostrarInfo(self):
        print(f"Nombre: {self.nombre}")
        print(f"CI: {self.ci}")
        print(f"Salario: {self.salario_base} Bs.\n")

    def calcularSalario(self):
        return self.salario_base

# Subclase tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, ci, salario_base, bono):
        super().__init__(nombre, ci, salario_base)
        self.bono = bono

    def calcularSalario(self):
        self.salario_base += self.bono
        return self.salario_base

# Subclase medio tiempo
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, ci, salario_base, horas_trabajadas):
        super().__init__(nombre, ci, salario_base)
        self.horas_trabajadas = horas_trabajadas

    def calcularSalario(self):
        self.salario_base = self.salario_base / self.horas_trabajadas
        return self.salario_base

# Subclase freelance
class EmpleadoFreelance(Empleado):
    def __init__(self, nombre, ci, salario_base, numero_proyectos, pago_por_proyecto):
        super().__init__(nombre, ci, salario_base)
        self.numero_proyectos = numero_proyectos
        self.pago_por_proyecto = pago_por_proyecto

    def calcularSalario(self):
        self.salario_base += self.numero_proyectos * self.pago_por_proyecto
        return self.salario_base

# Prueba con un objeto
empleado1 = EmpleadoFreelance("Paul Allen", "12997572", 2500, 10, 900)
empleado1.calcularSalario()
empleado1.mostrarInfo()