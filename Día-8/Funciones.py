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

def mayor_de_lista():
    while True:
        entrada_numeros = input("Por favor ingrese los números separados por comas: ")
        try:
            lista_entrada = entrada_numeros.split(",")
            lista_numeros = [float(x.strip()) for x in lista_entrada]
            break
        except ValueError:
            print("Deben de ser valores numéricos")
    lista_numeros.sort()
    numero_mayor = lista_numeros[-1]
    print(f"El número mayor es {numero_mayor}")

def cantidad_apariciones():
    texto = input("Escribe el texto a evaluar: ").lower()
    caracter = input("Escribe el caracter a contar: ")
    print(f'"{caracter}" se repite {texto.count(caracter)} veces.')

def filtrar_pares():
    while True:
        entrada_numeros = input("Por favor ingrese los números separados por comas: ")
        try:
            lista_entrada = entrada_numeros.split(",")
            lista_numeros = [int(x.strip()) for x in lista_entrada]
            break
        except ValueError:
            print("Deben de ser valores numéricos")
    lista_pares = []
    for num in lista_numeros:
        if num % 2 == 0:
            lista_pares.append(num)
    print(f"Los numeros pares son: {lista_pares}")

def es_palindromo():
    texto = input("Escribe algo: ").lower()
    texto_invertido = texto[::-1]
    if texto == texto_invertido:
        print(f"{texto.capitalize()} es palíndromo.")
    else:
        print(f"{texto} no es palíndromo.")

def factorial():
    while True:
        try:
            num = int(input("Digite un número para hallar su factorial: "))
            factorial = 1
            for i in range(1,num+1):
                factorial *= i
            print(factorial)
        except ValueError:
            print("Debe ingresar un número entero")

def eliminar_duplicados():
    entrada = input("Por favor ingrese los elementos separados por comas: ")
    lista = entrada.split(",")
    lista_unicos = set(lista)
    print(f"Lista sin repetir elementos: {lista_unicos}")

def FizzBuzz():
    while True:
        try:
            num = int(input("Por favor escribe un número entero: "))
            break
        except ValueError:
            print("Entrada inválida")
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print("...")
        
def contar_vocales():
    texto = input("Escribe el texto a evaluar: ").lower()
    vocales = "aeiou"
    contador = 0
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    print(f"El número de vocales que hay es: {contador}")

def texto_invertido():
    texto = input("Escribe el texto a evaluar: ")
    print(texto[::-1])

def contrasena_segura():
    validacion = True
    mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    minus = "abcdefghijklmnñopqrstuvwxyz"
    numeros = "1234567890"
    especiales = "!@#$%^&*()_+=-[]{};':\",./<>?\\|~`"
    contrasena = input("Escribe el texto a evaluar: ")
    if len(contrasena) < 8:
        validacion = False
    for caracter in contrasena:
        contador = 0
        if caracter in mayus:
            contador += 1
    if contador == 0:
        validacion = False
    for caracter in contrasena:
        contador = 0
        if caracter in minus:
            contador += 1
    if contador == 0:
        validacion = False
    for caracter in contrasena:
        contador = 0
        if caracter in numeros:
            contador += 1
    if contador == 0:
        validacion = False
    for caracter in contrasena:
        contador = 0
        if caracter in especiales:
            contador += 1
    if contador == 0:
        validacion = False
    if validacion:
        print("La contraseña es válida")
    else:
        print("La contraseña es inválida")

