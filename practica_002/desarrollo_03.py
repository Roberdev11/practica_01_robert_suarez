"""
Pregunta N°003
"""
def ingresar_datos():
    while True:
        try:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingrese un número válido.")

def division():
    while True:
        try:
            num1, num2 = ingresar_datos()
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
            break
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

def evaluar_suma():
    while True:
        try:
            num1, num2 = ingresar_datos()
            resultado = num1 + num2
            print("El resultado de la suma es:", resultado)
            break
        except ValueError:
            print("Error: Ingrese un número válido.")

def main():
    print("1. División")
    print("2. Evaluar suma")
    opcion = input("Seleccione una opción (1 o 2): ")

    if opcion == "1":
        division()
    elif opcion == "2":
        evaluar_suma()
    else:
        print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
