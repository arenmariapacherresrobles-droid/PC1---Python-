consumo = float (input ("¿cuanto fue su consumo ?"))
porcentaje = float( input("¿que porcentaje de propina quiere dejar?"))
propina = consumo * (porcentaje/100)
print(f"la propina es de: ${propina:.2f}")