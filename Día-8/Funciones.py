def saludar():
    nombre = input("Por favor digita tu nombre: ")
    print(f"Hola {nombre}, ten un buen día")

def suma():
    num1 = int(input("Digite el primer número: "))
    num2 = int(input("Digite el segundo número: "))
    print("La suma de los numeros es:",num1+num2)

def par_impar():
    num = int(input("Por favor digite un número: "))
    if num%2==0:
        print(f"{num} es número par")
    else:
        print(f"{num} es un número impar")