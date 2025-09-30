"""
programa02
Escribe un programa que escriba por pantalla: el booleano True, dos literales enteros,
dos literales flotantes y una cadena de caracteres, y para cada uno de ellos su tipo de
datos
"""

booleano = True
entero1 = 5
entero2 = 43
flotante1 = 4.56
flotante2 = 10.78
cadena_caracteres = "Me encanta la programación en Python, pero necesito de vuelta los punto y coma y los corchetes!!!!!"

print(str(booleano) + " -> " + str(type(booleano)))
print(str(entero1) + " -> " + str(type(entero1)))
print(str(entero2) + " -> " + str(type(entero2)))
print(str(flotante1) + " -> " + str(type(flotante1)))
print(str(flotante2) + " -> " + str(type(flotante2)))
print(cadena_caracteres + " -> " + str(type(cadena_caracteres)))


