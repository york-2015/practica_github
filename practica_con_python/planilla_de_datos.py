

class Preguntador():
	
	def __init__(self): #pregunta los tados con funciones fuera de la class 
		self.nombre_de_la_class = preguntar_nombre_clase()
		self.preguntar_los_datoos   = preguntar_los_datoos()
	
	def crea_una_class_nueeva(self):
		

		#------------puesto el nombre <ok>-------------------------------

		self.nombre_de_la_class = Personas()#el nombre eleguido pasa aki papi 
		#------------puesto el nombre <ok>-------------------------------

		#------------------------PONER LOS DATOS EN LA CLASS <ok>-------------
		self.nombre_de_la_class.nombre       = pedir_nombre()
		self.nombre_de_la_class.direccion    = pedir_direccion()
		self.nombre_de_la_class.edad         = pedir_edad()
		self.nombre_de_la_class.otra_boludes = pedir_otra_boludes()
		
		#------------------------PONER LOS DATOS EN LA CLASS <ok>-------------

		#------------------------FLATA LLAMAR A LA CLASS POR EL NOMBRE PUESTO-------------
		print self.nombre_de_la_class
		#------------------------FLATA LLAMAR A LA CLASS POR EL NOMBRE PUESTO-------------


		#-----------------------ultima parte del programa---------
		self.guardar_la_clase() 

		self.imprimir_class() 
		#-----------------------ultima parte del programa---------


class Personas():
	def __init__(self):
		pass
	def aki_estan_los_datos():
		pass

