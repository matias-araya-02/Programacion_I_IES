## Ejercicio

#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente)
# , donde preferente tendrá el valor `True` si se trata de un cliente preferente. El programa debe preguntar 
# al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,
# (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida 
# el programa tendrá que hacer lo siguiente:

#1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#3. Preguntar por el NIF del cliente y mostrar sus datos.
#4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#6. Terminar el programa.

def agregarCliente (lista_clientes):
	
	nif = int(input("NIF: "))
	nombre = input("Nombre: ")
	direccion = input("Dirección: ")
	telefono = input("Teléfono: ")
	correo = input("Correo: ") 
	preferente = input("¿Es cliente preferente? (s/n): ").lower() == 's'
	lista_clientes[nif] = {
		'nombre': nombre,
		'direccion': direccion,
		'telefono': telefono,
		'correo': correo,
		'preferente': preferente
	}
	print("Cliente añadido correctamente.")

def eliminarCliete (lista_clientes): 
	encontrado = True
	while encontrado: 
		nif = int(input("Ingrese el NIF del cliente a eliminar: "))
		if nif in lista_clientes: 
			del lista_clientes[nif]
			encontrado = False
		else: 
			print("Cliente no encontrado")

def mostrarCliente(lista_clientes):
	encontrado = True
	while encontrado: 
		nif = int(input("Ingrese el NIF del cliente para mostrar sus datos: "))
		if nif in lista_clientes: 
			print(lista_clientes[nif])
			encontrado = False
		else: 
			print("Cliente no encontrado")

def listarClientes(lista_clientes): 
	for i, cliente in enumerate(lista_clientes): 
		print(f'Cliente {i+1}: ', lista_clientes[cliente])
			
def mostrarClientesPreferentes(lista_clientes): 
	for nif, datos in lista_clientes.items():
			if datos['preferente']:
				print(f"NIF: {nif}, Nombre: {datos['nombre']}")

clientes = {}

salir = True

while salir:
	print("\n--- MENÚ ---")
	print("1. Añadir cliente")
	print("2. Eliminar cliente")
	print("3. Mostrar cliente")
	print("4. Listar todos los clientes")
	print("5. Listar clientes preferentes")
	print("6. Terminar")
	opcion = int(input("Opción: "))

	match opcion: 
		case 1: 
			agregarCliente(clientes)
		case 2: 
			eliminarCliete(clientes)
		case 3: 
			mostrarCliente(clientes)
		case 4: 
			listarClientes(clientes)
		case 5: 
			mostrarClientesPreferentes(clientes)
		case 6: 
			print("Saliendo...")
			salir = False
		case _:
			print("Opcion Incorrecta!")

