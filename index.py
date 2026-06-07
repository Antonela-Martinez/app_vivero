from vivero import menu as stock

def menu_principal():
    while True:
        print("0- SALIR")
        print("1- STOCK")
        print("2- CLIENTES")
        print("3- VENTAS")
        print("4- PROVEEDOR")

        op = int(input("Ingrese una opción: "))

        if op < 0 or op > 5:
            print("Ingrese una opcion valida")
            continue

        match op:
            case 0: 
                print("SALIO DEL PROGRAMA")
                break
            case 1:
                stock()
                continue
            case 2:
                clientes()
                continue
            case 3:
                ventas()
                continue
            case 4: 
                proveedores()
                continue
            case 5:
                encargos()
                continue


def clientes():
    pass
def ventas():
    pass
def proveeedores():
    pass
def encargos():
    pass