while True:
    try:
        temperatura = float(input("Por favor dame la temperatura: "))      
        
        if temperatura >= 0:
            print("No hace frío")
            break
        else:
            print("Hace frío")
            break
    
    except ValueError:
        print("Debes ingresar un valor numérico")
