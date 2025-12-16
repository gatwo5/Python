from batalla import jugador
from batalla import enemigo

def main():
    #Stats del jugador
    nombreJugador = ''
    conocimientoJugador = 0
    energiaJugador = 0
    magiaJugador = 0

    #Stats del enemigo
    nombreEnemigo = ''
    conocimientoEnemigo = 0
    energiaEnemigo = 0
    magiaEnemigo = 0

    try :
        #Introducir valores del jugador
        nombreJugador = str(input('Introduce tu nombre: '))

        while (conocimientoJugador < 1 or conocimientoJugador > 10):
            conocimientoJugador = int(input('Nivel de conocimiento (1-10): '))
        
        while (energiaJugador < 1 or energiaJugador > 5):
            energiaJugador = int(input('Energia inicial (1-5): '))

        #Mostrar jugador
        jugador.mostrar_jugador(nombreJugador, conocimientoJugador, energiaJugador)
        print()

        #Crear y mostrar enemigo
        nombreEnemigo, conocimientoEnemigo, energiaEnemigo = enemigo.generar_enemigo()
        enemigo.mostrar_enemigo(nombreEnemigo, conocimientoEnemigo, energiaEnemigo)

        # 3 Rondas

        for i in range(1,4):
            print(f'--- RONDA {i} ---')

            #Establecer niveles de magia
            magiaJugador = jugador.ataque_jugador(conocimientoJugador, energiaJugador)
            magiaEnemigo = enemigo.ataque_enemigo(conocimientoEnemigo, energiaEnemigo)

            print(f'Magia de {nombreJugador}: {magiaJugador}')
            print(f'Magia de {nombreEnemigo}: {magiaEnemigo}')

            #Combate
            if (magiaJugador < magiaEnemigo):
                energiaJugador = energiaJugador - 1
                print(f'{nombreEnemigo} responde con un conjuro devastador!  (-1 energia jugador)')

            elif (magiaJugador > magiaEnemigo):
                energiaEnemigo = energiaEnemigo - 1
                print(f'{nombreJugador} lanza un hechizo poderoso!  (-1 energia enemigo)')

        # Resultado final
        print('=== FIN DEL DUELO ===')

        if(energiaJugador > energiaEnemigo):
            print(f'{nombreJugador} ha vencido a {nombreEnemigo}!')

        elif(energiaJugador < energiaEnemigo):
            print(f'{nombreEnemigo} ha vencido a {nombreJugador}!')

        else:
            print('EMPATE EPICO!')

    except ValueError:
        print('Dato no valido')

if __name__ == "__main__":
    main()