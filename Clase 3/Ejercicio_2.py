## Ejercicio

#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Despúes debe mostrar por pantalla el mensaje `<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>`.

def rellenarDiccionario(datosUsuario): 

    clave = str(input("Ingrese la clave: "))
    valor = input("Ingrese el valor: ")

    datosUsuario[clave] = valor

def verDiccionario(datosUsuario): 
    print(datosUsuario)

datos_usuario = {}

salir = True 

while salir: 
    print(" --- MENU --- ")
    print("1. Rellenar diccionario")
    print("2. Ver todos los datos usuario")
    print("2. Salir")
    option = int(input("Ingrese una opción: "))

    match option: 
        case 1: 
            rellenarDiccionario(datos_usuario)
        case 2:
            verDiccionario(datos_usuario)
        case 3: 
            salir=False
        case _:  
            print("Opcion Incorrecta!")