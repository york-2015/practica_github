class Personas(object):#crea la caja de la persona  
	def __init__(self, nombre = "", direccion = "", otra_boludes = "" , edad = ""):
		self.nombre = nombre
		self.direccion = direccion
		self.otra_boludes = otra_boludes
		self.edad = edad

	def __repr__(self):
		return self.nombre+ " "+ self.direccion+ " "+ self.otra_boludes+ " "+ self.edad+ \
		"FUNCIONA"


class Preguntador(Personas):
	def __init__(self): #pregunta los datos con funciones fuera de la class 
		self.n1 = raw_input("primer 1nombre1a") #-----esto se hace primero-----
		self.n2 = raw_input("primer 1nombre1a")
		self.n3 = raw_input("primer 1nombre1a")
		self.n4 = raw_input("primer 1nombre1a")

	def poner_nombre(self):#---------esto cuando lo llaman 
		
		self.personas = Personas(self.n1, self.n2, self.n3, self.n4)
		return self.personas


	def lo_en_listo(self, lista_out):#crea una lista con los datos dados 
		self.lista_out = lista_out#con la lista que elijas 
		self.poner_nombre_estenombre = self.poner_nombre()#
		self.lista_llena = self.lista_out.append(self.poner_nombre_estenombre)
		return self.lista_llena
	
"""lista_nombre = []
pregunta = Preguntador()
pregunta.lo_en_listo(lista_nombre)

print lista_nombre
"""

listaDeClases = []

listaId = [1, 2, 3]

for i in range(0, 3):
	listaId[i] = Preguntador()
	print listaId[i].poner_nombre()
	listaDeClases.append(listaId[i])


preguntarUser = raw_input("quieres provar la matris y/pass: ")

if preguntarUser == "y":
	print listaId[0][0]
else: 
	pass