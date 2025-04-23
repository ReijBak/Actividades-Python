#                          Ejercicio

# Un menú en dónde se pueda ingresar para relizar las siguentes tareas:
# - Crear un usuario con sus datos (Nombre, apellido, correo y edad).
# - Consultar los datos de un usuario y editarlos si se requiere.
# - Eliminar un usuario.
# - Enlistar todos los usuarios registrados y sus datos.

#==========================================================================

usuarios = {}
#==========================================================================
# Consultar usuario

def crear_usuario():
    
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    edad = input("Ingrese la edad: ")
    correo = input("Ingrese el correo del usuario: ")
    if correo in usuarios:
        print("Ya existe un usuario con ese correo.")
        return
    usuarios[correo] = {"nombre": nombre, "apellido": apellido, "edad": edad}
    print("Usuario creado exitosamente.")
#==========================================================================
# Consultar usuario

def consultar_usuario():
    correo = input("Ingrese el correo del usuario a consultar: ")
    usuario = usuarios.get(correo)
    if usuario:
        print(f"Nombre: {usuario['nombre']}")
        print(f"Apellido: {usuario['apellido']}")
        print(f"Edad: {usuario['edad']}")
        editar = input("¿Desea editar este usuario? (s/n): ").lower()
        if editar == 's':
            editar_usuario(correo)
    else:
        print("Usuario no encontrado.")
#===========================================================================
# Editar usuario

def editar_usuario(correo):
    nombre = input("Nuevo nombre: ")
    apellido = input("Nuevo apellido: ")
    edad = input("Nueva edad: ")
    usuarios[correo] = {"nombre": nombre, "apellido": apellido, "edad": edad}
    print("Usuario actualizado exitosamente.")
#==========================================================================
# Eliminar usuario

def eliminar_usuario():
    correo = input("Ingrese el correo del usuario a eliminar: ")
    if correo in usuarios:
        del usuarios[correo]
        print("Usuario eliminado exitosamente.")
    else:
        print("Usuario no encontrado.")
#==========================================================================
# Listar usuarios

def listar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for correo, datos in usuarios.items():
        print(f"\nCorreo: {correo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Apellido: {datos['apellido']}")
        print(f"Edad: {datos['edad']}")

#==========================================================================
# Menú de opciones

def menu():
    while True:
        print("\n--- MENÚ DE USUARIOS ---")
        print("1. Crear usuario")
        print("2. Consultar/Editar usuario")
        print("3. Eliminar usuario")
        print("4. Listar todos los usuarios")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_usuario()
        elif opcion == '2':
            consultar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            listar_usuarios()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()
