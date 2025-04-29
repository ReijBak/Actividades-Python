while True:
    
    licencia = input("¿Tiene licencia? (Si/No)").strip().lower()
    casco = input("¿Tiene Casco? (Si/No)").strip().lower()
    
    if licencia == "no" or casco == "no":
        print("No puede conducir")
        break
    elif (licencia == "si" or licencia == "sí") and (casco == "si" or casco == "sí"):
        print("Puede conducir")
        break
    else:
       print("Debe responder Si o No")
       continue
    
