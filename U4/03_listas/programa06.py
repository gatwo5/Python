cadena = "I try to live in black and white but im so blue"

lista_split = cadena.split()
lista_partition = list(cadena.partition(' '))

print(lista_split)
print(lista_partition)

# ----

lista_split = ['And', 'when', 'the', 'seasons', 'change']
cadena = ' '.join(lista_split)

print(cadena)
