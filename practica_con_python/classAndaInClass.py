
class Personas(object):#crea la caja de la persona  
	def __init__(self, nombre = "", direccion = "", otra_boludes = "" , edad = ""):
		self.nombre = nombre
		self.direccion = direccion
		self.otra_boludes = otra_boludes
		self.edad = edad

	def __str__(self):
		return self.nombre+ " "+ self.direccion+ " "+ self.otra_boludes+ " "+ self.edad+ \
		"FUNCIONA"


class Preguntador(Personas):
	def __init__(self): #pregunta los datos con funciones fuera de la class 
		self.n1 = raw_input("primer 1nombre1a")
		self.n2 = raw_input("primer 1nombre1a")
		self.n3 = raw_input("primer 1nombre1a")
		self.n4 = raw_input("primer 1nombre1a")

	def poner_nombre(self):
		
		self.Persona = Personas(self.n1, self.n2, self.n3, self.n4)
		return self.Persona


	def lo_en_listo(self, lista_out):#crea una lista con los datos dados 
		self.lista_out = lista_out
		self.lista_llena = self.lista_out.append(self.Persona)
		
	
	def __str__(self):#lo hace visible 
		return self.lista_llena

pregunta = Preguntador()
#crear una lista de nombre unirlos con una lista de class

print pregunta.poner_nombre()
lista_nombre = []
pregunta.lo_en_listo(lista_nombre)

print lista_nombre