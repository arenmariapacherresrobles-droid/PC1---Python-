import math

# pedimos los coeficientes 
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# calculamos la discriminante
D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"La ecuación tiene dos soluciones reales: x1 = {x1}, x2 = {x2}")

elif D == 0:
    X = -b / (2*a)
    print(f"La ecuación tiene una única solución real: x = {X}")

else:
    print("La ecuación no tiene solución real")
