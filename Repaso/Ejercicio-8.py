while True:
    
    tarea = input("¿Terminaste la tarea? (Si/No): ").strip().lower()

    if tarea == "no":
        print("¡Debes terminar la tarea!")
        continue
    elif tarea == "si":
        print("¡Ves que no era tan dificil!") 
        break
    else:
       print("Muy gracios@, ¡debes responder Si o No!")
       continue
    
