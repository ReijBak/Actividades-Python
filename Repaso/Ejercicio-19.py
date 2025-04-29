pares = []

for i in range(5):
    while True:
        try:
            numero = int(input(f"Ingres el número {i+1}: "))
            if numero % 2 == 0:
                pares.append(numero)
            break

        except ValueError:
            print("Debes ingresar un valor numérico")
        
print("Números pares ingresados:",pares)