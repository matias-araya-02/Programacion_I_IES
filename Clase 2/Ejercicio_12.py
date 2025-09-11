## Ejercicio

#Escribir un programa que almacene las matrices en una tupla y muestre por pantalla su producto.  
#Nota: Para representar matrices mediante tuplas usar tuplas anidadas, representando cada vector fila en una tupla.

def multiplicar_matrices(A, B):
    # Cantidad de filas de A y columnas de B
    filas_A, columnas_A = len(A), len(A[0])
    filas_B, columnas_B = len(B), len(B[0])

    # Validar dimensiones
    if columnas_A != filas_B:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

    # Crear la matriz resultado (como lista de listas)
    resultado = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            # Producto escalar de fila de A con columna de B
            valor = sum(A[i][k] * B[k][j] for k in range(columnas_A))
            fila.append(valor)
        resultado.append(tuple(fila))  # convertir fila en tupla
    return tuple(resultado)  # convertir resultado en tupla de tuplas

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))



C = multiplicar_matrices(a, b)
print("Resultado:")
for fila in C:
    print(fila)