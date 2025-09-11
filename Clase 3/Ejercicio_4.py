## Ejercicio

#Escribir un programa que pregunte una fecha en formato `dd/mm/aaaa` 
# y muestre por pantalla la misma fecha en formato `dd de <mes> de aaaa` donde `<mes>` 
# es el nombre del mes.

meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

salir = True

print(" --- FECHA ACTUAL --- ")
dia = int(input("Ingrese el día: "))
while salir: 
    mes = int(input("Ingrese el mes en numero: "))
    if mes in meses: 
        salir = False
    else: 
        print("Ea mes no existe")
ano = int(input("Ingrese el año: ")) 

print(dia," de ",meses[mes]," de ",ano)