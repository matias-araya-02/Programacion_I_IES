# Función que recibe una cadena y devuelve un diccionario con la frecuencia de cada palabra
def contar_palabras(cadena):
	palabras = cadena.split()
	frecuencias = {}
	for palabra in palabras:
		if palabra in frecuencias:
			frecuencias[palabra] += 1
		else:
			frecuencias[palabra] = 1
	return frecuencias

# Función que recibe el diccionario y devuelve la palabra más repetida y su frecuencia
def palabra_mas_repetida(diccionario):
	if not diccionario:
		return None, 0
	palabra = max(diccionario, key=diccionario.get)
	return palabra, diccionario[palabra]

# Ejemplo de uso
if __name__ == "__main__":
	texto = input("Ingrese una cadena de texto: ")
	frecuencias = contar_palabras(texto)
	print("Frecuencias:", frecuencias)
	palabra, frecuencia = palabra_mas_repetida(frecuencias)
	print(f"La palabra más repetida es '{palabra}' y aparece {frecuencia} veces.")
