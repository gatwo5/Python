'''Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.'''
import random

num_jugadores = int(input('Introduce el numero de jugadores: '))

banca = random.randrange(17,22)
mano_jugador = 0
seguir_robando = True

print('Banca:', banca)

for x in range(1,num_jugadores+1):
    print('Jugador', x, '-----------')

    seguir_robando = True
    mano_jugador = 0
    
    while (seguir_robando):
        print('Puntuacion actual: ', mano_jugador)
        seguir_robando = input('Quieres robar una? (s/n)').lower().startswith('s')

        if (seguir_robando):
            mano_jugador += random.randrange(1,6)

        if (mano_jugador > 21):
            seguir_robando = False

    if (mano_jugador > 21):
        print('Te has pasado de 21')
    elif (mano_jugador > banca):
        print('Has ganado con una puntuacion de', mano_jugador)
    else:
        print('Has perdido, puntuacion inferior')

