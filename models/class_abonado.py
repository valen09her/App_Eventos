from models.class_persona import Persona

class Abonado(Persona):

    def __init__(self,nombre,dni,edad,numAbono,fechaAbono):
        super().__init__(nombre,dni,edad)
        self.numAbono = numAbono
        self.fechaAbono = fechaAbono

    def renovarAbono(self):
        print("Abono renovado")