"""
Pregunta N°1
"""

#cual es el nombre de la persona 1 y luego cual es el nomb 2
data = ["Nombre trabajador N°1", "Edad trabajador N°1", "Nombre trabajador N°2", "Edad trabajador N°2"]
lista_nova = []

for i in range(0,len(data)):
    valores = input("¿Cual es tu " + data[i] + " ?")
    lista_nova.append(valores)

suma_edades = int(lista_nova[1]) + int(lista_nova[3])
print("La suma de edades de los trabajadores es: {}".format(suma_edades))

"""
Pregunta N°2
"""
ten_numbers = []
for num in range(1,11):
    ten_numbers.append(num)

cuadrados = [x*y for x,y in zip(ten_numbers,ten_numbers)]
cubos = [x*y*z for x,y,z in zip(ten_numbers,ten_numbers,ten_numbers)]

suma = list(map(sum, zip(cuadrados, cubos)))
rev = suma[::-1]
print(rev)






