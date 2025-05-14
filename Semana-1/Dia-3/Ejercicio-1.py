#   Ejericio 1 - 🧩 Gestión de Biblioteca
#   Contexto:
#   Una pequeña biblioteca necesita registrar sus libros en un sistema muy simple.
#   
#   Tareas:
#   -Crear:
#   Agrega nuevos libros al diccionario.
#   Cada libro tendrá: ID, Título, Autor, Año de publicación.
#   
#   -Leer:
#   Muestra todos los libros almacenados.
#   Permite buscar un libro por su ID o Título.
#   
#   Actualizar:
#   Modifica la información de un libro dado su ID.
#   Ejemplo: cambiar el autor o el año de publicación.
#   
#   Eliminar:
#   Elimina un libro de la biblioteca usando su ID.

print("\n¡Bienvenido! 👋\n")

books = {}

DANGER = "\033[91m"
WARNING = "\033[93m"
SUCCESS = "\033[92m"
RESET = "\033[0m"

def add_book():

    cont = True
    id = input("ID del libro: ").strip().lower()

    if id in books:
        print(WARNING + "⚠️ Ya se encuentra un libro registrado con esta ID." + RESET)
        return
    
    title = input("Título del libro 📘: ").strip().lower()
    author = input("Autor del libro: ")
    
    while cont:

        try:

            year = int(input("Año de publicación: "))
            if year > 2025:
                print("DANGER + ❌ Error: No puede ser un año que no ha pasado" + RESET)
                continue
            cont = False
        
        except ValueError:
            print(DANGER + "❌ Error: Ingresa valores numéricos válidos." + RESET)

    books[id] = {"title": title, "author": author, "year": year}
    print(SUCCESS + "✅ Libro añadido correctamente." + RESET)

def search_book():
    
    id = input("ID del libro a consultar: ").strip().lower()
    book = books.get(id)

    if book:
        print(f"📘 Título del libro: {book['title'].title()}")
        print(f"   Autor del libro: {book['author'].title()}")
        print(f"   Año de publicación: {book['year']}")
    else:
        print(DANGER + "❌ Libro no encontrado." + RESET)

def update_book():

    cont = True
    id = input("ID del libro a actualizar: ").strip().lower()
    if id in books:
        new_author = input("Nuevo autor: ")
        books[id]['author'] = new_author
        while cont:
            new_year = int(input("Nuevo año de lanzamiento: "))
            if new_year > 2025:
                print("DANGER + ❌ Error: No puede ser un año que no ha pasado" + RESET)
                continue
            books[id]['year'] = new_year
            cont = False
            
def delete_book():
    
    id = input("Nombre del libro a eliminar: ").strip().lower()
    if id in books:
        del books[id]
        print(WARNING + "🗑️ Libro eliminado correctamente." + RESET)
    else:
        print(DANGER + "❌ Libro no encontrado." + RESET)

def menu():
    options = {
        "1": add_book,
        "2": search_book,
        "3": update_book,
        "4": delete_book,
        "5": finish
    }

    while True:
        print(" ================================== // ================================== ")
        print("\n Menú Gestión de Biblioteca:\n")
        print("1. Añadir libro.")
        print("2. Consultar libro.")
        print("3. Actualizar libro.")
        print("4. Eliminar libro.")
        print("5. Salir.")
        
        choice = input("\nSeleccione una opción (1-5): ").strip()
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
