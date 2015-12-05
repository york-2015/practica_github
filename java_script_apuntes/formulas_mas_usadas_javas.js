//------------------------comentarios--------------------------

//hola hola hola 


/*

hola que hay de nuevo 
con sartos de pagians 


*/

//------------------------comentarios--------------------------

//--------------------------comparadores------------------------------- 
 > Mayor que
 < Menor que
 <= Menor o igual que
 >= Mayor o igual que
 === Igual que
!== Distinto de
//--------------------------comparadores-------------------------------


//----------------------------mide en numeros el string-----------------

"cadena de mierda".length

//----------------------------mide en numeros el string-----------------

//--------------------------------------muestra lo quiere del string----------
"milanesas".substring(3,7);

//--------------------------------------muestra lo quiere del string----------

//-----------------------------cajas de dialogos----------------------------
confirm("loca de re loca, asi es la vida" );
//-----------------------------cajas de dialogos----------------------------





//----------------------variable una variable------------------

var algo = "algo algo" ;
var algo = 1000 ;
var algo = prompt("te pregunto algo");

algo = "te canbio de valor" //le doy otro significado

//var global

var algo = "hola"
//var local

var hola = function(){
	var hola2 = "variable "
	console.log(hola2);
};
//----------------------variable una variable------------------

//----------------------preguntar algo------------------------
var edad = prompt("¿Cuántos años tenés?");
//----------------------preguntar algo------------------------


//-----------------------------  for, else ----------------------

for (auto === perro)
{
	console.log("algo algo");
}
else
{
	console.log("algo algo 2 ");
}
//-----------------------------  for, else ----------------------


//-----------------------------imprimir----------------------

console.log("Qué bueno verte," + " " + nombre);

var string = "la puta madre";
console.log("Qué bueno verte, %s" , string ); //creoo

var nose = "hola esto es un string "
	console.log("esto es un texto\n%s", nose  );	

//-----------------------------imprimir----------------------

//---------------------------------funcion--------------------

var saludo = function (nombre) {
    console.log("Qué bueno verte," + " " + nombre);
};

saludo("jorge");
//---------------------------------funcion--------------------

//-------------------------------Comando return----------------------
var porDos = function(numero) {
    return numero * 2;
};

// llama a porDos acá
var nuevoNumero = porDos(8)
console.log(nuevoNumero);
 //SEGUNDO EJERSICIO+++++++++++++++++++++++++++++++++
var unCuarto = function(numero){
    return numero / 4;
    };

if (unCuarto(0) % 3 === 0 ) {
  console.log("La sentencia es verdadera");
} else {
  console.log("La sentencia es falsa");
}
//TERCER EJERCICIO+++++++++++++++++++++++++++++++++
var perimetroCaja = function(longitud, ancho)
{
    return longitud * 2 + ancho * 2;    
}
perimetroCaja(10, 5);
//cuarto ejercicio+++++++++++++++++++++++++++++++
var nombreCadena = function ( nombre) {
    return "hola, soy" + " " + nombre;
};
nombreCadena("jorge");



//-------------------------------Comando return----------------------


//---------------------------------random Math----------------------
var computadoraElige = Math.random()

//---------------------------------random Math----------------------

