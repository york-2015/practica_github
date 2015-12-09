# -*- coding: utf-8 -*-
#ESTE CODIGO SE COLOCA PARA EVITAR ERRORS TYPOGRAFIA 

#Imprime lo que esta en la lista en el rango de la longitud de la lista...
def longitud_de_la_lista(lista):
	for i in range(len(lista)):
		print lista[i]

#Poner un validador de secuencia en un funcion o codido sin que lo imprima 

es_alfanumerico = "hol345asad"
si_es_falso_o_verdadero = es_alfanumerico.isalnum()

if si_es_falso_o_verdadero == False:
	print "algo"


#Te pregunta y guarda tus respeustas en una lista 
def lista_imput():
	lista_preguntas = ["cual es tu nombre: ", "Cual es tu edad: ", "Por que estudias: ", "Por que sigues: "]
	for i in range(len(lista_preguntas)):
		lista_preguntas[i] = lista_preguntas[i] + raw_input(lista_preguntas[i])
	
	for i in range(len(lista_preguntas)):
		print lista_preguntas[i]
#Te pregunta y guarda tus respeustas en una lista


#CONTROL DE MAYUSCULAS 
estaesy = "y" 
if continuar == estaesy or estaesy.upper():
	print "funciona canpeon"
#CONTROL DE MAYUSCULAS 


def lista_imput():
	lista_preguntas = []
	otra = True	#control del bucle while 
	i = 0	#El incremento de las lista
	while otra == True:
		continuar = raw_input("Quieres guardar una pregunta:(y/n)")#Pide al usuario si quiere guardar 
		#CONTROL DE RESPUETAS
		n = "n"
		y = "y" 
		if continuar == n or n.upper():
			otra = False
			break

		elif continuar == y or y.upper():
			i += 1 #ocupado el lugar vuelve acomensar 
			lista_preguntas[i] = raw_input("Pon tu pregunta aqui: ")#guardar en la lista las preguntas 
			#CONTROL DE RESPUETAS
		#MODTRAR PREGUNTAS GUARDADAS 
		mostrar = raw_input("quieres ver todas las preguntas(y/n): ")




		#MODTRAR PREGUNTAS GUARDADAS 	

#--------------------FUNCIONES BASICAS RETURN-----------------
def hola():
	return "hola que hay papa"


hola34 = hola()

print hola34
#--------------------FUNCIONES BASICAS RETURN-----------------	

#--------------------dividir una palabra -----------------	

# -*- coding: utf-8 -*-
def contracena():
	pedir = raw_input(u"dime tu cotracena: ")# la u activa el conding 
	
	for i in pedir:
		print i 

#contracena()

#--------------------dividir una palabra -----------------
	

#------------------------busca esto-------------------------
['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
li.index("example")
#------------------------busca esto-------------------------


#-----------------------------buscar esto--------------------------------
class Perro:
#############ATRIBUTO
    tipo = 'canino'                 # variable de clase compartida por todas las instancias
#############ATRIBUTO
#-----------------------METODO---------
    def __init__(self, nombre):
        self.nombre = nombre        # variable de instancia única para la instancia  
#-----------------------METODO---------

  >>> d = Perro('Fido')
  >>> e = Perro('Buddy')
  >>> d.tipo                    # compartido por todos los perros
  'canino'
  >>> e.tipo                    # compartido por todos los perros
  'canino'
  >>> d.nombre                  # único para d
  'Fido'
  >>> e.nombre                  # único para e
  'Buddy'
#-----------------------------buscar esto--------------------------------

#----------------------clase avansadas------------------------------------
class hotel(object):
	
	def __init__(self, nombre = '*', puntaje = 0, precio = float("inf") ):
		pass

	def esNumemro():
		#identifica si es un numero
		# Cuando un """precio"" viene en cero se reemplaza su valor por 
		#float("inf") (de modo de asegurar que el precio nunca quede en cero). 
		pass
		
		if es_cadena_no_vacia(nombre):# buscar esta funcion 
			#"""nombre"" y """ubicacion"" no deben generace vacias
			self.nombre = nombre
		else:
			raise TypeError ("nos amigo no debe estas vacio")

		if es_cadena_no_vacia(ubicacion):#buscar esta funcion 
			#"""nombre"" y """ubicacion"" no deben generace vacias
			self.ubicacion = ubicacion
		else:
			raise TypeError ("nos amigo no debe estas vacio")
		
	def __str__(self):# de buelve balores en string
        """ Muestra el hotel según lo requerido. """
        return self.nombre + " de "+ self.ubicacion+ \
                " - Puntaje: "+ str(self.puntaje) + " - Precio: "+ \
                str(self.precio)+ " pesos."
#----------------------clase avansadas------------------------------------


#----------------------------------------class---------------------------------

hola = raw_input("esto es una pregunta ")
adol = Personas(hola, hola, hola, hola)


print adol
#----------------------------------------class---------------------------------