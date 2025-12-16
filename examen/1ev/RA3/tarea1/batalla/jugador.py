import random

#ataque_jugador. Recibe el conocimiento y la energia para devolver su nivel de magia
def ataque_jugador(conocimiento, energia):
    return (conocimiento * energia) * random.randrange(1,4)

#mostrar_jugador. Recibe el nombre, conocimiento y energia para imprimirlo
def mostrar_jugador(nombre, conocimiento, energia):
    print(f'Jugadora: {nombre}\nConocimiento: {conocimiento}\nEnergia: {energia}')