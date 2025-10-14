import math

eleccion = int(input('1: Seno, 2: Coseno, 3: Raiz, 4: Potencia'))
num1 = 0
num2 = 0

match (eleccion):
    case 1:
        num1 = float(input('Introduce el angulo'))
        print(f'El seno de {num1} es de', math.sin(num1))
    case 2:
        num1 = float(input('Introduce el angulo'))
        print(f'El coseno de {num1} es de', math.cos(num1))
    case 3:
        num1 = float(input('Introduce numero'))
        print(f'La raiz cuadrada de {num1} es de', math.sqrt(num1))
    case 4:
        num1 = float(input('Introduce la base'))
        num2 = float(input('Introduce el exponente'))
        print(math.pow(num1,num2))