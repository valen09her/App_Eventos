from models.class_entrada import Entrada

class Tribuna(Entrada):

    def __init__(self, numeroBoleta, precio, numAsiento, grada):
        super().__init__(numeroBoleta, precio)
        self.numAsiento = numAsiento
        self.grada = grada