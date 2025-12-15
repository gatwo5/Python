# ==== AnimalTerrestre ====

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

# ==== Mamífero ====

class Mamifero(AnimalTerrestre):

    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.__gestacion_dias = gestacion_dias

    # --- GETTERS & SETTERS ---

    @property
    def gestacion_dias(self):
        return self.__gestacion_dias
    
    @gestacion_dias.setter
    def gestacion_dias(self, nuevo_gestacion_dias):
        self.__gestacion_dias = nuevo_gestacion_dias

    # --- METODOS DE INSTANCIA

    def saluda(self):
        print(f"Soy un mamífero llamado {self.nombre}, tengo {self.edad} años y mi gestación dura 100 días")

class Ave(AnimalTerrestre):

    def __init__(self, nombre, edad, peso, puede_volar):

        super().__init__(nombre, edad, peso)
        self.__puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self.__puede_volar
    
    @puede_volar.setter
    def puede_volar(self, nuevo_puede_volar):
        self.__puede_volar = nuevo_puede_volar

    def saluda(self):

        if self.__puede_volar:
            cadena = "puedo volar"
        else:
            cadena = "no puedo volar"

        print(f"Soy un ave llamado {self.nombre}, tengo {self.edad} anios y {cadena}")

animales = [
    AnimalTerrestre("Kuma",10, 100), 
    AnimalTerrestre("Miu", 5,  6), 
    Mamifero("Log", 10, 90, 200),
    Ave("Uff", 4, 3, True)
]

for animal in animales:
    animal.saluda()



