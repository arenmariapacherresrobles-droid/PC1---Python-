#Ingresamos datos 
edad = int(input("Ingrese su edad: "))
#condicionales 
#primera condicion: si es menos de 4 años
if edad < 4:
    print("Entrada gratis")
#segunda condicion: si tiene entre 4 y 18 años 
elif 4 <= edad <= 18:
    print("El costo de su entrada es $5")
#si es mayor de 18 años
else: 
    print("El costo de su entrada es $10")