from views.menu import menu
from controllers.administrador_boletas import ingresar, consultar, consultarId, borrar

while True:

    menu()

    opcion = input("Elija una opción: ")

    if opcion == "1":
        ingresar()

    elif opcion == "2":
        consultar()

    elif opcion == "3":
        consultarId()

    elif opcion == "4":
        borrar()

    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opción incorrecta")