while True:
    try:
        edad = int(input("Por favor dame tu edad: "))
        
        if edad <= 0 or edad >= 120:
            print("La edad debe estar entre 0 y 120.")
            continue
        
        if edad >= 18:
            print("Puede votar")
            break
        else:
            print("No puede votar")
            break
    
    except ValueError:
        print("Debes ingresar un valor numérico")
