# Ejercicio
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

def numeros_ganadores(num): 
    lista_numeros.append(num)
    lista_numeros.sort()

lista_numeros = []

salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Ingresar numero ganador")
    print("2. Salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            numero_ganador = int(input("Ingrese el número: "))
            numeros_ganadores(numero_ganador)
        case 2: 
            salir = False; 
        case _:
            print("Opcion Incorrecta!")


print(lista_numeros)
