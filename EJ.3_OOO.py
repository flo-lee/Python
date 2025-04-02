'''
SUBCLASE -> HERENCIA DE ATRIBUTOS
Y MÉTODOS DE LA CLASE PADRE

HERENCIA -> OBTENER ATRIBUTOS Y 
ACCIONES (super())

class(ClasePadre) -> heredando

PASO 1: CREAR LA CLASE PADRE
'''
class Persona: 

 #Paso 2: Definir el constructor 
 def __init__(self, nombre, edad, ci ,celular)
  self.nombre = nombre #variante: self.nom = nombre
  self.edad = edad
  self.ci = ci
  self.celular = celular 
  
  #Paso 3. Crear las acciones o métodos.
  def comer(self, comida)
   print (f"{self.nombre} está comiendo {comida}")
  def dormir(self)
   print (f"{self.nombre} está durmiendo...")
 
 #Paso 4: Crear los objetos de la clase (fuera de la clase)
 persona1=Persona("Paul Allen", 23, "23987655", "+1 38828909")
 persona2=Persona("Patrick Bateman", 25, "23987659", "+1 38828988")
 
 persona1.comer("Langosta")
 persona2.dormir()
 persona1.dormir()
 persona2.comer("Caviar")
 
 #Paso 5: Crear SUBCLASE ESTUDIANTE
 
 #Paso 5.1: Definir la subclase.
 #NOTA: Para definir una subclase se UTILIZA class(ClasePadre)

class Estudiante(Persona): 
 #Paso 5.2: Definir el constructor
 def __init__(self, nombre, edad, ci, celular, carrera, codEstudiante, )
  #Paso 5.3: Heredar los atributos de la clase Padre con super() 
    super().__init__(nombre, edad, ci, celular)
    #Paso 5.4: definir los parametros nativos de la subclase Estudiante
    self.carrera=carrera
    self.codEstudiante=codEstudiante
  #Paso 5.5: Definir las acciones o métodos nativos
  
 def estudiar(self)
  print (f"{self.nombre} está estudiando...")
 def darExamen(self)
  print(f"{self.nombre} está dando exámen...")
#Paso 5.6: Crear los objetos de la subclase ESTUDIANTE

estudiante1=Estudiante("Rick", 60, "12997572","13104786", "Física", "131047")
estudiante2=Estudiante("Mini Rick", 59, "12997571", "78965432", "Química", "123456")


estudiante1.darExamen()
estudiante2.estudiar()
