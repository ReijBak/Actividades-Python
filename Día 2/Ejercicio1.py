num1=float(input("Por favor dame un número: "))
num2=float(input("Por favor dame otro número: "))
num3=float(input("Por favor dame otro número: "))
if num1<num2<num3 or num1<num3<num2:
    print(num1)
elif num2<num1<num3 or num2<num3<num1:
    print(num2)
else:
    print(num3)