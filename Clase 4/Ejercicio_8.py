import math

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def media(lista_numeros): 
    media = sum(lista_numeros) / len(lista_numeros)
    return media

def varianza(lista_numero, media): 
    varianza = sum((x - media) ** 2 for x in lista_numero) / len(lista_numero)
    return varianza

def desviacion_estandar(varianza): 
    resultado_desviacion_estandar = math.sqrt(varianza)
    return resultado_desviacion_estandar

def conversionDiccionario(lista_numeros, media, varianza, desviacion_estandar):
    diccionario = {
    "Lista: ":lista_numeros,
    "Media: ":media,
    "Varianza: ": varianza,
    "Desviacion Estandar: ": desviacion_estandar
    }
    return diccionario


media = media(lista_numeros)
print(media)
varianza = varianza(lista_numeros,media)
print(varianza)
desviacion_estandar = desviacion_estandar(varianza)
print(desviacion_estandar)
diccionario = conversionDiccionario(lista_numeros, media, varianza, desviacion_estandar)
print(diccionario)