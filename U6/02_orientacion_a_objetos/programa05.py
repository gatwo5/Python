class Manada:

    def __init__(self, lista_animales = []):
        self._lista_animales = lista_animales

        self._actual = 0
        self._fin = 0

    def agregar_animal(self, animal):
        self._lista_animales.append(animal)
        self._fin += 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._actual < self._fin:
            animal = self._lista_animales[self._actual]
            self._actual += 1
            return animal
        else:
            raise StopIteration

manada = Manada()

manada.agregar_animal("Perro")
manada.agregar_animal("gato")
manada.agregar_animal("Leon")
manada.agregar_animal("Buey")

for animal in manada:
    print(animal)