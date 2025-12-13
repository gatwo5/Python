mi_lista10 = [1, 'cadenita', False, 3.14]

mi_lista10[2] = True

mi_lista10.append('Me encanta Python')

mi_lista10.insert(1, 'Hola!')

# ------------

lista2 = mi_lista10[2:5]
listapares = mi_lista10[::2]
lista_inversa = mi_lista10[::-1]

print(lista2)
print(listapares)
print(lista_inversa)

lista_inversa.reverse()

print(lista_inversa)