frutas = ["manzana","mango", "fresa","mora"]

print("Lista de frutas: ",frutas)
eliminar = input("¿Qué fruta deseas eliminar? ")

if eliminar in frutas:
    frutas.remove(eliminar)
    print("Fruta eliminada.")
else:
    print("La fruta no está en la lista.")

print("Lista actualizada:",frutas)
