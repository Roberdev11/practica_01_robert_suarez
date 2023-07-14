"""
PREGUNTA N°003
 Crear un programa usando decoradores para medir el tiempo de
ejecución.
Reglas:
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo, multiplicación de 4 números (o x números)
para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**) y visualizar los resultados con un mínimo tres ejemplos.
"""
import time
def ejecucion(func):
    def wrapper(*args, **kwargs):
        empezar = time.time()
        result = func(*args, **kwargs)
        finalizar = time.time()
        print("Tiempo transcurrido: {} segundos".format(finalizar - empezar))
        return result
    return wrapper
@ejecucion
def multiplicar(a, b, c, d):
    return a * b * c * d

print(multiplicar(1, 2, 3, 4))
print(multiplicar(10, 20, 30, 40))
