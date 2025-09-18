def factorial (num):
    fac = 1
    for i in range(1, num + 1): 
        fac *= i

    #Forma mas corta 
    #fac = math.factorial(num)

    return fac

num = int(input("Ingrese un numero: "))
resultado = factorial(num)
print("El factorial de", num,"es", resultado)