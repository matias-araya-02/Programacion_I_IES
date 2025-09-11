#Funcion Suma 
def suma(num1,num2): 
    return num1+num2

#Funcion Resta
def resta(num1,num2): 
    return num1-num2

#Funcion Multiplicacion
def multiplicacion(num1,num2): 
    return num1*num2

#Funcion def Division(num1,num2): 
def division(num1,num2): 
    return num1/num2

num1 = int(input("Ingrese el primer número: "))

num2 = int(input("Ingrese el segundo número: "))

salir = True

while salir: 

    print("\nIngrese que operacion quiere realizar ")
    print(""" 
    1. Suma 
    2. Resta
    3. Multiplicación
    4. División 
    5. Salir
    """)
    operacion = int(input("-> " ))

    match operacion:
        case 1: 
            print("\nResultado: ",suma(num1,num2))
        case 2: 
            print("\nResultado: ",resta(num1,num2))
        case 3: 
            print("\nResultado: ",multiplicacion(num1,num2))
        case 4: 
            try: 
                print("\nResultado: ",division(num1,num2))
            except ZeroDivisionError: 
                print("No se puede dividir por 0")
        case 5: 
            print("\nSaliendo de la Calculadora")
            salir = False; 
        case _: 
            print("Opcion incorrecta, Intente Nuevamente ")
