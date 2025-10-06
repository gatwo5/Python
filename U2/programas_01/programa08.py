'''Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)'''
import random

jugador1_dado1 = random.randrange(1, 7)
jugador1_dado2 = random.randrange(1, 7)
jugador1_total = jugador1_dado1 + jugador1_dado2
jugador1_dado_mayor = 0

jugador2_dado1 = random.randrange(1, 7)
jugador2_dado2 = random.randrange(1, 7)
jugador2_total = jugador2_dado1 + jugador2_dado2
jugador2_dado_mayor = 0


print(f"Jugador 1: Dado1 -> {jugador1_dado1} | Dado 2 -> {jugador1_dado2}")
print(f"Jugador 2: Dado1 -> {jugador2_dado1} | Dado 2 -> {jugador2_dado2}")

if (jugador1_total > jugador2_total):
    print('Ganador: Jugador 1')
elif (jugador1_total < jugador2_total):
    print('Ganador: Jugador 2')
else:
    if (jugador1_dado1 > jugador1_dado2):
        jugador1_dado_mayor = jugador1_dado1
    else:
        jugador1_dado_mayor = jugador1_dado2
    
    if (jugador2_dado1 > jugador2_dado2):
        jugador2_dado_mayor = jugador2_dado1
    else:
        jugador2_dado_mayor = jugador2_dado2
    
    if (jugador1_dado_mayor > jugador2_dado_mayor):
        print('Ganador: Jugador 1, dado mayor')
    elif (jugador2_dado_mayor > jugador1_dado_mayor):
        print('Ganador: Jugador 2, dado mayor')
    else:
        print('Empate')