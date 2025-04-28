edad = float(input("Escribe la edad: "))
if 0< edad <12:
    print("Niño")
elif 12<= edad <18:
    print("Adolescente")
elif 18<= edad <60:
    print("Adulto")
elif edad <60:
    print("Anciano")
else:
    print("Edad inválida")
