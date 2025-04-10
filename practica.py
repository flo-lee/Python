#Clase Padre
class Empleado:
     def __init__(self, nombre, ci, salario_base):
          self.salario_base = 2500

          def mostrarInfo(self):
               print(f"Nombre: {self.nombre}\n")
               print(f"CI: {self.ci}\n")
               print(f"Salario: {salario_base} Bs.\n")

          def calcularSalario(self, salario_base, pago):
               print("Salario Base: ")
          return pago
               
              

class EmpleadoTiempoCompleto(Empleado):
     def __init__(self, nombre, ci, salario_base, bono, salario):
          super().__init__(nombre,ci,salario_base)
          self.bono = 500

     def calcularSalario(self, salario_base, bono, pago):
        self.salario_base=self.salario_base+self.bono
          
class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, ci, salario_base, horas_trabajadas):
          super().__init__(nombre,ci,salario_base)
          self.horas_trabajadas = self.horas_trabajadas

    def calcularSalario(self, salario_base, horas_trabajadas, pago):
         pago = self.salario_base/self.horas_trabajadas


class EmpleadoFreelance(Empleado):
     def __init__(self, nombre, ci, salario_base, numero_proyectos, pago_por_proyecto):
          super().__init__(nombre,ci,salario_base)
          self.numero_proyectos = numero_proyectos 
          self.pago_por_proyecto = pago_por_proyecto  

     def calcularSalario(self, salario_base, numero_proyectos, pago_por_proyecto):
         self.salario_base= self.salario_base+(numero_proyectos*pago_por_proyecto)
 
empleado1 = EmpleadoFreelance ("Paul Allen", "12997572", 2500, 10, 900)
empleado1.mostrarInfo()
