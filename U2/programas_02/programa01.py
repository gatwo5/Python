'''
Escribe un programa que muestre una lista de números del 1 al 10. Resuelve el ejercicio
de dos formas distintas, utilizando los bucles for y while. Cuando utilices el bucle for
puedes hacer uso de la función range.
'''
print('Primera forma: ')

i = 1

while (i <= 10):
    print(i)
    i+=1

print('Segunda forma: ')

j = range(1,11)

for n in j:
    print(n)