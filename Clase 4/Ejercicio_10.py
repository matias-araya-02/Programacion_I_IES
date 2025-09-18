def decimalAbinario (num): 
    binario = bin(num)[2:]
    print("Decimal: ", num)
    print("Binario: ", binario)
    
def binarioAdecimal (num): 
    decimal = int(num, 2)
    print("Binario: ",num)
    print("Decimal: ", decimal)

salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Decimal a Binario")
    print("2. Binario a Decimal")
    print("3. Salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            num = int(input("Ingrese un numero entero: "))
            decimalAbinario(num)
        case 2: 
            num = str(input("Ingrese un numero binario: "))
            binarioAdecimal(num)
        case 3: 
            salir = False 
        case _:
            print("Opcion Incorrecta!")