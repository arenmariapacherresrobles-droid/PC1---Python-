# ingresamos los datos 
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# mostramos las opciones
print("Elige una de las siguientes opciones: ")
print("1. Sumar")
print("2. Restar (numero1 - numero2)")
print("3. Multiplicar")

opcion = int(input("Opción: "))

# condicionales 
if opcion == 1:
    print(f"La suma es: {numero1 + numero2}")
elif opcion == 2:
    print(f"La resta es: {numero1 - numero2}")
elif opcion == 3:
    print(f"El producto es: {numero1 * numero2}")
else:
    print("Opción inválida")





