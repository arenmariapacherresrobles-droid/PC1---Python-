# Ingresamos la hora 
time = input("Ingrese la hora en formato hh:mm: ")

# Separamos horas y minutos 
hours, minutes = time.split(":")
hours = int(hours)
minutes = int(minutes)

# Convertimos hora en decimal 
hora_decimal = hours + minutes / 60

# Condicionales 
if 7 <= hora_decimal <= 8:
    print("Es hora de desayunar")
elif 12 <= hora_decimal <= 13:
    print("Es hora de almorzar")
elif 18 <= hora_decimal <= 19:
    print("Es hora de cenar")