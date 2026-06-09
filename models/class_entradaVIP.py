from models.class_entrada import Entrada

class EntradaVIP(Entrada):

    def __init__(self, numeroBoleta, precio, numeroVIP):
        super().__init__(numeroBoleta, precio)
        self.numeroVIP = numeroVIP