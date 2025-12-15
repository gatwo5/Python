class Animal:

    def __init__(self, nombre, especie, edad, id_chip, peso):

        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.__id_chip = id_chip
        self.__peso = peso
        

    # --- MÉTODOS DE ISNTANCA ---

    def saluda(self):
        return f'Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años'
    
    def cumplir_anios(self):
        self.edad += 1

    # id_chip

    @property
    def id_chip(self):
        return self.__id_chip
    
    @id_chip.setter
    def id_chip(self, nuevo_id):
        if type(nuevo_id) is str:
            self.__id_chip = nuevo_id
        else:
            raise (TypeError("El id_chip debe ser string"))
        
    # Peso

    @property
    def peso(self):
        return(self.__peso)
    
    @peso.setter
    def peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    @peso.deleter
    def peso(self):
        del self.__peso

# ----- MAIN -------

animal = Animal("Chispas", "gato", 14, "AAA", 15)

print(animal.peso)

animal.peso = 10
print(animal.peso)

del animal.peso
print(animal.peso)

