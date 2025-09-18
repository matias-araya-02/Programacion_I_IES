
from deep_translator import GoogleTranslator


def traductorIngles(frase):
    return GoogleTranslator(source='auto', target='en').translate(frase)

cadena = str(input("Ingrese una palabra o frase para traducir: "))
traduccion = traductorIngles(cadena)
print(traduccion)