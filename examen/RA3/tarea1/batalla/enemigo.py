import random

#genera_enemigo. No recibe nada y devuelve el enemigo de forma aleatoria
def generar_enemigo():

    nombres = ['Hydra', 'Kraken', 'Minotauro', 'Gorgona', 'Titán']

    nombre = random.choice(nombres)
    conocimiento = random.randrange(1,11)
    energia = random.randrange(1,6)

    return nombre, conocimiento, energia

#ataque_enemigo. Recibe el conocimiento y la energia para devolver su nivel de magia
def ataque_enemigo(conocimiento, energia):
    return (conocimiento * energia) * random.randrange(1,4)

#mostrar_enemigo. Recibe nombre, conocimiento y energia y lo muestra por pantalla
def mostrar_enemigo(nombre, conocimiento, energia):
    print(f'Enemigo: {nombre}\nConocimiento: {conocimiento}\nEnergia: {energia}')