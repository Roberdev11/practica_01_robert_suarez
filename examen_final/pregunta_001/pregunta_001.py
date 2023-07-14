"""
PREGUNTA N°°1
- Crear una función que le permitirá almacenar 10 números aleatorios en una
lista y finalmente los imprimirá por consola al llamar la función.
- Crear una función que le permita almacenar los números no repetidos de la
lista anterior, retornar este valor e imprimirlo por consola.
- Crear una función donde se creará una lista para ordenar de mayor a menor
la lista que se creó en el ítem anterior (número no repetidos) y otra lista
para ordenarlas de menor a mayor, retornar este valor e imprimirlos por
consola.
- Crear una función para indicar cuál es mayor número de la lista (lista del
ítem 2), retornar este valor e imprimirlo por consola.

"""

import random

def generar_lista_aleatoria():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 100))
    return lista

def eliminar_repetidos(lista):
    lista_sin_repetidos = list(set(lista))
    return lista_sin_repetidos

def ordenar_lista(lista):
    lista_mayor_a_menor = sorted(lista, reverse=True)
    lista_menor_a_mayor = sorted(lista)
    return lista_mayor_a_menor, lista_menor_a_mayor

def encontrar_maximo(lista):
    maximo = max(lista)
    return maximo

