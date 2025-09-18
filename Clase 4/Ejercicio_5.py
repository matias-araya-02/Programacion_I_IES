import math

def areaCirculo(radio,PI) -> float:
    area =  PI * pow(radio,2)
    return area

def volumenCilindro(resultado_area, altura): 
    volumen = resultado_area * altura

    print("El volumen del cilindro es ", volumen)

PI = math.pi

radio = float(input("Ingrese el radio del circulo: "))
resultado_area = areaCirculo(radio,PI)
print(resultado_area)

altura = float(input("Ingrese la altura: "))
volumenCilindro(resultado_area, altura)