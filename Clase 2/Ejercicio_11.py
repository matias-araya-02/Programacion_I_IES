# Ejercicio

#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.

a = (1, 2, 3)
b = (-1, 0, 2)

producto_escalar = 0

for i, x in zip(a, b): 
    producto_escalar += i * x

print("El producto escalar es:", producto_escalar)