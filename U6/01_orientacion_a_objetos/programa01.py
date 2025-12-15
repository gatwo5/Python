class Animal:

    def __init__(self, nombre, especie, edad):

        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # --- MÉTODOS DE ISNTANCA ---

    def saluda(self):
        return f'Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años'
    
    def cumplir_anios(self):
        self.edad += 1
    
animal = Animal('Kuma', 'tigre', 5)
animal2 = Animal('Trululú', 'perro', 2)

print(animal.saluda())
animal.cumplir_anios()
print(animal.saluda())

print(animal2.saluda())
animal2.cumplir_anios()
print(animal2.saluda())

animal2.nombre = 'dali'

print(animal2.saluda())
