from abc import ABC, abstractmethod
import random

# ==== CLASE PERSONAJE ====

class Personaje(ABC):

    def __init__(self, nombre, vida):

        self._nombre = nombre
        self._vida = vida
        self._vivo = True

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, nueva_vida):

        if nueva_vida > 0:
            self._vida = nueva_vida

        else:
            print('No se puede tener vida negativa')

    @property
    def vivo(self):
        return self._vivo
    
    @abstractmethod
    def atacar(self, objetivo):
        pass

# ==== CLASE ARMA ====

class Arma:

    def __init__(self, nombre, danio):
        self._nombre = nombre
        self._danio = danio
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def danio(self):
        return self._danio
    
# ==== CLASE GUERRERO ====

class Guerrero(Personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre,vida)
        self._arma = Arma("Dragon slayer", 15)

    def atacar(self, enemigo):
        ataque = self._arma.danio + random.randrange(1,11)
        enemigo.vida = enemigo.vida - ataque

# ==== CLASE MAGO ====

class Mago(Personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre,vida)

        self._hechizos = {
            "Bola de fuego": 18,
            "Rayo": 22,
            "Hielo": 10,
            "Maldición": 25
        }
    
    def atacar(self, enemigo):
        ataque = random.choice(list(self._hechizos.values()))
        enemigo.vida = enemigo.vida - ataque
        