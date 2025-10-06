'''Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una'''
import random

banca = random.randrange(17,22)
mano_jugador = 0
seguir_robando = True

print('Banca:', banca)

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



