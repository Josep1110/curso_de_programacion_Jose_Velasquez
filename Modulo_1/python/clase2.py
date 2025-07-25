#ejercicio 1 

num1 = 5
num2 = 15

if num1 > num2: 
    print(f"{num1} es mayor que {num2}")
else:
     if num1 < num2:
      print(f"{num1} es menor que {num2}") 

#ejercicio 2 

numero1 = 20
numero2 = 15
numero3 = 10

if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} es el mayor de los tres")
if numero3 < numero1 and numero3 < numero2:
    print(f"{numero3} es el menor de los tres")

#ejercicio 3 

calificacion = int(input("Ingrese una calificacion numerica")) 
if calificacion >= 90 and calificacion <= 100:
    print("Tienes una A")
elif calificacion >= 80 and calificacion <= 89: 
    print("Tienes una B")
elif calificacion >= 70 and calificacion <= 79: 
    print("Tienes una C")
elif calificacion >= 60 and calificacion <= 69: 
    print("Tienes una D")
elif calificacion >= 0 and calificacion <= 59: 
    print("Tienes una F")

#ejercicio 4 

numero = int(input("Por favor, ingrese el numero"))
             
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es cero")


 
