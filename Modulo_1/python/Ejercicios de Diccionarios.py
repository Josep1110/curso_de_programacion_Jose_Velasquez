#actividad 1

diccionario = {"nombre": "Ana","edad": 2,"carrera": "Ingenieria"}

print("Nombre:", diccionario["nombre"])
print("Edad:", diccionario["edad"])
print("Carrera:", diccionario["carrera"])

for valor in diccionario.values():
    print("\nValor:", valor)
    print(f"Este es el valor de la clave: {valor}")
  
#actividad 2

banana = {"b": 1, "a": 3, "n": 2}

print("Cantidad de B en banana:", banana["b"])
print("Cantidad de A en banana:", banana["a"])
print("Cantidad de N en banana:", banana["n"])


#actividad 3

precios = {"manzana": 0.5, "banana": 0.3}

print("Manzana:", precios["manzana"])
print("Banana:", precios["banana"])

precios["banana"] = 0.4
print("\nDiccionario después de modificar el precio de la banana:", precios)

#actividad 4

paises_y_capitales = {"Francia": "Paris", "Italia": "Roma", "España": "Madrid"}

for clave, valor in paises_y_capitales.items():
    print(f"\nPais: {clave}, Capital: {valor}")



