num1 = int(input('Introduce el dividendo '))
num2 = int(input('Introduce el divisor '))

if (num2 == 0):
    print('No se puede dividir por cero')
else:
    print(f'{num1}/{num2} =',(num1/num2))