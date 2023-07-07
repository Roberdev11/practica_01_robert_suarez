"""
Pregunta N°001
"""
import datetime

class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.saldo = 0
        self.nacionalidad = "peruana"

    def solicitar_datos(self):
        while True:
            try:
                self.nombre = input("Ingrese su nombre: ")
                if not self.nombre.isalpha():
                    raise ValueError("Error: El nombre debe contener solo letras.")

                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError as e:
                print(str(e))

    def cumpleaños(self):
        self.edad += 1

    def obtener_fecha_registro(self):
        fecha_actual = datetime.datetime.now()
        return fecha_actual.strftime("%Y-%m-%d %H:%M")


# Crear instancia de la clase Persona
persona = Persona()

# Solicita nombre y edad
persona.solicitar_datos()

# Incrementar edad
persona.cumpleaños()
persona.cumpleaños()

# Mostrar edad actualizada
print("Edad actualizada:", persona.edad)

# Obtener fecha
fecha_registro = persona.obtener_fecha_registro()
print("Fecha de registro:", fecha_registro)
