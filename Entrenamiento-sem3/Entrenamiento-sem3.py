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

inventory = {}

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

def add_product():
    name = input("Nombre del producto: ").strip().lower()
    if name in inventory:
        print(WARNING + "⚠️ El producto ya existe en el inventario." + RESET)
        return
    try:
        price = float(input("Precio del producto: "))
        quantity = int(input("Cantidad disponible: "))
        inventory[name] = {"price": price, "quantity": quantity}
        print(SUCCESS + "✅ Producto añadido correctamente." + RESET)
    except ValueError:
        print(DANGER + "❌ Error: Ingresa valores numéricos válidos." + RESET)

def check_product():
    name = input("Nombre del producto a consultar: ").strip().lower()
    product = inventory.get(name)
    if product:
        print(f"📦 Producto: {name.title()}")
        print(f"   Precio: ${product['price']:.2f}")
        print(f"   Cantidad: {product['quantity']}")
    else:
        print(DANGER + "❌ Producto no encontrado en el inventario." + RESET)

def update_price():
    name = input("Nombre del producto a actualizar: ").strip().lower()
    if name in inventory:
        try:
            new_price = float(input("Nuevo precio: "))
            inventory[name]['price'] = new_price
            print(SUCCESS + "✅ Precio actualizado correctamente." + RESET)
        except ValueError:
            print(DANGER + "❌ Error: El precio debe ser un número válido." + RESET)
    else:
        print(DANGER + "❌ Producto no encontrado." + SUCCESS)

def delete_product():
    name = input("Nombre del producto a eliminar: ").strip().lower()
    if name in inventory:
        del inventory[name]
        print(DANGER + "🗑️ Producto eliminado correctamente." + RESET)
    else:
        print(DANGER + "❌ Producto no encontrado." + RESET)

def calculate_total_value():
    total = sum(map(lambda x: x['price'] * x['quantity'], inventory.values()))
    print(WARNING + f"💰 Valor total del inventario: ${total:.2f}" + RESET)

def menu():
    options = {
        "1": add_product,
        "2": check_product,
        "3": update_price,
        "4": delete_product,
        "5": calculate_total_value,
        "6": exit
    }
    while True:
        print(" ================================== // ================================== ")
        print("\nBienvenido")
        print("\n📋 Menú de Inventario:\n")
        print("1. Añadir producto.")
        print("2. Consultar producto.")
        print("3. Actualizar precio.")
        print("4. Eliminar producto.")
        print("5. Calcular valor total del inventario.")
        print("6. Salir.")
        choice = input("\nSeleccione una opción (1-6): ").strip()
        action = options.get(choice)
        if action:
            action()
        else:
            print(DANGER + "❌ Opción no válida." + RESET)

def exit():
    print("👋 Saliendo del programa... ¡Hasta luego!")
    exit()

if __name__ == "__main__":
    menu()
