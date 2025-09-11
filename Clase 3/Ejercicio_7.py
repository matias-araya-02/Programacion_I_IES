## Ejercicio

#Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario 
# decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

def carritoCompras (lista_carrito):

    producto = str(input("Ingrese el producto: "))
    valor = float(input("Ingrese el valor de "+ producto+":"))

    lista_carrito[producto] = valor


def sumaCarrito(lista_carrito): 

    sumaTotal = 0

    for i, producto in enumerate(lista_carrito): 
        sumaTotal += lista_carrito[producto]


    print(" --- CARRITO --- ")

    for i, producto in enumerate(lista_carrito): 
        print(f"Articulo "+producto+": ",lista_carrito[producto])

    print("Total: ", sumaTotal)

carrito = {}

salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Agregar Producto")
    print("2. Salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            carritoCompras(carrito)
        case 2: 
            sumaCarrito(carrito)
            salir = False; 
        case _:
            print("Opcion Incorrecta!")