from models.class_carnet import Carnet

class Infantil(Carnet):

    def __init__(self,fechaCarnet,numCarnet,cuota,rebaje):
        super().__init__(fechaCarnet,numCarnet,cuota)
        self.rebaje = rebaje