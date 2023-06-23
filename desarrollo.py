"""
Pregunta N°001
"""
# lista almacenada
trabajadores = []

# consultas 1er trabajador
nombre1 = input("Ingrese el nombre del primer trabajador: ")
edad1 = int(input("Ingrese la edad del primer trabajador: "))

# Mostrar los tipos ingresados
print("Tipo de nombre1:", type(nombre1))
print("Tipo de edad1:", type(edad1))

# Agregar el primer trabajador a la lista
trabajadores.append((nombre1, edad1))

# consultas segundo trabajador
nombre2 = input("Ingrese el nombre del segundo trabajador: ")
edad2 = int(input("Ingrese la edad del segundo trabajador: "))

# Mostrar los tipos ingresados
print("Tipo de nombre2:", type(nombre2))
print("Tipo de edad2:", type(edad2))

# Agregar el segundo trabajador a la lista
trabajadores.append((nombre2, edad2))

# Calcular la suma de las edades
suma_edades = edad1 + edad2

#Lista final
print(trabajadores)
# Mostrar la suma de las edades
print("La suma de las edades de los trabajadores en la posición 0 y 1 es:", suma_edades)

"""
Pregunta N°002
"""
# lista con 10 valores
lista_valores = []
for i in range(1, 11):
    lista_valores.append(i)

# Llenar lista con los cubos
lista_cubos = []
for valor in lista_valores:
    lista_cubos.append(valor ** 3)

# Llenar lista nueva con los cuadrados
lista_cuadrados = []
for valor in lista_valores:
    lista_cuadrados.append(valor ** 2)

# Resultado
suma_inversa = []
for i in range(len(lista_cubos)):
    suma_inversa.append(lista_cubos[i] + lista_cuadrados[-(i + 1)])

print("Lista de valores:", lista_valores)
print("Lista de cubos:", lista_cubos)
print("Lista de cuadrados:", lista_cuadrados)
print("Suma inversa de ambas listas:", suma_inversa)

"""
Pregunta N°3
"""

# Diccionario
diccionario = {}

# Solicitar valores
nombre = input("Ingresa tu nombre: ")
apellidos = input("Ingresa tus apellidos: ")
edad = input("Ingresa tu edad: ")
dni = input("Ingresa tu DNI: ")

# Asignar los valores
diccionario['nombre'] = nombre
diccionario['apellidos'] = apellidos
diccionario['edad'] = edad
diccionario['dni'] = dni

# Mostrar los valores
print("Valores del diccionario: {}".format(diccionario))

# Agregar un nuevo key
profesion = input("Ingresa tu profesión: ")
diccionario['profesion'] = profesion

# Eliminar la clave 'dni'
diccionario.pop('dni')

# Mostrar el nuevo diccionario
print("Diccionario actualizado: {}".format(diccionario))

