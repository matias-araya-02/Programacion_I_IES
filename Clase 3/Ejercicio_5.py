## Ejercicio

#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso `{'Matemáticas': 6, 'Física': 4, 'Química': 5}` y después muestre por pantalla los créditos de cada asignatura en el formato `<asignatura> tiene <créditos> créditos`, donde `<asignatura>` es cada una de las asignaturas del curso, y `<créditos>` son sus créditos. Al final debe mostrar también el número total de créditos del curso.

def mostrarAsignaturas(lista_asignaturas): 

    for i, asignatura in enumerate(lista_asignaturas): 
        print(f'Materia {i+1}: ', 'La asignatura ',asignatura, ' tiene ', lista_asignaturas[asignatura], ' creditos')


def sumaTotalCreditos(lista_asignaturas): 
    suma_total_creditos = 0; 

    for i, asignatura in enumerate(lista_asignaturas): 
        suma_total_creditos += lista_asignaturas[asignatura]

    return suma_total_creditos


curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

salir = True

while salir: 

    print(" --- MENU --- ")
    print("1. Mostrar Asignaturas")
    print("2. Mostrar Numero total de Creditos")
    print("3. Salir")
    opcion = int(input("Opcion: "))

    match opcion: 
        case 1: 
            mostrarAsignaturas(curso)
        case 2: 
            resultado = sumaTotalCreditos(curso)
            print("La suma total de los creditos es: ", resultado)
        case 3: 
            salir = False; 
        case _:
            print("Opcion Incorrecta!")