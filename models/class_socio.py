from models.class_persona import Persona

class Socio(Persona):

    def __init__(self,nombre,dni,edad,numSocio,fechaSocio,tiempoSocio,carnet):
        super().__init__(nombre,dni,edad)
        self.numSocio = numSocio
        self.fechaSocio = fechaSocio
        self.tiempoSocio = tiempoSocio
        self.carnet = carnet