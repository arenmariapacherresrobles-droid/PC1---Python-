#ingresamos los datos 
capital= float(input("ingresa el capital incial"))
#tasa de interes
r =4
#calculamos el capital para cada año usando la formula 
for t in range(1, 4):
 capital_final = capital * (1 + r/100)**t
 print(f"año : {t}: {round(capital_final , 2)}")