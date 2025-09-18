import math 

def maximoComunDivisor(num1, num2):
    mcd = math.gcd(num1, num2) 
    return mcd

def minimoComunDivisor(num1, num2, mcd): 
    mcm = abs(num1 * num2) // mcd
    return mcm


num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
mcd = maximoComunDivisor(num1,num2)
print("Maximo comun Divisor: ", mcd)
mcm = minimoComunDivisor(num1, num2, mcd)
print("Minimo comun divisor: ", mcm)