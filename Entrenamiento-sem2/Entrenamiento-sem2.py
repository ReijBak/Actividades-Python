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
#       -Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
#       -Calcular y mostrar el promedio de las calificaciones en la lista
#
# ======================================//======================================

notas = []
continuar=True

def agregar_nota():

        
        try:
            nota = float(input("Digite la nota a agregar (0-100): "))
            if nota<0 or nota>100:
                print("Valor fuera de rango, intente de nuevo")  

            if nota>=70:
                print("Aprobó")
            else:
                print("reprobó")
                
        except ValueError:
            print("Valor inválido, intente de nuevo")
    
    
        
        guardar_nota = input("¿Desea guardar la nota en la lista?(Si/No)\n").lower()

        if guardar_nota=="si" or guardar_nota=="sí":
            notas.append(nota)
            print("La nota ha sido agregada")
        
        elif guardar_nota=="no":
            print("La nota no ha sido agregada")
        else:
            print("Opción no válida, intente de nuevo")
        
def consultar_nota():

    for i in range(len(notas)):
        print(f"las nota {i+1}. es  {notas[i]}")

def calcular_promedio():

    suma = sum(notas)
    if suma == 0:
        print("El promedio de las notas es: 0")
    else:
        promedio = suma / len(notas)
        print("El promedio de las notas es:",promedio)

def comparar_notas():

    

def main():       

    while True:

        print(" ======================================//====================================== \n")
        print("¡Bienvenido!\n")
        print("\nSeleccione una de las siguientes opciones:\n")
        print("1. Agregar una nota.\n2. Calcular promedio de notas.")
        print("3. Comparar notas según una nota de referencia.\n4. Consultar la existencia de una nota.")
        print("5. Salir\n")

        opcion = int(input("Por favor digite la opción que desea elegir aquí: ---> "))

        if opcion==1:
            continuar=True
            while continuar:
                print("Has elegido: Agregar una nota.")
                agregar_nota()
                opc=input("Desea seguir agregando notas si/no: ?")
                if opc=="no" or opc=="n":
                    continuar=False
        elif opcion==2:
            print("Has elegido: Calcular promedio de notas.")
            calcular_promedio()
        elif opcion==3:
            print("Has elegido: Comparar notas según una nota de referencia.")
            comparar_notas()
        elif opcion==4:
            print("Has elegido: Consultar la existencia de una nota")
            consultar_nota()
        elif opcion==5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente")



if __name__ == '__main__':
    main()
