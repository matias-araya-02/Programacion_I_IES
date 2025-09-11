import random

jugadores = int(input("Ingrese la cantidad de jugadores: "))

lista_jugadores = []
for i in range(jugadores):
    nombre = input(f"Ingrese el nombre del jugador {i+1}: ")
    lista_jugadores.append(nombre)

print("Lista de jugadores:")
for i, nombre in enumerate(lista_jugadores):
    print(f"Jugador {i+1}: {nombre}")

print("Lista de jugadores invertida:")
for i, nombre in enumerate(reversed(lista_jugadores)):
    print(f"Jugador {i+1}: {nombre}")

for i, nombre in enumerate(lista_jugadores): 
    print("Jugador 1 --> ", nombre)
    intentos = 0
    num_aleatorio = random.randint(1,10)
    while intentos < 3:
        numero = int(input("Ingrese un número del 1 al 10: "))
        if numero == num_aleatorio:
            print()
            print("Adivinaste!")
            break
        else:
            print("Perdiste!")
            intentos += 1
            print(f"Intento {intentos} de 3")
    if intentos == 3:
        print(f"No adivinaste el número. Era {num_aleatorio}")
        