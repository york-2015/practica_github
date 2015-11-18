

class Personas(object):
	def __init__(self, nombre = "", direccion = "", otra_boludes = "" , edad = ""):
		self.nombre = nombre
		self.direccion = direccion
		self.otra_boludes = otra_boludes
		self.edad = edad

	def __str__(self):
		return self.nombre+ " "+ self.direccion+ " "+ self.otra_boludes+ " "+ self.edad+ \
		"FUNCIONA"


class Preguntador(Personas):
	def __init__(self): #pregunta los tados con funciones fuera de la class 
		self.n1 = raw_input("primer 1nombre1a")
		self.n2 = raw_input("primer 1nombre1a")
		self.n3 = raw_input("primer 1nombre1a")
		self.n4 = raw_input("primer 1nombre1a")

	def poner_nombre(self):
		
		hola2 = Personas(self.n1, self.n2, self.n3, self.n4)
		return hola2


pregunta = Preguntador()

print pregunta.poner_nombre()