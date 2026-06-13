from vivero import menu as stock

def mostrar_menu():
    #console.log("[blue]═══════════════════════════════════════════════════")
    print("🌱 - VIVERO EL JACARANDÁ ")
    #console.log("[blue]═══════════════════════════════════════════════════")
    print(" ")
    print("1 - Stock de plantas")
    print("2 - Clientes")
    print("3 - Ventas")
    print("4 - Proveedores")
    print("5 - Encargos especiales")
    print("0 - Salir")
    print(" ")

def menu_principal():
    
    while True:

        mostrar_menu()

        op = int(input("Ingrese una opción: "))
        print(" ")

        if op < 0 or op > 5:
            print(" ")
            print("Ingrese una opcion valida")
            continue

        match op:
            case 0: 
                print(" ")
                print('"Un vivero es paciencia. Una planta tarda en crecer y un cliente tarda en volver.')
                print('Pero los dos vuelven, si los cuidás."')
                print("— Sofía, Vivero El Jacarandá")
                print(" ")
                print("------------------")
                print("SALIO DEL PROGRAMA")
                print("------------------")
              
                print(" ")
                break
            case 1:
                stock()
                continue
            case 2:
                pass
                #clientes()
                #continue
            case 3:
                pass
                #ventas()
                #continue
            case 4: 
                pass
                #proveedores()
                #continue
            case 5:
                pass
                #encargos()
                #continue

menu_principal()