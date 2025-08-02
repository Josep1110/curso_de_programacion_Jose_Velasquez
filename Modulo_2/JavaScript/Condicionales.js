//Eejercicio 1

let edad = prompt("Por favor, ingresa tu edad:");

if (edad >= 18){
    console.log("Es mayor de edad")
} else {
    console.log("Es menor de edad")
}

//Ejeercicio 2

let numero1 = prompt("Ingrese el primer numero:");
let numero2 = prompt("Ingrese el segundo numero:");

if (numero1 > numero2){
    console.log(`${numero1} es mayor que ${numero2}`);
} else if (numero1 < numero2){
    console.log(`${numero1} es menor que ${numero2}`);
} else {
    console.log("Ambos numeros son iguales");
}

//Ejercicio 3

let colorSemaforo = prompt("Color del semaforo:");
if (colorSemaforo === "verde"){
    console.log("Puede cruzar")
} else if (colorSemaforo === "amarillo"){
    console.log("Precaucion...");
} else if (colorSemaforo === "amarillo"){
    console.log("Precaucion...");
} else if (colorSemaforo === "rojo"){
    console.log("No puede cruzar");
} else {
    console.log("Color no valido")
}

//Ejercicio 4

let Edad = prompt("Ingrese su edad:");
let tieneticket = true

if (Edad >= 18 && tieneticket){
    console.log("Acceso concedido")
} else {
    console.log("Acceso denegado")
}

//Ejercicio 5

let montoCompra = prompt("Ingrese el monto de la compra:");
let preciofinal;

if (montoCompra > 100){
    preciofinal = montoCompra * 0.8;
} else if (montoCompra >= 50.01){
    preciofinal = montoCompra * 0.9;
} else {
    preciofinal = montoCompra;
}

console.log("Precio final: $" + preciofinal);
