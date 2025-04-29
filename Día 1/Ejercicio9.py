year=int(input("Digite un año: "))
x="El año no es bisiesto"
if year%4==0 and year%100!=0:
    x="El año es bisiesto"
elif year%400==0:
    x="El año es bisiesto"
print(x)