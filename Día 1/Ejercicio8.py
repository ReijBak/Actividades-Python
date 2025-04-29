peso=float(input("Digite su peso en kilogramos: "))
altura=float(input("Digite su altura en metros: "))
IMC=peso/altura**2
if IMC<18.5:
    print("Bajo peso")
elif 18.5<=IMC<25:
    print("Normal")
elif 25<=IMC<30:
    print("Sobrepeso")
elif IMC>=30:
    print("Obesidad")