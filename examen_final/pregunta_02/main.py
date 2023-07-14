"""
PREGUNTA N°002
Crear un programa para gestionar un fichero con diferentes
tipos de operaciones numéricas.
Reglas:
- El programa tendrá la función de crear el fichero con el nombre “notas.txt”
crearlo si no existe y el cual será dividido en dos archivos, uno principal
donde se llamará a las funciones que realizarán distintas operaciones en el
otro archivo la cual será llamada funciones.py.
- Crear una función donde se pedirá el tamaño de lista será ingresado por
consola (los números serán llenados de manera aleatoria dentro de la lista),
esta lista será escrita dentro del file “notas.txt”
- Crear una función donde se usará la librería math para obtener la raíz
cuadrada de los números que han sido llenados en la lista anterior y los
cuales serán escritos en el file “notas.txt”.
• Cerrar respectivamente los ficheros cada vez que se abra
"""

import funciones

def escribir_lista():

    tamano = int(input("Ingrese el tamaño de la lista: "))

    lista = funciones.generar_lista_aleatoria(tamano)
    archivo = open("notas.txt", "a")
    archivo.write("Lista generada: " + str(lista) + "\n")
    archivo.close()

def obtener_raices():

    archivo = open("notas.txt", "r")
    contenido = archivo.readlines()
    archivo.close()

    lista = funciones.extraer_lista(contenido)
    raices = funciones.calcular_raices(lista)
    archivo = open("notas.txt", "a")
    archivo.write("Raíces cuadradas: " + str(raices) + "\n")
    archivo.close()

escribir_lista()
obtener_raices()
