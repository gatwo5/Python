import random

eleccion = int(input('1. Piedra\n2. Papel\n3. Tijera\nSeleccione una opción (1, 2 o 3): '))
resultado_maquina = random.randrange(1, 4)

print(f"Tu elecion: {eleccion} | Eleccion de la maquina: {resultado_maquina}")

match (eleccion):
    case 1:
        if (resultado_maquina == 2):
            print('Perdiste: Piedra pierde contra Papel')
        elif (resultado_maquina == 3):
            print('Ganaste: Piedra gana a Tijera')
        else:
            print('Empate: Piedra contra Piedra')
    case 2:
        if (resultado_maquina == 1):
            print('Ganaste: Papel gana a Piedra')
        elif (resultado_maquina == 3):
            print('Perdiste: Papel pierde contra Tijera')
        else:
            print('Empate: Papel contra Papel')
    case 3:
        if (resultado_maquina == 1):
            print('Perdiste: Tijera pierde contra Piedra')
        elif (resultado_maquina == 2):
            print('Ganaste: Tijera gana a Papel')
        else:
            print('Empate: Tijera contra Tijera')
