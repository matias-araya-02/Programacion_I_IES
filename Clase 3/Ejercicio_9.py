## Ejercicio

#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.


def agregarFactura (factura): 

    numero_factura = int(input("Ingrese el numero de la factura: "))
    porte_factura = float(input("Ingrese su valor: "))

    factura[numero_factura] = porte_factura

    print(factura)

def pagarFactura (factura): 

    monto_factura = 0
    numero_factura = int(input("Ingrese el numero de la factura: "))
    
    if numero_factura in factura: 
        print("Factura pagada exitosamente")
        monto_factura = factura[numero_factura] 
        del factura[numero_factura] 
    else: 
        print("Factura inexistente, intente nuevamente")

    return monto_factura

facturas = {}
total_facturas_pagadas = 0
salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Añadir nueva factura")
    print("2. Pagar factura")
    print("3. Salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            agregarFactura(facturas)
        case 2: 
            monto_factura = pagarFactura(facturas)
            total_facturas_pagadas += monto_factura
            print("Cantidad cobrada hasta el momento: ", total_facturas_pagadas)
            print("Cantidad pendiente: ", sum(facturas.values()))
        case 3: 
            salir = False; 
        case _:
            print("Opcion Incorrecta!")