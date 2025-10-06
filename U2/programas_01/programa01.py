num_par = int(input('Introduce un numero par '))
num_impar = int(input('Introduce un numero impar '))

if (num_par % 2 != 0 or num_impar % 2 == 0):
    print('Numeros no validos')
else:
    print('Numeros validos')
