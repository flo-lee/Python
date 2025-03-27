#OOP
#1Clases. class
#Propiedades y Atributos. self 
#acciones, métodos. def 
#objetos 

#clase PERSONA (clase padre)
#PROPIEDADES: Nombre, Edad, Altura, CI
#MÉTODOS: Acciones
#caminar() comer() dormir()

#objetos: Persona1= ("Juan", 19)

#SUBCLASES 
#ESTUDIANTES (clases hijos)
#PROPIEDADES codEstudiante, Carrera, semestre
#ACCIONES estudiar() jugar()

#DOCENTES 
#PROPIEDADES profesion, carrera
#ACCIONES evaluar() revisarExamen()

#SINTAXIS BÁSICA POO
#CLASE = CLASS
#PROPIEDADES = SELF 
#ACCIONES = DEF

#ej1.
#Paso 1: Definir la clase (para definir el nombre de la clase, iniciamos con Mayúsculas)
#Paso 2: Definir las propiedades de la claseclass Persona: 
#constructor
class Persona:
    def _init_(self, nombre, edad, altura):
#propiedades almacenarlos en variables
    self.nombre = nombre 
    self.edad = edad
    self.altura = altura 
    self.ci = ci
#Paso 3: Definir las acciones 
  def comer(self,comida):
      print(f"{self.nombre} Está comiendo {comida}")
  def dormir (self): #no necesita parámetro
      print(f"{self.nombre} Está durmiendo")
  def caminar (self):
      print(f"{self.nombre} Está caminando")
      
      
#crear los objetos 
persona1=Persona("Brian", 29, 1.75,"12997572") 
persona2=Persona("Mary", 29, 1.60, "12997571")


persona1.comer("Pan")
persona2.dormir()

#Crear la clase ESTUDIANTE 
#HERENCIA: HEREDAD ACCIONES Y ATRIBUTOS DE UNA CLASE PADRE
#subclase
#Paso 1. Definir la subclase
class Estudiante(Persona):
#crear constructor 
 def _init_(self, nombre, edad, altura, ci, codEstudiante, carrera, semestre):
#Paso 2. Herencia de atributos 
#método super()
#heredar los atributos
  super()._init(nombre, edad, altura, ci)
  self.codEstudiante = codEstudiante
  self.carrera = carrera
  self.semestre = semestre
#paso 3. acciones de un estudiante 

def estudiar (self):
  (f"{self.nombre} Está estudiando")
 
  estudiante1=Estudiante("Fred", 25, 1.75, 12997572,131047,"Ing. de Sistemas", 4)
  estudiante2=Estudiante()

estudiante1.dormir()
estudiante1.comer("Galletas")
estudiante1.estudiar()