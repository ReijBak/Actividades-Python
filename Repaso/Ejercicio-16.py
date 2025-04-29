numeros = [33,14,37,7,4]
while True:
    try:
        buscado = int(input("Ingresa el número que deseas buscar: "))

        if buscado in numeros:
            posicion = numeros.index(buscado)
            print(f"El número {buscado} está en la posición {posicion}.")
            break
        else:
            print(f"El número {buscado} no está en la lista")
            break

    except ValueError:
        print("Debe ser un valor numérico")
