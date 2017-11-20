var usuarioElige = prompt("piedra, papel o tijera?");
var computadoraElige = Math.random();
if (computadoraElige <0,34){
	computadoraElige = "piedra";
}else if(computadoraElige <=0.67){
	computadoraElige = "papel";
}else{
	computadoraElige = "tijera";
}
var comparar = function(eleccion1, eleccion2) {
    if (eleccion1 === eleccion2) {        
        return "¡Es un empate!";
        }
    if (elecion1 === "piedra"){
        if (eleccion2 === "tijera"){
            return "piedra gana"
        }else{
            return "papel gana"
            }
        }
    };
    
    
comparar(computadoraElige, usuarioElige);console.log("hola ")

var menu = ""

console.log(menu)

