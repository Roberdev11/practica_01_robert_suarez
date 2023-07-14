from pregunta_001 import generar_lista_aleatoria, eliminar_repetidos, ordenar_lista, encontrar_maximo

# Lista aleatoria
lista_aleatoria = generar_lista_aleatoria()
print("Lista aleatoria: {}".format(lista_aleatoria))

# Eliminar números repetidos
lista_sin_repetidos = eliminar_repetidos(lista_aleatoria)
print("Lista sin números repetidos: {}".format(lista_sin_repetidos))

# Ordenar listas : de mayor a menor y de menor a mayor
lista_mayor_a_menor, lista_menor_a_mayor = ordenar_lista(lista_sin_repetidos)
print("Lista ordenada de mayor a menor: {}".format(lista_mayor_a_menor))
print("Lista ordenada de menor a mayor: {}".format(lista_menor_a_mayor))

# Encontrar el número máximo y mostrarlo
maximo_numero = encontrar_maximo(lista_sin_repetidos)
print("El número máximo es:", maximo_numero)