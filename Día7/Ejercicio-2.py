#   Actividad: Cajero automático simplificado
  
#   Descripción del problema:
#   Vas a simular un cajero automático. El sistema debe permitir al usuario:
#   - Ver el saldo de su cuenta.
#   - Retirar dinero.
#   - Depositar dinero.
#   - Ver el historial de movimientos.
#   - Salir del programa.

saldo = 0
movimientos = []

def ver_saldo():
        print("su saldo actual es: $",saldo)

def retirar_dinero():
        global saldo
        global movimientos
        salir = True
        while(salir):
            try:
            
                retiro = int(input("¿Cuánto dinero desea retirar?\n"))
                if(retiro> saldo): 
                    print("Saldo insuficiente, digite una cantidad menor")
                else: 
                    print("Retirando dinero, por favor espere un momento...")
                    saldo-=retiro
                    movimientos.append(-retiro)
                    print("!El dinero ha sido retirado con éxito¡")
                    salir = False
            except ValueError:
                print("El valor debe ser numérico")

def depositar_dinero():
        global saldo 
        global movimientos
        salir = True
        while(salir):
            try:
                  
                deposito = int(input("¿Cuánto dinero desea depositar?\n"))
                print("Depositando el dinero, por favor espere un momento...")
                saldo += deposito
                movimientos.append(deposito)
                print("!Su dinero ha sido depositado con éxito¡")
                salir = False
            except ValueError:
                 print("El valor debe ser numérico")

def ver_movimientos():
        print(tuple(movimientos))

while True: # Esta estructura nos permite regresar el menú cada vez que el usuario termine de utilizar una funcionalidad.

        print(" ======================================//====================================== \n")
        print("¡Bienvenido!\n")
        print("\nSeleccione una de las siguientes opciones:\n")
        print("1. Ver el saldo de tu cuenta.\n2. Retirar dinero.")
        print("3. Depositar dinero.\n4. Ver el historial de movimientos.")
        print("5. Salir\n")

        opcion_menu1 =input("Por favor digite la opción que desea elegir aquí: ---> ")
        if opcion_menu1=="1":
            print("Has elegido: Ver el saldo de tu cuenta.")
            ver_saldo()

        elif opcion_menu1=="2":
            print("Has elegido: Retirar dinero.")
            retirar_dinero()

        elif opcion_menu1=="3":
            print("Has elegido: Depositar dinero.")
            depositar_dinero()

        elif opcion_menu1=="4":
            print("Has elegido: Ver el historial de movimientos")
            ver_movimientos()

        elif opcion_menu1=="5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intente nuevamente")