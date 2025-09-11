## Ejercicio

#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# y cada par `<palabra>:<traducción>` separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español 
# y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

def agregarPalabras(lista_palabras): 
    palabra = str(input("Ingrese la palabra: "))
    pares = palabra.split(',')
    for i in pares: 
        if ':' in i: 
            clave, valor = i.split(':')
            lista_palabras[clave.strip()] = valor.strip() 

    print(lista_palabras)

def mostrarTraduccion(lista_palabras): 
    frase = input("Ingrese una frase en español: ")
    palabras = frase.split()
    traduccion = []
    for palabra in palabras:
        traduccion.append(lista_palabras.get(palabra, palabra))
    print("Frase traducida:", ' '.join(traduccion))
    


traductor = {}

salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Agregar palabras al traductor")
    print("2. Traducir y salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            agregarPalabras(traductor)
        case 2: 
            mostrarTraduccion(traductor)
            salir = False; 
        case _:
            print("Opcion Incorrecta!")