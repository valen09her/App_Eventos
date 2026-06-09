class Entrada:

    def __init__(self, numeroBoleta, precio):
        self.numeroBoleta = numeroBoleta
        self.precio = precio

    def venderEntrada(self):
        print("Entrada vendida")

    def cambiarPrecio(self, nuevoPrecio):
        self.precio = nuevoPrecio