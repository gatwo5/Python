'''Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso'''

num_par = int(input('Introduce un numero par '))
num_impar = int(input('Introduce un numero impar '))

if (num_par % 2 != 0 or num_impar % 2 == 0):
    print('Numeros no validos')
else:
    print('Numeros validos')
