# Eres parte del equipo de desarrollo de software de una tienda que desea mejorar la gestión de su inventario digital. Te han asignado la tarea de crear un 
# programa en Python que permita al equipo añadir, consultar, actualizar y eliminar productos del inventario de manera eficiente, así como calcular el valor 
# total del inventario. Tu programa debe interactuar con el usuario para realizar las siguientes operaciones:
# 
#     Añadir productos:
#       - Cada producto debe estar definido por su nombre, precio y cantidad disponible.
#       - Esta información será almacenada de modo que el inventario pueda crecer dinámicamente.
#     Consultar productos:
#       - Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible.
#       - Si el producto no está en el inventario, se debe notificar adecuadamente.
#     Actualizar precios:
#       - El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el 
#         inventario.
#     Eliminar productos:
#       - El programa debe permitir al usuario eliminar productos del inventario de manera segura.
#     Calcular el valor total del inventario:
#       - El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario.
#       - Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.
# 
# ============================================================================= // ============================================================================= 

inventario = {}

def añadir_producto():
    nombre = input("Nombre del producto: ").strip().lower()
    if nombre in inventario:
        print("⚠️ El producto ya existe en el inventario.")
        return
    try:
        precio = float(input("Precio del producto: "))
        cantidad = int(input("Cantidad disponible: "))
        inventario[nombre] = {"precio": precio, "cantidad": cantidad}
        print("✅ Producto añadido correctamente.")
    except ValueError:
        print("❌ Error: Ingresa valores numéricos válidos.")

def consultar_producto():
    nombre = input("Nombre del producto a consultar: ").strip().lower()
    producto = inventario.get(nombre)
    if producto:
        print(f"📦 Producto: {nombre.title()}")
        print(f"   Precio: ${producto['precio']:.2f}")
        print(f"   Cantidad: {producto['cantidad']}")
    else:
        print("❌ Producto no encontrado en el inventario.")

def actualizar_precio():
    nombre = input("Nombre del producto a actualizar: ").strip().lower()
    if nombre in inventario:
        try:
            nuevo_precio = float(input("Nuevo precio: "))
            inventario[nombre]['precio'] = nuevo_precio
            print("✅ Precio actualizado correctamente.")
        except ValueError:
            print("❌ Error: El precio debe ser un número válido.")
    else:
        print("❌ Producto no encontrado.")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip().lower()
    if nombre in inventario:
        del inventario[nombre]
        print("🗑️ Producto eliminado correctamente.")
    else:
        print("❌ Producto no encontrado.")

def calcular_valor_total():
    total = sum(map(lambda x: x['precio'] * x['cantidad'], inventario.values()))
    print(f"💰 Valor total del inventario: ${total:.2f}")

def menu():
    opciones = {
        "1": añadir_producto,
        "2": consultar_producto,
        "3": actualizar_precio,
        "4": eliminar_producto,
        "5": calcular_valor_total,
        "6": salir
    }
    while True:
        print("\n📋 Menú de Inventario:")
        print("1. Añadir producto")
        print("2. Consultar producto")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        eleccion = input("Seleccione una opción (1-6): ").strip()
        accion = opciones.get(eleccion)
        if accion:
            accion()
        else:
            print("❌ Opción no válida.")

def salir():
    print("👋 Saliendo del programa... ¡Hasta luego!")
    exit()

if __name__ == "__main__":
    menu()

