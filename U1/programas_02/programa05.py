#Escribe un programa que pregunte al usuario dos números y calcule su suma, resta,
#multiplicación, división, módulo y potencia
num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

print("Operaciones con", num1, "y", num2)
print("Suma:",(num1+num2))
print("Resta:",(num1-num2))
print("Multiplicacion:",(num1*num2))
print("Divison:",(num1/num2))
print("Modulo:",(num1%num2))
print("Potencia:",pow(num1,num2))
