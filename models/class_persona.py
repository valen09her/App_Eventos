class Persona:

    def __init__(self,nombre,dni,edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def comprarEntrada(self):
        print("Entrada comprada")