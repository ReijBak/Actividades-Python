while True:
    try:
        num1 = float(input("Por favor dame un número: "))      
        num2 = float(input("Por favor dame otro número: "))

        if num1 >= 0 and num2 >= 0:
            print("Ambos son positivos")
            break
        else:
            print("No son positivos")
            break
    
    except ValueError:
        print("Debes ingresar un valor numérico")
