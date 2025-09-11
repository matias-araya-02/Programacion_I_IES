# Ejercicio

#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una tupla y muestre por pantalla su media y desviación típica.
import math

def agregar_numero_tupla(tupla_numeros, numeros):
    numeros = tuple(float(n) for n in numeros)
    return tupla_numeros + numeros

def media(tupla_numeros): 
    media = sum(tupla_numeros) / len(tupla_numeros)
    return media

def desviacion_estandar(tupla_numeros, media): 
    varianza = sum((x - media) ** 2 for x in tupla_numeros) / len(tupla_numeros)
    resultado_desviacion_estandar = math.sqrt(varianza)
    return resultado_desviacion_estandar

tupla_numeros = ()

salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Ingresar numero para la tupla")
    print("2. Media")
    print("3. Desviación estándar")
    print("4. Salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            numeros = input("Ingrese el/los número(s) separados por coma: ").split(',')
            tupla_numeros = agregar_numero_tupla(tupla_numeros, numeros)
            print(tupla_numeros)
        case 2: 
            print("La media es: ", media(tupla_numeros))

        case 3: 
            m = media(tupla_numeros)
            print("La desviación estándar es:", desviacion_estandar(tupla_numeros, m))
            
        case 4: 
            salir = False; 
        case _:
            print("Opcion Incorrecta!")


