<?php

//Ejercicio 1

//Declaramos los contadores
$pares = 0;
$impares = 0;

for ($i = 1; $i <= 50; $i++) {
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Cantidad de numeros pares entre 1 y 50: " . $pares . "";
echo "\n";
echo "Cantidad de numeros impares entre 1 y 50: " . $impares . "";
echo "\n";


//Ejercicio 2

$numero = 8;

echo "\nTabla de multiplicar del " . $numero . ":\n";

for ($i = 1; $i <= 10; $i++) {
    echo "8 x " . $i . " = " . (8 * $i) . "\n";
}
echo "\n";

//Ejercicio 3

$num_secreto = rand(1,10);

echo "Adivina el numero (entre 1 y 10):\n";

while ((int)trim(fgets(STDIN)) != $num_secreto) {
  echo "Incorrecto. Intenta otra vez ";
}

echo "Lo adivinaste!\n";


//Ejercicio 4

$suma = 0;

for ($i = 1; $i <= 100; $i++) {
  if ($i % 2 != 0) {
    $suma += $i;
  }
}

echo "La suma de todos los numeros impares del 1 al 100 es: " . $suma . "";
echo "\n";

//Ejercicio 5

$edad = readline("Introduce tu edad: ");

echo "\nVerificacion de edad para licencia de conducir:\n";
echo "Edad ingresada: " . $edad . " años\n";

if ($edad >= 18 && $edad <= 65) {
  echo "Cumple con los requisitos para obtener la licencia.\n";
} else {
    if ($edad < 18) {
    echo "No cumple con los requisitos para obtener la licencia.  Motivo: Es menor de 18 años\n";
    } else {
        echo "No cumple con los requisitos. Motivo: Supera el limite de 65 años\n";
    }
}


//Ejercicio 6 

$tamaño = 5;

for ($i = 1; $i <= $tamaño; $i++) {
  for ($j = 1; $j <= $tamaño; $j++) {
    echo "# ";
  }
  echo "\n";
}

//Ejercicio 7

$num = readline("Ingrese un numero: ");

if ($num > 0) {
  echo "El numero es positivo";
} elseif ($num < 0) {
  echo "El numero es negativo";
} else {
  echo "El numero es cero";
} 


//Ejercicio 8

echo "\n";
for ($i = 1; $i <= 30; $i++) {
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo "MarTierra ";
    } elseif ($i % 3 == 0) {
        echo "Mar ";
    } elseif ($i % 5 == 0) {
        echo "Tierra ";
    } else {
        echo $i . " ";
    }
    echo "\n";
}

//Ejercicio 9

$temperatura = readline("Ingrese la temperatura: ");

if ($temperatura < 10) {
  echo "Clima frio";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
  echo "Clima templado";
} else {
  echo "Clima Caluroso";
}

//Ejercicio 10

echo "Cuenta "

?>