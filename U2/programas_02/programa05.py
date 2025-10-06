'''Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto'''

num = 0

while (num < 1 or num > 10):
    num = int(input('Introduce un numero del 1 al 10: '))

for x in range(1,num + 1):
    print(x)