"""
Pregunta N°002
"""
class Persona:
    def __init__(self, nombre, edad, saldo):
        self.nombre = nombre
        self.edad = edad
        self.saldo = saldo
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

    def transferencia(self, otra_persona, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            otra_persona.saldo += monto
            print("Transferencia realizada.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        return self.saldo


persona1 = Persona("Juan", 25, 1000)
persona2 = Persona("María", 30, 500)

monto_transferencia = 200
print('La persona 1: {} con saldo inicial de: {} transfiere: {} a persona 2: {}'.format(persona1.nombre,persona1.saldo,monto_transferencia,persona2.nombre))

persona1.transferencia(persona2, monto_transferencia)

print("El saldo final de Juan es: {}".format(persona1.mostrar_saldo()))
print("El saldo final de Maria es: {}".format(persona2.mostrar_saldo()))

