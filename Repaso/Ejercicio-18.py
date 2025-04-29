numeros = [10,20,30,40,50]
print(numeros)

while True:
    try:
        
        numero = int(input("Número a insertar: "))
        posicion = int(input("En qué posisión (1 a 5): "))-1

        numeros.insert(posicion,numero)
        print("Lista actualizada:",numeros)
        break

    except ValueError:
        print("Debes ingresar un número")
