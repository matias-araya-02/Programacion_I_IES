## Ejercicio

#Escribir un programa que guarde en una variable el diccionario `{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}`, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

def busquedaDivisa(diccionario_monedas):
    divisa = str(input("Ingrese alguna divisa: "))

    if divisa in diccionario_monedas: 
        print("La divisa "+divisa+" existe y su valor es "+diccionario_monedas[divisa])
    else: 
        print("La clave "+divisa+" no existe.")


monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

salir = True 

while salir: 
    print(" --- MENU --- ")
    print("1. Buscar una divisa")
    print("2. Salir")
    option = int(input("Ingrese una opción: "))

    match option: 
        case 1: 
            busquedaDivisa(monedas)
        case 2:
            salir=False
        case _:  
            print("Opcion Incorrecta!")
