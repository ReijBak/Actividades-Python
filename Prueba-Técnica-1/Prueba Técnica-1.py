#    Caso de uso (Épica): Como líder de operaciones de inventario, quiero un sistema que permita
#    gestionar el inventario de una tienda de manera dinámica, para que pueda realizar un seguimiento
#    eficiente de los productos disponibles, su cantidad y precios actualizados, además de calcular el valor
#    total del inventario.
#
#    Funcionalidades principales: para alcanzar un resultado óptimo en esta prueba, deberás:
#    
#    1. Añadir productos al inventario: permitir al usuario agregar productos con atributos como
#       nombre, precio y cantidad disponibles.
#    2. Consultar productos en inventario: buscar un producto por su nombre y mostrar sus
#       detalles (nombre, precio, cantidad).
#    3. Actualizar precios de productos: modificar el precio de un producto específico en el
#       inventario.
#    4. Eliminar productos del inventario: permitir la eliminación de un producto que ya no está
#       disponible.
#    5. Calcular el valor total del inventario: multiplicar el precio por la cantidad de cada producto
#       y mostrar el total acumulado.

print("\n¡Bienvenido! 👋\n")

inventory = {} # The dictionary to be used to store the items is declared.

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

def add_product(): # This function is used for add a item, if it haven't was added yet.
    
    cont = True
    name = input("Nombre del producto 📦: ").strip().lower()
    
    if name in inventory:
        print(WARNING + "⚠️ El producto ya existe en el inventario." + RESET)
        return
    
    while cont:    
        
        try:
            
            price = float(input("Precio del producto: "))
            if price <= 0:
                print(DANGER + "❌ Error: El precio debe ser una cantidad positiva." + RESET)
                continue
            cont = False

        except ValueError:
            print(DANGER + "❌ Error: Ingresa valores numéricos válidos." + RESET)

    cont = True
    while cont:

        try:

            quantity = int(input("Cantidad disponible: "))
            if quantity <= 0:
                print(DANGER + "❌ Error: La cantidad debe ser positiva." + RESET)
                continue
            cont = False

        except ValueError:
            print(DANGER + "❌ Error: Ingresa valores numéricos válidos." + RESET)

    inventory[name] = {"price": price, "quantity": quantity}
    print(SUCCESS + "✅ Producto añadido correctamente." + RESET)
        

def check_product(): # This one displays the data for a specific item if it exists. If the item that you typed don't exist, you can add it as a new item.

    print("Lista de productos 📦:\n")
    for product in inventory:
        print(f"- {product.title()}")
    print("")

    name = input("Nombre del producto a consultar: ").strip().lower()
    product = inventory.get(name)
    
    if product:
        print(f"📦 Producto: {name.title()}")
        print(f"   Precio: ${product['price']:.2f}")
        print(f"   Cantidad: {product['quantity']}")
    else:
        print(DANGER + "❌ Producto no encontrado en el inventario." + RESET)

        cont = True
        while cont:

            add_missing_product = input("¿Desea agregar el producto al inventario? (S/N)\n").lower()

            if add_missing_product == "s":
                add_product()
                cont = False
            elif add_missing_product == "n":
                print("El producto no ha sido agregado")
                cont = False
            else:
                print(DANGER + "❌ Error: Opción no válida, intente de nuevo" + RESET)

def update_price(): # This one is used to update the price of one item if it exists. If the item that you typed don't exist, you can add it as a new item.

    print("Lista de productos 📦:\n")
    for product in inventory:
        print(f"- {product.title()}")
    print("")

    name = input("Nombre del producto a actualizar: ").strip().lower()
    if name in inventory:
        try:
            new_price = float(input("Nuevo precio: "))
            inventory[name]['price'] = new_price
            print(SUCCESS + "✅ Precio actualizado correctamente." + RESET)
        except ValueError:
            print(DANGER + "❌ Error: El precio debe ser un número válido." + RESET)
    else:
        print(DANGER + "❌ Producto no encontrado en el inventario." + RESET)

        cont = True
        while cont:

            add_missing_product = input("¿Desea agregar el producto al inventario? (S/N)\n").lower()

            if add_missing_product == "s":
                add_product()
                cont = False
            elif add_missing_product == "n":
                print("El producto no ha sido agregado")
                cont = False
            else:
                print(DANGER + "❌ Error: Opción no válida, intente de nuevo" + RESET)

def delete_product(): # This one is used to delete one item.
    
    print("Lista de productos 📦:\n")
    for product in inventory:
        print(f"- {product.title()}")
    print("")

    name = input("Nombre del producto a eliminar: ").strip().lower()
    if name in inventory:
        del inventory[name]
        print(WARNING + "🗑️ Producto eliminado correctamente." + RESET)
    else:
        print(DANGER + "❌ Producto no encontrado en el inventario." + RESET)

def calculate_total_value(): # And this one calculates the items total value.

    print("Lista de productos 📦:\n")
    for product in inventory:
        print(f"- {product.title()}")
    print("")

    total = sum(map(lambda x: x['price'] * x['quantity'], inventory.values()))
    print(WARNING + f"💰 Valor total del inventario: ${total:.2f}" + RESET)

def menu(): # This fuction contains a dictionary used for the menu.
    
    first = True

    if first == True:
        print("Introduce al menos un producto para acceder a las todas funcionalidades\n")
        add_product()
        first = False

    options = {
        "1": add_product,
        "2": check_product,
        "3": update_price,
        "4": delete_product,
        "5": calculate_total_value,
        "6": finish
    }
    while True:
        print(" ================================== // ================================== ")
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

def finish():
    print("👋 Saliendo del programa... ¡Hasta luego!")
    exit()

if __name__ == "__main__":
    menu()