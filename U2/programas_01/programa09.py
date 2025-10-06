'''Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra'''
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
