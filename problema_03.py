#ingresamos los datos 
payasos =  int(input("ingrese número de payasos vendidos: "))
muñecas = int(input("ingrese número de muñecas vendidas: 3"))
#calculamos el peso
peso = (payasos*112 ) + (muñecas*75)
print(f"el peso total del paquete es: {peso:.2f} g")