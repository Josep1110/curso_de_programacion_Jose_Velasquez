//Ejercicio 1

const numero = prompt("Ingrese un numero");

console.log(`Tabla de multiplicar del ${numero}:`);
for (let i = 1; i <= 10; i++){
    console.log(`${numero} x ${i} = ${numero * i}`);
}

//Ejercicio 3

let contador = 10;

console.log("Cuenta regresiva iniciada.");
while(contador >= 0){
    console.log(contador);
    contador--;
}
console.log("¡Despegue!");

//Ejercicio 4

const NumeroSecreto = Math.floor(Math.random() * 10)+1;
let intentousuario = 0;

console.log("¡Bienvenido al juego de adivinar el numero secreto!");
console.log("El programa intentara adivinar un numero entre 1 y 10...");

while (intentousuario !== NumeroSecreto){
    intentousuario = Math.floor(Math.random() * 10) +1;
    console.log(`Intento: ${intentousuario}`);

    if (intentousuario === NumeroSecreto){
        console.log(`¡Correcto! El numero secreto era: ${NumeroSecreto}`)
    } else {
        console.log("Incorrecto, intentando nuevamente...");
    }

}
