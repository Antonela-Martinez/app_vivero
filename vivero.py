import os
import json


NOMBRE_ARCHIVO = os.path.join('datos', 'plantas.json')

SEC_INTERIOR = 'Interior'
SEC_EXTERIOR = 'Exterior'
SEC_INVERNADERO = 'Invernadero'
SEC_HUERTA = 'Huerta'


def leer_archivo():
    if os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, 'rt', encoding='UTF-8') as archivo:
            datos = json.load(archivo)
            return datos
    else:
        return []

def guardar_archivo(datos):
    with open(NOMBRE_ARCHIVO, 'wt', encoding='UTF-8') as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=2)

def ingresar_entero(msj:str)->int:
    a_retornar = input(msj)
    while not a_retornar.isnumeric():
        print("ERROR!! EL VALOR DEBE SER NUMERICO")
        a_retornar = input(msj)
    return int(a_retornar)

def ingresar_float(msj: str) -> float:
    a_retornar = input(msj).strip()
    while True:
        if not a_retornar.replace(".", "", 1).lstrip("-").isdigit():
            print("ERROR!! EL VALOR DEBE SER NUMERICO")
        else:
            valor = float(a_retornar)
            if valor < 0:
                print("ERROR!! EL VALOR DEBE SER MAYOR O IGUAL A CERO")
            else:
                return valor  #válido, salimos de la función
        # Pedir nuevamente
        a_retornar = input(msj).strip()

#---------------------------------------------------------------------------
# 1) Cargar una planta nueva cuando llega o cuando producimos una variedad nueva
#----------------------------------------------------------------------------


def cargar_planta():

    plantas = leer_archivo()

    nombre_comun = input("Ingrese nombre comun de la planta: ").capitalize().strip()
    while not nombre_comun:
        print("ERROR! EL CAMPO NOMBRE NO PUEDE ESTAR VACIO")
        nombre_comun = input("Ingrese nuevamente nombre comun: ").capitalize().strip()

    nombre_cientifico = input("Ingrese nombre cientifico de la planta: ").capitalize().strip()
    while not nombre_cientifico:
        print("ERROR! EL CAMPO NOMBRE CIENTIFICO NO PUEDE ESTAR VACIO")
        nombre_cientifico = input("Ingrese nuevamente nombre cientifico: ").capitalize().strip()

    categoria = input("Ingrese categoria (ÁRBOL, ARBUSTO, SUCULENTA, AROMÁTICA, FRUTAL, ORNAMENTAL): ").capitalize().strip()
    while not categoria:
        print("ERROR! EL CAMPO CATEGORIA NO PUEDE ESTAR VACIO")
        categoria = input("Ingrese nuevamente categoria: ").capitalize().strip()
        
    sector = input("Ingrese sector: \n- INTERIOR\n- MEXTERIOR\n- HUERTA\n- INVERNADERO\n ").capitalize().strip()
    while not sector:
        print("ERROR! EL CAMPO SECTOR NO PUEDE ESTAR VACIO")
        sector = input("Ingrese nuevamente el sector: ").capitalize().strip()

    cantidad = ingresar_entero("Ingrese nuevo stock de la planta: ")

    precio = ingresar_float("ingrese el precio unitario: ")

    cuidados_basicos = input("Ingrese cuaidados basicos de la planta: ").strip()  
    while not cuidados_basicos:
        print("ERROR! EL CAMPO CUIDADOS BASICOS NO PUEDE ESTAR VACIO")
        cuidados_basicos = input("Ingrese nuevamente cuaidados basicos: ").strip()

    id = 1
    if(len(plantas)>0):
        ultima_planta = plantas[-1]
        id = ultima_planta["id"]+1

    planta = {
        "id":id,
        "nombre_comun":nombre_comun,
        "nombre_cientifico":nombre_cientifico,
        "categoria":categoria,
        "sector":sector,
        "cantidad":cantidad,
        "precio":precio,
        "cuidados_basicos":cuidados_basicos
    }
    plantas.append(planta)
    guardar_archivo(plantas)
    print(" ")
    print(f"✅ La planta {planta['nombre_comun'].upper()} se ha guardado correctamente.")


#--------------------------------------------------------------------------------------------
# 2) Ver el listado completo, y poder filtrar por sector (interior, exterior, invernadero, huerta) 
# o por categoría (árboles, arbustos, suculentas, aromáticas, frutales, ornamentales)
#--------------------------------------------------------------------------------------------


def filtrar_por_sector(archivo):
    sector = input('Ingrese sector (INTERIOR-EXTERIOR-HUERTA-INVERNADERO): ').capitalize()

    while not (sector == SEC_EXTERIOR or sector == SEC_HUERTA or sector == SEC_INTERIOR or SEC_INVERNADERO): 
        sector = input('Ingrese el sector correspondiente (INTERIOR-EXTERIOR-HUERTA-INVERNADERO): ').capitalize()

    indice = 0
    for planta in archivo:
        if sector in planta['sector']:
            print (planta)
            indice+= indice
        elif not sector in planta['sector']:
            indice+= indice

def filtrar_por_categoria(archivo):
    categoria = input('Ingrese categoria (ÁRBOL-ARBUSTO-SUCULENTA-AROMÁTICA-FRUTAL-ORNAMENTAL): ')

    indice = 0
    for planta in archivo:
        if categoria in planta['categoria']:
            print (planta)
            indice+= indice
        elif not categoria in planta['categoria']:
            indice+= indice


def listar_plantas():
    plantas = leer_archivo()
    for planta in plantas:
        print(planta)

    filtrar = input("¿Desea filtrar por sector (INGRESE S) o categoria (INGRESE C)? ")

    if filtrar == 's':
        filtrar_por_sector(plantas)
    elif filtrar == 'c':
        filtrar_por_categoria(plantas)


#-------------------------------------------------------------
# 3) Buscar una planta por nombre común o por nombre científico.
#-------------------------------------------------------------


def buscar_planta():
    plantas = leer_archivo()
    nombre = input("Ingrese el nombre de la planta que desea buscar: ")

    indice = 0
    for planta in plantas:
        if nombre == planta["nombre_comun"]:
            break
        indice += 1
    planta = plantas[indice]
    print(planta)


#-------------------------------------------------------------------------------
# 4) Actualizar el stock cuando vendo, cuando muere una planta, o cuando se reproduce.
#--------------------------------------------------------------------------------

def mostrar_stock(planta):
    print(" ")
    print(f"NUEVO STOCK de {planta['nombre_comun']} : {planta['cantidad']}")

def actualizar_stock():

    plantas = leer_archivo()
    nombre = input("Para modificar el sstock ingrese el nombre de la planta: ")

    indice = 0
    for planta in plantas:
        if nombre == planta["nombre_comun"]:
            break
        indice += 1
    planta = plantas[indice]

    nombre_comun = planta["nombre_comun"]
    nombre_cientifico = planta["nombre_cientifico"]
    categoria = planta["categoria"]
    sector = planta["sector"]
    cantidad = planta["cantidad"]
    precio = planta["precio"]
    cuidados_basicos = planta["cuidados_basicos"]

    print(' ')
    nuevos_ingresos = ingresar_entero("ingrese cantidad de plantas INGRESADAS(+)/VENDIDAS(-): ")

    cantidad = nuevos_ingresos + cantidad


    planta = {
        "id":indice+1,
        "nombre_comun":nombre_comun,
        "nombre_cientifico":nombre_cientifico,
        "categoria":categoria,
        "sector":sector,
        "cantidad":cantidad,
        "precio":precio,
        "cuidados_basicos":cuidados_basicos
    }
    plantas[indice] = planta
    guardar_archivo(plantas)

    mostrar_stock(planta)


#---------------------------------------------------
# 5) Dar de baja una variedad que ya no vamos a vender.
#---------------------------------------------------


def eliminar_planta():
    plantas = leer_archivo()
    nombre = input("Para dar de baja ingrese el nombre de la planta: ")

    existe = False
    indice = 0

    for planta in plantas:
        if planta["nombre_comun"].lower() == nombre.lower():
            existe = True
            break
        indice += 1


    if existe == False:
        print("❌ No se encontró la planta con ese nombre.")
        return


    confirmar = input(f"¿Está seguro de que desea eliminar {plantas[indice]['nombre_comun']}? (SI/NO): ")

    if confirmar.strip().lower() == "si":
        planta_eliminada = plantas.pop(indice)
        guardar_archivo(plantas)
        print(f"✅ La planta {planta_eliminada['nombre_comun']} se ha eliminado correctamente.")
    else:
        print("❎ Operación cancelada, la planta no fue eliminada.")



#------------------------------------------------
# -----------------MENU-------------------------
#-----------------------------------------------


def mostrar_menu():
    #console.print("═══════════════════════════════════════════════════",style="cervezas")
    print("═══════════════════════════════════════════════════")
    print("🌱 STOCK DE PLANTAS")
    print("═══════════════════════════════════════════════════")
    print(" ")
    print("1 - Cargar una planta nueva")
    print("2 - Ver listado de plantas")
    print("3 - Buscar planta por nombre")
    print("4 - Actualizar stock o precio")
    print("5 - Dar de baja una planta")
    print("0 - Volver a la pantalla principal")
    print(" ")

def menu():
    while True:
        mostrar_menu()

        op = int(input("¿Qué queres hacer? - Ingrese una opcion : "))
        print(" ")

        if op < 0 or op > 5:
            print("Ingrese una opcion valida")
            continue

        match op:
            case 0:
                print(" ") 
                print("----------------------")
                print("Salio del modulo stock")
                print("----------------------")
                break
            case 1:
                cargar_planta()
                continue
            case 2:
                listar_plantas()
                continue
            case 3:
                buscar_planta()
                continue
            case 4:
                actualizar_stock()
                continue
            case 5:
                eliminar_planta()
                continue

if __name__ == '__main__':
    menu()

