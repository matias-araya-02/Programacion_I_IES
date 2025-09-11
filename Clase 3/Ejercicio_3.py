# Ejercicio

#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
def cargarValoresFruta(frutas): 
    fruta = str(input("Ingrese la fruta a la que quiere modificar su precio: "))
    salir = True

    while salir: 
        if fruta in frutas: 
            nuevo_precio = int(input("Ingrese el nuevo valor: "))
            frutas[fruta] = nuevo_precio
            salir = False
        else: 
            print("La fruta no existe intente nuevamente")


def verPreciosFrutas(frutas): 
    fruta = str(input("Ingrese la fruta que desea saber su precio: "))
    salir = True

    while salir: 
        if fruta in frutas:
            print("El precio de ",fruta," es ",frutas[fruta])
            salir = False
        else: 
            print("La fruta no existe intente nuevamente")

    print("Lista de precios de frutas")        
    print(frutas)



frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}

salir = True 

while salir: 
    print(" --- MENU --- ")
    print("1. Cargar valores de frutas")
    print("2. Ver precio de frutas")
    print("2. Salir")
    option = int(input("Ingrese una opción: "))

    match option: 
        case 1: 
            cargarValoresFruta(frutas)
        case 2:
            verPreciosFrutas(frutas)
        case 3: 
            salir=False
        case _:  
            print("Opcion Incorrecta!")