casco = bool(input("¿Tiene casco?(1=si 0=no): "))
licencia = bool(input("Tiene casco?(1=si 0=no): "))
if casco == 1 or licencia == 1:
    print("Puede conducir")
else:
    print("No puede conducir")