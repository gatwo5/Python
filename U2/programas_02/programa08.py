'''Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.'''
import random

num_aleatorio = random.randrange(1, 21)
num_introducido_por_usuario = 1
contador_intentos = 0

while (contador_intentos < 3 and num_introducido_por_usuario != contador_intentos):
    num_introducido_por_usuario = int(input('Introduce un numero: '))

    if (num_introducido_por_usuario > num_aleatorio):
        print('El numero es menor')
    elif (num_introducido_por_usuario < num_aleatorio):
        print('El numero es mayor')

    contador_intentos += 1

if (contador_intentos > 2):
    print('Has perdido. El numero era', num_aleatorio)
else:
    print('Has ganado en',contador_intentos,'intentos')