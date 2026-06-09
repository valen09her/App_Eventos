from models.class_persona import Persona

class NoSocio(Persona):

    def __init__(self,nombre,dni,edad,numCuenta):
        super().__init__(nombre,dni,edad)
        self.numCuenta = numCuenta