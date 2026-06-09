from models.class_persona import Persona
from models.class_socio import Socio
from models.class_entrada import Entrada
from models.class_entradaVIP import EntradaVIP

boletas = {}


def ingresar():

    nombre = input("Nombre: ")
    dni = input("DNI: ")
    edad = int(input("Edad: "))

    numeroBoleta = input("Número de boleta: ")
    numeroVIP = input("Número VIP: ")

    persona = Persona(nombre, dni, edad)

    socio = Socio(
        nombre,
        dni,
        edad,
        1,
        "01/01/2026",
        "1 año",
        None
    )

    entrada = Entrada(numeroBoleta, 150000)

    entradaVIP = EntradaVIP(
        numeroBoleta,
        150000,
        numeroVIP
    )

    boletas[numeroBoleta] = {
        "persona": persona,
        "socio": socio,
        "entrada": entrada,
        "entradaVIP": entradaVIP
    }

    print("Boleta registrada correctamente")


def consultar():

    if len(boletas) == 0:
        print("No hay registros")
        return

    for codigo, datos in boletas.items():

        print("\n===================")

        print("Número de boleta:", codigo)

        print("Nombre:",
              datos["persona"].nombre)

        print("DNI:",
              datos["persona"].dni)

        print("Edad:",
              datos["persona"].edad)

        print("Precio:",
              datos["entrada"].precio)

        print("Número VIP:",
              datos["entradaVIP"].numeroVIP)


def consultarId():

    codigo = input("Número de boleta: ")

    if codigo in boletas:

        datos = boletas[codigo]

        print("\n===== BOLETA =====")

        print("Nombre:",
              datos["persona"].nombre)

        print("DNI:",
              datos["persona"].dni)

        print("Precio:",
              datos["entrada"].precio)

        print("Número VIP:",
              datos["entradaVIP"].numeroVIP)

    else:
        print("No existe")


def borrar():

    codigo = input("Número de boleta: ")

    if codigo in boletas:

        del boletas[codigo]

        print("Registro eliminado")

    else:
        print("No existe")