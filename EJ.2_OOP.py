#Comunicacion entre clases padre
#1.Clases intermedias (puente de comunicaciòn)

class Persona:
    def __init__(self, nombre, ci, edad):
     self.nombre=nombre
     self.ci=ci
     self.edad=edad
    def comer(self):
     print ("Está comiendo.")
    def inscribirse(self, sistema):
        print("Solicitud de inscripción")
        self.sistema=sistema



# Clase Padre
class Universidad:
    def __init__(self, sistema):
        self.sistema=sistema

    #ACCIONES DE LA UNIVERSIDAD
    def procesarSolicitud(self):
        print ("Universidad está procesando su solicitud...")

#Subclases
class Facultad(Universidad):
   pass 
class Carrera(Universidad):
   pass


#CLASE INTERMEDIA (PUENTE DE COMUNICACIÓN)
class SistemaRegistroUniversidad:
    def __init__(self, usuario, contraseña):
        self.usuario=usuario
        self.contraseña=contraseña
        self.mensaje=""
#ACCIONES DE LA CLASE INTERMEDIA
    def enviar (self, mensaje):
        print ("Mensaje enviado.")
        self.mensaje = mensaje
    def recibir(self):
        print ("Mensaje recibido.")
        return self.mensaje
    
#PROBAR LOS OBJETOS DE LA CLASE

sistema=SistemaRegistroUniversidad("ABC",123)
estudiante1=Persona("Florencia", 12997572, 20)
udabol=Universidad(sistema) #comunicador a variable "sistema" de Clase "Universidad"
estudiante1.inscribirse(sistema) 


sistema.enviar(mensaje="Enviando...")
sistema.recibir()