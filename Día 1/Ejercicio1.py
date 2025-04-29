nombre = input("Por favor dame tu nombre: ")
apellido = input("Por favor dame tu apellido: ")
edad = int(input("Por favor dame tu edad: "))
x=""
if edad>17:
  x="Eres es mayor de edad"
else:
  x="Eres es menor de edad"
print(nombre," ",apellido+"\n",edad,"\n",x,sep="")
