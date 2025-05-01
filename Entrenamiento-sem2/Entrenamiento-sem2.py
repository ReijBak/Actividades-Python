#
#   Determinar el estado de aprobación:
#       -Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
#       -Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
#   Calcular el promedio:
#       -Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#       -Calcular y mostrar el promedio de las calificaciones en la lista
#   Contar calificaciones mayores:
#       -Preguntar al usuario por un valor específico
#       -Contar cuántas calificaciones en la lista son mayores que este valor
#   Verificar y contar calificaciones específicas:
#       -Preguntar al usuario por una calificación específica. 
#       -Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa. 
#
# ======================================//======================================

notas = []
continuar=True

def agregar_nota():

    while True:

        try:
            
            nota = float(input("Digite la nota a agregar (0-100): "))
            if nota<0 or nota>100:
                print("Valor fuera de rango, intente de nuevo")  
                continue
            if nota>=70:
                print("Aprobó")
                break
            else:
                print("reprobó")
                break
        except ValueError:
            print("Valor inválido, intente de nuevo")
    
    guardar_nota = input("¿Desea guardar la nota en la lista?(S/N)\n").lower()
    
    if guardar_nota=="s":
        notas.append(nota)
        print("La nota ha sido agregada")
    
    elif guardar_nota=="n":
        print("La nota no ha sido agregada")
    else:
        print("Opción no válida, intente de nuevo")
        
def calcular_promedio():

    print("1. Promedio de las notas guardadas.\n2. Importar lista para promediar.")
    opcion_menu2 = int(input("Por favor digite la opción que desea elegir aquí: ---> "))

    if opcion_menu2==1:

        promedio(notas)

    elif opcion_menu2==2:

        while True:
            entrada_notas = input("Por favor ingrese las notas separadas por comas:\n")

            try:
                user_notas_string = entrada_notas.split(",")
                user_notas_float = [float(x.strip()) for x in user_notas_string]

                if any(nota < 0 or nota > 100 for nota in user_notas_float):
                            print("Error: Todas las notas deben estar entre 0 y 100.")
                            continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar solo números válidos, separados por comas.")

        promedio(user_notas_float)

def promedio(notas):
    suma = sum(notas)
    if suma == 0:
        print("No hay notas para promediar")
    else:
        promedio = suma / len(notas)
        print("El promedio de las notas es:",promedio)

        
        

def comparar_notas():
    nota_referencia = float(input("Por favor ingrese la nota que desea comparar: "))

    notas_mayores = [nota for nota in notas if nota > nota_referencia]
    notas_menores = [nota for nota in notas if nota < nota_referencia]
    notas_iguales = [nota for nota in notas if nota == nota_referencia]

    cantidad_mayores = len(notas_mayores)
    cantidad_menores = len(notas_menores)
    cantidad_iguales = len(notas_iguales)

    print(f"La cantidad de notas mayores que {nota_referencia} son {cantidad_mayores}")
    print(f"La cantidad de notas menores que {nota_referencia} son {cantidad_menores}")
    print(f"La cantidad de notas iguales a {nota_referencia} son {cantidad_iguales}")

    print(f"Notas mayores: {notas_mayores}")
    print(f"Notas menores: {notas_menores}")

def consultar_nota():

    for i in range(len(notas)):
        print(f"La nota {i+1}. es  {notas[i]}")

def main():       

    while True:

        print(" ======================================//====================================== \n")
        print("¡Bienvenido!\n")
        print("\nSeleccione una de las siguientes opciones:\n")
        print("1. Agregar una nota.\n2. Calcular promedio de notas.")
        print("3. Comparar notas según una nota de referencia.\n4. Consultar la existencia de una nota.")
        print("5. Salir\n")

        opcion_menu1 = int(input("Por favor digite la opción que desea elegir aquí: ---> "))

        if opcion_menu1==1:
            continuar=True
            
            while continuar:
                print("Has elegido: Agregar una nota.")
                agregar_nota()
                
                opcion1=input("¿Desea seguir agregando notas?(S/N)").lower()
                if opcion1=="n":
                    continuar=False

        elif opcion_menu1==2:
            print("Has elegido: Calcular promedio de notas.")
            calcular_promedio()

        elif opcion_menu1==3:
            print("Has elegido: Comparar notas según una nota de referencia.")
            comparar_notas()

        elif opcion_menu1==4:
            print("Has elegido: Consultar la existencia de una nota")
            consultar_nota()

        elif opcion_menu1==5:
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intente nuevamente")

if __name__ == '__main__':
    main()
