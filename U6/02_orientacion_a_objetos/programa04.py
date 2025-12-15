class AnimalTerrestre:

    def __init__(self, nombre, edad, peso):

        self.__nombre = nombre
        self.__edad = edad
        self.__peso = peso

    # --- GETTERS & SETTERS ---

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def peso(self):
        return self.__peso
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    @peso.setter
    def peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    # --- MÉTODOS DE INSTANCIA ---

    def saluda(self):
        print(f'Soy un animal terrestre llamado {self.__nombre} y tengo {self.__edad} años')

    def __str__(self):
        return f'Soy un animal terrestre llamado {self.__nombre} y tengo {self.__edad} años'
    
    def __lt__(self, otro):
        return self.__edad < otro.edad
    
    def __add__(self, otro):
        nombre = self.__nombre + otro.nombre
        edad = (self.__edad + otro.edad)/2
        peso = self.__peso + otro.peso

        return AnimalTerrestre(nombre, edad, peso)
    
animal = AnimalTerrestre(nombre='Kuma',edad=5, peso=120.0)
animal2 = AnimalTerrestre(nombre='Rei',edad=10, peso=50.0)
animal3 = animal + animal2

print(animal3)