while True:
    
    try:
        edad = float(input("Escribe la edad: "))
        
        if edad < 0 or edad > 120:
            print("El valor no está en el rango de edad")
            continue

        if 0< edad <12:
            print("Niño")
            break
        elif 12<= edad <18:
            print("Adolescente")
            break
        elif 18<=edad <60 :
            print("Adulto")
            break
        elif edad >= 60:
            print("Anciano")
            break
    
    except ValueError:
        print("Debes ingresar un valor numérico")
