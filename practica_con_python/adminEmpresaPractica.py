#TkInter, EasyGUI 

ganancia = 0
costosDeProducion = 


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

 
 
