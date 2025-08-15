<?php

//Ejercicio 1

//Se declaran los contadores
$pares = 0;
$impares = 0;

//Se recorren los numeros del 1 al 50
for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) { //Si es divisible entre 2, es par
        $pares++;
    } else { //Si no, es impar
        $impares++;
    }
}

//Se muestran los resultados
echo "Cantidad de numeros pares entre 1 y 50: " . $pares . "";
echo "\n";
echo "Cantidad de numeros impares entre 1 y 50: " . $impares . "";
echo "\n";

//Ejercicio 2
//En este ejercicio, en vez de limitarme al numero 8, simplemente coloque un readline para asi poder ver la tabla de multiplicar del numero que quiera

$numero = readline("\nIngrese un numero: ");  

echo "\nTabla de multiplicar del " . $numero . ":\n";

//Generamos la tabla del multiplicar del numero ingresado
for ($i = 1; $i <= 10; $i++) {
    echo $numero . " x " . $i . " = " . ($numero * $i) . "\n";
}
echo "\n";

//Ejercicio 3

$num_secreto = rand(1,10); //Se genera un numero aleatorio del 1 al 10

echo "Adivina el numero (entre 1 y 10):\n";

while ((int)trim(fgets(STDIN)) != $num_secreto) { //Empieza un bucle while
  echo "Incorrecto. Intenta otra vez ";
}

echo "Lo adivinaste!\n"; //El bucle termina una vez que adivinado el numero generado

//Ejercicio 4

$suma = 0; //Declaramos la variable para acumular la suma

//Recorremos los numeoros del 1 al 100
for ($i = 1; $i <= 100; $i++) {
  if ($i % 2 != 0) { //Si es impar, los sumamos
    $suma += $i;
  }
}

//Mostramos el resultado
echo "\nLa suma de todos los numeros impares del 1 al 100 es: " . $suma . "";
echo "\n";

//Ejercicio 5

$edad = readline("\nIntroduce tu edad: "); //Se usa en readline para introducir la edad

echo "Verificacion de edad para licencia de conducir:\n";
echo "Edad ingresada: " . $edad . " años\n";

//Se verifican los requisitos
if ($edad >= 18 && $edad <= 65) {
  echo "Cumple con los requisitos para obtener la licencia.\n"; 
} else {
    if ($edad < 18) {
    echo "No cumple con los requisitos para obtener la licencia.  Motivo: Es menor de 18 años\n";
    } else {
        echo "No cumple con los requisitos. Motivo: Supera el limite de 65 años\n";
    }   
    echo "\n";
}


//Ejercicio 6 

$tamaño = 5; //Se define el tamaño del cuadrado (5x5)

//Bucle externo para las filas 
for ($i = 1; $i <= $tamaño; $i++) {
    //Bucle interno para las columnas
  for ($l = 1; $l <= $tamaño; $l++) {
    echo "# "; //Se imprime el cuadro
  }
  echo "\n";
}

//Ejercicio 7

$num = readline("\nIngrese un numero: "); //Se utiliza de nuevo el readline para introducir un numero

//Condicionales para la clasificacion
if ($num > 0) {
  echo "El numero es positivo\n";
} elseif ($num < 0) {
  echo "El numero es negativo\n";
} else {
  echo "El numero es cero\n";
} 


//Ejercicio 8

echo "\n";
//Bucle para recorrer los numeros del 1 al 30
for ($i = 1; $i <= 30; $i++) {
    //Posteriormente, se verifican todas las condiciones
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo "MarTierra ";
    } elseif ($i % 3 == 0) {
        echo "Mar ";
    } elseif ($i % 5 == 0) {
        echo "Tierra ";
    } else { //Si no se cumple ninguna condicion anterior
        echo $i . " ";
    }
    echo "\n";
}

//Ejercicio 9

$temperatura = readline("\nIngrese la temperatura: "); //Otro readline mas para introducir la temperatura 

//Condicionales para la clasificacion
if ($temperatura < 10) {
  echo "Clima frio\n";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
  echo "Clima templado\n";
} else {
  echo "Clima Caluroso\n";
}

//Ejercicio 10

echo "\nCuenta regresiva para Año Nuevo:\n";

//Bucle descendente del 10 al 1
for ($i = 10; $i >= 1; $i--) {
    echo $i . "...\n";
}

//Mensaje final
echo "Feliz Año Nuevo! \n";
?>
