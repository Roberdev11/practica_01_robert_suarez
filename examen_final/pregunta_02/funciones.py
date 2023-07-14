import random
import math

def generar_lista_aleatoria(tamano):
    lista = [random.randint(1, 100) for i in range(tamano)]
    return lista

def extraer_lista(contenido):
    for linea in contenido:
        if "Lista generada:" in linea:
            lista = eval(linea.split(":")[1])
            return lista

def calcular_raices(lista):
    raices = [math.sqrt(num) for num in lista]
    return raices
