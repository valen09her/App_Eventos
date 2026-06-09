from models.class_entrada import Entrada

class Palco(Entrada):

    def __init__(self, numeroBoleta, precio, idPalco, zona):
        super().__init__(numeroBoleta, precio)
        self.idPalco = idPalco
        self.zona = zona