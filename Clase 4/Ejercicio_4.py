def aplicarIVA(precio_producto): 

   IVA = 0.21 
   suma_iva = (precio_producto * IVA)
   precio_final = precio_producto + suma_iva

   print("Precio Original: ", precio_producto)
   print("El precio final con iva es: ", precio_final)


print("--- CALCULADORA IVA ---")
precio_producto = float(input("Ingrese el precio: "))
aplicarIVA(precio_producto)