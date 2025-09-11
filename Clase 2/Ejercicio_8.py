# Ejercicio

# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un ACpalíndromo.

def es_palindromo(palabra) -> bool: 
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]
    

palabra = str(input("Ingrese una palabra: "))

resultado = es_palindromo(palabra) 

if resultado:  
    print("Es Palíndromo")
else: 
    print("No es Palíndromo")