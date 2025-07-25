# Diccionario de alumnos
alumnos = {
    "Luis": {"Matemáticas", "Historia", "Biología"},
    "Ana": {"Matemáticas", "Física", "Química"},
    "Carlos": {"Historia", "Arte", "Biología"},
}

print("Diccionario original:")
print(alumnos)
print("=" *50)#Este print lo use varias veces para separar toda la informacion, porque aparecia todo seguido y no se distinguia bien


# 1. Mostrar todas las materias únicas
materias_unicas = set().union(*alumnos.values())
print("1. Materias únicas que cursan todos los alumnos:", materias_unicas)
print("=" *50)

# 2. Materias comunes entre Luis y Ana
comunes_luis_ana = alumnos["Luis"].intersection(alumnos["Ana"])
print("2. Materias comunes entre Luis y Ana:", comunes_luis_ana)
print("=" *50)

# 3. Agregar "Física" a Carlos
alumnos["Carlos"].add("Física")
print("3. Se agregó 'Física' a Carlos")
print("Estado actual del diccionario:")
print(alumnos)
print("=" *50)

# 4. Eliminar "Arte" de Carlos (si existe)
alumnos["Carlos"].discard("Arte")
print("4. Se eliminó 'Arte' de Carlos (si existía)")
print("Estado actual del diccionario:")
print(alumnos)
print("=" *50)

# 5. Imprimir cada alumno y cantidad de materias
print("5. Alumnos y cantidad de materias:")
for alumno, materias in alumnos.items():
    print(f"{alumno}: {len(materias)} materias - {materias}")
print("=" *50)

print("\nEstado final del diccionario:")
print(alumnos)