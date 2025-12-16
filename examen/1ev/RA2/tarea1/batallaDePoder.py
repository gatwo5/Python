import random

# Estadísticas del jugador
vidasJugador = 3
puntosJugador = 0
nivelJugador = 1

#Elección del jugador
eleccionAtaqueJugador = 0

#Puntuación de combate
valorCartaJugador = 0
valorCartaEnemigo = 0

try:
    while(vidasJugador > 0):

        eleccionAtaqueJugador = int(input('Introduce el tipo de ataque\n1. Fuerza\n2. Precision\n3. Riesgo\n'))

        while (eleccionAtaqueJugador < 1 or eleccionAtaqueJugador > 3):
            eleccionAtaqueJugador = int(input('Introduce el tipo de ataque\n1. Fuerza\n2. Precision\n3. Riesgo\n'))

        #Decisión de estilo de combate
        match eleccionAtaqueJugador:

            case 1:

                valorCartaJugador = random.randrange(5,11)
                valorCartaEnemigo = random.randrange(3,11)

            case 2:

                valorCartaJugador = random.randrange(3,9)
                valorCartaEnemigo = random.randrange(2,10)

            case 3:

                valorCartaJugador = random.randrange(1,11)
                valorCartaEnemigo = random.randrange(1,9)

        print(f'Jugador: {valorCartaJugador} | Enemigo: {valorCartaEnemigo}')

        #Si el valor del jugador es mayor al enemigo
        if (valorCartaJugador > valorCartaEnemigo):

            print('Ganaste! Obtienes 1 punto')
            puntosJugador += 1

            #Si consigue 3 puntos más
            if (puntosJugador % 3 == 0):
                print('Subes de nivel!')

                #En caso de tener menos de 3 de vida consigue una más
                if(vidasJugador < 3):
                    print('Consigues una vida!')
                    vidasJugador += 1

        #Si el valor del jugador es menor al enemigo
        elif (valorCartaJugador < valorCartaEnemigo):
            print('Perdiste! Pierdes 1 vida')
            vidasJugador -= 1

        print()
        print(f'Situacion actual: Vidas: {vidasJugador} | Puntos: {puntosJugador} | Nivel: {nivelJugador}')
        
        #Final de partida
        print(f'Final de partida: Puntos = {puntosJugador} | Nivel = {nivelJugador}')

except ValueError:
    print('Dato no valido')

