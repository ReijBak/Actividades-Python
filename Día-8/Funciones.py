def saludar():
    nombre = input("Por favor digita tu nombre: ")
    print(f"Hola {nombre}, ten un buen día")

def suma():
    num1 = int(input("Digite el primer número: "))
    num2 = int(input("Digite el segundo número: "))
    print("La suma de los numeros es:",num1+num2)

def par_impar():
    num = int(input("Por favor digite un número: "))
    if num % 2 == 0:
        print(f"{num} es número par")
    else:
        print(f"{num} es un número impar")

def mayoria_edad():
    while True:
        edad = int(input("Por favor digita tu edad: "))
        if edad < 0 or edad > 120:
            print("Edad inválida, intente de nuevo")
            continue
        elif edad >= 18:
            print("Eres mayor de edad")
            break
        else:
            print("Eres menor de edad")
            break 
    
def Celsius_a_Farenheit():
    celsius = float(input("Por favor escribe la temperatura en °C: "))
    farenheit = celsius * 1.8 + 32
    print(f"{celsius}°C son equivalentes a {farenheit:.2f}°F")

def area_triangulo():
    base = float(input("Por favor digite la base del triángulo: "))
    altura = float(input("Por favor digite la altura del triángulo: "))
    print(f"El área del triángulo es {base * altura / 2:.2f}")

def lista_numerica():
    while True:
        try:
            entrada_numeros = input("Por favor ingrese los números separados por comas: ")
            lista_entrada = entrada_numeros.split(",")
            lista_numeros = [float(x.strip()) for x in lista_entrada]
            break
        except ValueError:
            print("Deben de ser valores numéricos")
    mayor_de_lista(lista_numeros)

def mayor_de_lista(lista):
    lista = lista.sort()
    print(f"El número mayor de la lista es {lista[-1]}")

