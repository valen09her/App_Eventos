from models.class_carnet import Carnet

class Plata(Carnet):

    def __init__(self,fechaCarnet,numCarnet,cuota,descuento):
        super().__init__(fechaCarnet,numCarnet,cuota)
        self.descuento = descuento