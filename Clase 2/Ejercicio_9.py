
# Ejercicio

#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

# Verificar si una palabra contiene alguna vocal usando una lista
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']

tiene_vocal = False
contador_vocales = 0

for i in vocals:
    if i in word:
        tiene_vocal = True
        contador_vocales+=1
        

if tiene_vocal:
    print("La palabra contiene", contador_vocales,"vocales")
else:
    print("La palabra no contiene ninguna vocal.")