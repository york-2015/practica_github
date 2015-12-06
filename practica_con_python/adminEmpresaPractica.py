"""#TkInter, EasyGUI 

ganancia = 0
costosDeProducion = 0


ganaciaBruta = ganancia - costosDeProducion

#gastos

gastosAdministrativo = 0

gastosComercial = 0 

gastoFinanciero = 0

sumaGastos = gastoFinanciero + gastosComercial + gastosAdministrativos

perdidaNeta = sumaGastos - ganaciaBruta

#activos 
activoDeUso = 0  
activoDeDisponibilidad = 0
activoDeCredito = 0
activoSuma = activoDeDisponibilidad + activoDeCredito + activoDeUso
#pasivo
pasivoComercial = 0
pasivoFiscal = 0
pasivoFinanciero = 0
pasivoSuma = pasivoFinanciero + pasivoComercial + pasivoFiscal
#patrimonio neto 
patrimonioNetoSuma = 0

##############Resultado del ejercicio##############################3
#A la suma del patrimonio se le resta la perdida neta 
patrimonioNetoSuma -= perdidaNeta
            
####Ecuacion patrimonial########

if activoSuma == pasivoSuma + patrimonioNetoSuma :
    print 'la ecuacino a dado %f', activoSuma 

 """
 
class FormulaDeverHaber():
    def __init__(self): #Pregunta lo que necesitan
        self.ganancia = raw_input("Cuales son las ganacia: ")
        self.costosDeProducion = raw_input("Cuales son los costos de produccion")
        #Gastos 
        self.gastosAdministrativo = raw_input("Cuales son los gastos ADMINISTRATIVOS: ")
        self.gastosComercial = raw_input("Cuales son los gastos COMERCIALES: ")
        self.gastoFinanciero = raw_input("Cuales son los gastos FINANCIEROS: ")
        #Activo
        self.deUso = raw_input("Cuales son los ACTIVOS DE USO: ")
        self.deDisponibilidad = raw_input("Cuales son los ACTIVOS DE DISPONIBILIDAD ")
        self.deCredito = raw_input("Cuales son los ACTIVOS DE CREDITO: ")
        #Pasivo
        self.pasivoComercial = raw_input("Cuales son los pasivos Comercial: ")
        self.pasivoFiscal = raw_input("Cuales son los pasivo Fiscal: ")
        self.pasivoFinanciero = raw_input("Cuales son los pasivo Financiero: ")
        
        #Pratimonio NETO
        self.sumaPN = 0 
        self.seguir = False
        self.y = "y"
        self.n = "n"

        while self.seguir != True: 
            self.patrimonioNeto = int(raw_input("Cuales son los Patrimonio Neto: "))
            self.gregarMasPN = str(raw_input("QUIERES AGREGAS MAS A PN Y/N: "))
            
            if self.gregarMasPN == self.y or self.y.upper():
                self.sumaPN += int(self.patrimonioNeto) 
            elif self.gregarMasPN == self.n or self.n.upper():
                
                self.seguir = True
            else:
                print "No te entiendo, se \
                se cancela la operacion"
                self.seguir = True
        
        print self.sumaPN

        #####RESULTADO DEL EJERCICIO#####

cuenta1 = FormulaDeverHaber()


"""

preguntar los valores
    funcion preguntarValores
realisar las formualas con los valores tomados 
    funcion ganaciaBruta
    funcion gastosSumados
    funcion perdidaNeta
    funcion resultadoDelEjercicio
    funcion ecuacionPatrimonial
imprimir los resultados 
    funcion imprimirValores

DARLE UNA INTERFAS
"""


2