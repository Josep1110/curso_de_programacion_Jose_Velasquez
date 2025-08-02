//Ejercicio 1

let Nombre = "Jose Velasquez";
let edad = 16;
let Es_Estudiante = true;

console.log("Nombre:", Nombre)
console.log("Edad:", edad)
console.log("Es estudiante:", Es_Estudiante)

//Ejercicio 2

let NombreUsuario = prompt("Por favor, ingresa tu nombre de usuario:");
let AnioNacimiento = prompt("Por favor, ingresa tu año de nacimiento:");

let AnioActual = 2025;
let EdadUsuario = AnioActual - Number(AnioNacimiento);

console.log(`Hola, ${NombreUsuario}, tienes aproximadamente ${EdadUsuario} años.`);


//Ejercicio 3 

let numero1 = prompt("Ingrese el primer numero:");
let numero2 = prompt(`Ingrese el segundo numero:`);

let num1 = Number(numero1)
let num2 = Number(numero2)

let suma = num1 + num2;
let resta = num1 - num2;
let multiplicacion = num1 * num2;
let division = num1 / num2;

console.log("Suma:", suma);
console.log("Resta:", resta);
console.log("Multiplicacion:", multiplicacion);
console.log("Division:", division);

//Ejercicio 4 

let baseRectangulo = prompt("Ingresa la base del rectangulo:");
let alturaRectangulo = prompt("Ingresa la altura del rectangulo:");

let base = Number(baseRectangulo)
let altura = Number(alturaRectangulo)

let area = base * altura;
let perimetro = 2 * (base + altura);

console.log("Area del rectangulo:", area);
console.log("Perimetro del rectangulo:", perimetro);

//Ejercicio 5

let edadUsuario = prompt("Por favor, ingresa tu edad:");

let edaduser = Number(edadUsuario)

let enRangolaboral = edaduser >= 18 && edaduser <= 64;

console.log("¿Esta en edad laboral?", enRangolaboral);