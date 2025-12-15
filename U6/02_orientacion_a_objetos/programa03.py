from abc import ABC, abstractmethod

class AnimalMarino(ABC):

    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @abstractmethod
    def sonido(self):
        pass

    @abstractmethod
    def saluda(self):
        pass

class Delfin(AnimalMarino):
    
    def __init__(self, nombre):
        super().__init__(nombre)

    def sonido(self):
        print("Clicks y silbidos")

    def saluda(self):
        print(f"Hola soy un deflin llamado {self.nombre}")

class Tiburon(AnimalMarino):

    def __init__(self, nombre):
        super().__init__(nombre)

    def sonido(self):
        print("No tiene un sonido audible caracteristico")

    def saluda(self):
        print(f"Hola soy un tiburon llamado {self.nombre}")

animales_marinos = [Delfin('Alex'), Tiburon('Juanita')]

for animal in animales_marinos:
    animal.sonido()
    animal.saluda()

