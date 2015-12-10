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
        self.sumaPN = 0 #Aqui se guarda la suma del patrimonio neto 
        self.seguir = False
        self.y = "y"
        self.n = "n"

        while self.seguir != True: 
            self.patrimonioNeto = int(raw_input("Cuales son los Patrimonio Neto: "))
            self.gregarMasPN = str(raw_input("QUIERES AGREGAS MAS A PN Y/N: "))
            
            if self.gregarMasPN in (self.y, self.y.upper()):
                self.sumaPN += int(self.patrimonioNeto) 
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
    def patrimonioNeto(self):
        self.totalPatrimonioNeto = self.sumaPN 
    def ecuacionPatrimonial(self, a, p, pn):
        #variables 
        self.a = a 
        self.p = p
        self.pn = pn 
        self.sumaPPnCopy = self.sumaPPn
        if a == int(p + pn):
            self.sumaPPnCopy = p + pn
            return "es true"+ self.sumaPPnCopy
        else:
            return "a no es igual "
    def __str__(self):
        self.activoI = self.activo()
        self.pasivoI = self.pasivo()
        self.patrimonioNetoI = self.patrimonioNeto()
        self.ePMC = self.ecuacionPatrimonial()

        return 'El pasivo es +++ El activo es +++ El patrimonio neto es '

    



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


