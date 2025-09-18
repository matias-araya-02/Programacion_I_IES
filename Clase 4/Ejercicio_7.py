lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def lista_cuadrado(lista_numeros):
    lista_nueva = []

    for i in lista_numeros:
        lista_nueva.append(pow(i,2))
    
    print(lista_nueva)

lista_cuadrado(lista_numeros)