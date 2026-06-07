import os
import json

NOMBRE_ARCHIVO = os.path.join('datos', 'plantas.json')

SECTOR_INTERIOR = 'Interior'
SECTOR_EXTERIOR = 'Exterior'
SECTOR_INVERNADERO = 'Invernadero'
SECTOR_HUERTA = 'Huerta'

def menu():
    while True:
        print("0- SALIR")
        print("1- ALTA")
        print("2- MODIFICACION")
        print("3- ELIMINAR")
        print("4- BUSCAR")

        op = int(input("Ingrese una opción: "))

        if op < 0 or op > 5:
            print("Ingrese una opcion valida")
            continue

        match op:
            case 0: 
                print("Salio del modulo stock")
                break
            case 1:
                crear_planta()
                continue
            case 2:
                modificar_planta()
                continue
            case 3:
                baja_planta()
                continue
            case 4:
                listar_plantas()
                continue
            case 5:
                filtrar()
                continue

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
    while not a_retornar.isnumeric:
        print("El valor debe ser numerico")
        a_retornar = input(msj)
    return int(a_retornar)

def ingresar_float(msj:str)->float:
    a_retornar = input(msj)
    while not a_retornar.isnumeric:
        print("El valor debe ser numerico")
        a_retornar = input(msj)
    return float(a_retornar)


def listar_plantas():
    plantas = leer_archivo()
    for planta in plantas:
        print(planta)

def crear_planta():
    plantas = leer_archivo()
    nombre_comun = input("ingrese nombre comun de la planta: ")
    nombre_cientifico = input("ingrese nombre cientifico de la planta: ")
    categoria = input("ingrese categoria de la planta: ")
    sector = input("ingrese sector donde esta la planta: ")
    cantidad = ingresar_entero("ingrese nuevo tock de la planta: ")
    precio = ingresar_float("ingrese el precio unitario: ")
    cuidados_basicos = input("ingrese cuaidados basicos de la planta: ")

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

def baja_planta():
    plantas = leer_archivo()
    nombre = input("Para dar de baja ingrese el nombre: ")

    indice = 0
    for planta in plantas:
        if nombre == planta["nombre_comun"]:
            break
        indice += 1
    #POP para eliminar el item de la lista
    plantas.pop(indice)
    guardar_archivo(plantas)

def modificar_planta():
    plantas = leer_archivo()
    nombre = input("Para modificar ingrese el nombre: ")

    indice = 0
    for planta in plantas:
        if nombre == planta["nombre_comun"]:
            break
        indice += 1
    planta = plantas[indice]

    nombre_comun = input("ingrese nombre comun de la planta: ")
    nombre_cientifico = input("ingrese nombre cientifico de la planta: ")
    categoria = input("ingrese categoria de la planta: ")
    sector = input("ingrese sector donde esta la planta: ")
    cantidad = ingresar_entero("ingrese nuevo tock de la planta: ")
    precio = ingresar_float("ingrese el precio unitario: ")
    cuidados_basicos = input("ingrese cuaidados basicos de la planta: ")


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


def filtrar():
        pass

menu()



'''Guardar: -Un código interno (único, no se repite). -Nombre común (ej: "lavanda").
    -Nombre científico (ej: "Lavandula angustifolia").
    -Categoría (árbol, arbusto, suculenta, aromática, frutal, ornamental, otro).
    -Sector donde está (interior, exterior, invernadero, huerta).
    -Cantidad en stock.
    -Precio unitario.
    -Cuidados básicos (un breve texto: "sol pleno, riego moderado").'''

'''filtrar por sector (interior, exterior, invernadero, huerta) o por
categoría (árboles, arbustos, suculentas, aromáticas, frutales, ornamentales).'''

#buscar una planta por nombre común o por nombre científico.
#Actualizar el stock cuando vendo, cuando muere una planta, o cuando se reproduce.
#Dar de baja una variedad que ya no vamos a vender.