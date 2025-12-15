class Animal:

    def __init__(self, nombre, especie, edad, id_chip):

        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.__id_chip = id_chip
        

    # --- MÉTODOS DE ISNTANCA ---

    def saluda(self):
        return f'Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años'
    
    def cumplir_anios(self):
        self.edad += 1

    def get_id_chip(self):
        return self.__id_chip
    
    def set_id_chip(self, nuevo_id):
        if type(nuevo_id) is str:
            self.__id_chip = nuevo_id
        else:
            raise (TypeError("El id_chip debe ser string"))
        
animal = Animal('Kuma', 'tigre', 5, "AAA")

animal.set_id_chip("BBB")

print(animal.get_id_chip())
