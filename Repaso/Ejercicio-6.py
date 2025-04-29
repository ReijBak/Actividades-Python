while True:
    try:
        hora = int(input("Por favor dame la hora (formato 24h y sin minutos): "))      

        if hora<0 or hora>23:
            print("El valor debe ser mayor o igual a 0 y menor a 24")
            continue
        
        if 12<hora<18:
            print("Es hora de trabajar")
            break
        else:
            print("No es hora de trabajar")
            break
    
    except ValueError:
        print("Debes ingresar un valor numérico")
