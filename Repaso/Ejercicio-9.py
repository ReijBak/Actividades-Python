while True:
    
    try:
        nota = float(input("Escribe la nota (0 a 10): "))

        if nota < 0 or nota > 10:
            print("Debes ingresar una nota válida")
            continue

        if 5> nota:
            print("Perdió")
            break
        elif 5<= nota <7:
            print("Aprobó")
            break
        else:
            print("Sobresaliente")
            break
    except ValueError:
        print("Debes ingresar un valor numérico")
