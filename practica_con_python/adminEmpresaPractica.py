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
        self.ganancia = int(raw_input("Cuales son las ganacia: "))
        self.costosDeProducion = int(raw_input("Cuales son los costos de produccion"))
        #Gastos 
        self.gastosAdministrativo = int(raw_input("Cuales son los gastos ADMINISTRATIVOS: "))
        self.gastosComercial = int(raw_input("Cuales son los gastos COMERCIALES: "))
        self.gastoFinanciero = int(raw_input("Cuales son los gastos FINANCIEROS: "))
        #Activo
        self.deUso = int(raw_input("Cuales son los ACTIVOS DE USO: "))
        self.deDisponibilidad = int(raw_input("Cuales son los ACTIVOS DE DISPONIBILIDAD "))
        self.deCredito = int(raw_input("Cuales son los ACTIVOS DE CREDITO: "))
        #Pasivo
        self.pasivoComercial = int(raw_input("Cuales son los pasivos Comercial: "))
        self.pasivoFiscal = int(raw_input("Cuales son los pasivo Fiscal: "))
        self.pasivoFinanciero = int(raw_input("Cuales son los pasivo Financiero: "))
        
        #Pratimonio NETO
        self.sumaPN = 0 #Aqui se guarda la suma del patrimonio neto 
        self.seguir = False
        self.y = "y"
        self.n = "n"

        while self.seguir != True: 
            self.patrimonioNeto = int(raw_input("Cuales son los Patrimonio Neto: "))
            self.gregarMasPN = str(raw_input("QUIERES AGREGAS MAS A PN Y/N: "))
            
            if self.gregarMasPN in (self.y, self.y.upper()):
                self.sumaPN += self.patrimonioNeto 
            elif self.gregarMasPN == self.n :
                
                self.seguir = True
            else:
                print "No te entiendo, se \
                se cancela la operacion"
                self.seguir = True
        
        print self.sumaPN

    def activo(self):
        self.activoTotal = self.pasivoComercial + self.pasivoFiscal + self.pasivoFinanciero
    def pasivo(self):
        self.pasivoTotal = self.deUso + self.deDisponibilidad + self.deCredito 
    


    def ecuacionPatrimonial(self, a, p, pn):
        #variables 
        self.a = a 
        self.p = p
        self.pn = pn 
        self.sumaPPnCopy = self.sumaPN
        #Si es igual di es true y la suma del pn 
        self.sumapMasN = self.p + self.pn
        if self.a == self.sumapMasN:
            return "es true"+ self.sumaPPnCopy
        else:
            return "a no es igual "
    
    def __str__(self):
        self.activoI = self.activo()
        self.pasivoI = self.pasivo()
         # pn-----------------------
        self.ePMC = self.ecuacionPatrimonial(self.activoI, self.pasivoI, self.sumaPN)

        """return "El pasivo es %i \nEl activo es %i \nEl patrimonio neto es %i \
                                \n La ecuacion patrimonial es %i" & self.pasivoI, self.activoI,\
                                self.patrimonioNetoSumaI, self.ePMC 
                        """
        return self.ePMC
    



        #####RESULTADO DEL EJERCICIO#####

cuenta1 = FormulaDeverHaber()

print cuenta1############################################

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


