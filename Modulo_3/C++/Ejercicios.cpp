#include <iostream>
#include <cmath>
using namespace std;

//Ejercicio 1

int main() {
    cout << "¡Hola Mundo!" << endl;

    int edad;
    cout << "Introduce tu edad: ";
    cin >> edad;

    cout << "Tienes " << edad << " años." << endl;

    float x = 9.25;
    float y = 3.26;

    int multiplicacion1 = x * y;
    cout << "x * y es igual a: " << multiplicacion1 << endl;

    char letra = 'H';
    cout << "Char: " << letra << endl;
    char letra2 = 'O';
    cout << "Char: " << letra2 << endl;
    char letra3 = 'L';
    cout << "Char: " << letra3 << endl;
    char letra4 = 'A';
    cout << "Char: " << letra4 << endl;

    int numero;

    cout << "Ingrese un numero: ";
    cin >> numero;

    bool resultado = (numero % 2 == 0);

    cout << "¿Es par? " << resultado << endl;

    if (resultado) {
        cout << numero << " es par" << endl;
    } else {
        cout << numero << " es impar" << endl;
    }

//Ejercicio 2

    int num1;
    cout << "Ingrese el primer numero: ";
    cin >> num1;

    int num2;
    cout << "Ingrese el segundo numero: ";
    cin >> num2;

    int suma = num1 + num2;
    cout << num1 << " + " << num2 << " es igual a " << suma << endl;
    int resta = num1 - num2;
    cout << num1 << " - " << num2 << " es igual a " << resta << endl;
    int multiplicacion2 = num1 * num2;
    cout << num1 << " * " << num2 << " es igual a " << multiplicacion2 << endl;
    int division = num1 / num2;
    cout << num1 << " / " << num2 << " es igual a " << division << endl;
    int raiz = sqrt(num1);
    cout << "La raíz cuadrada de " << num1 << " es " << raiz << endl;
    int potencia = pow(num1, num2);
    cout << num1 << " elevado a " << num2 << " es " << potencia << endl;

//Ejercicio 3

    int edad2;
    cout << "Introduce tu edad: ";
    cin >> edad2;

    if (edad2 >= 18) {
        cout << "Eres mayor de edad." << endl;
    } else {
        cout << "Eres menor de edad." << endl;
    }

//Ejercicio 4

    #define LIMITE 10

    int num;
    cout << "Introduce un numero: ";
    cin >> num;
    
    cout << "Tabla de multiplicar del: " << num << endl;

    for (int i = 1; i <= 10; i++) {
        cout << num << " x " << i << " = " << (num * i) << endl;
    }

    return 0;
}