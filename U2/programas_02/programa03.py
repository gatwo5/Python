'''
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el
ejercicio de 4 formas diferentes. Usando los bucles for y while sin y con la sentencia
continue
'''
print('Resuelto con For sin continue: ')

for x in range(0, 11, 2):
    print(x)

print('Resuelto con For con continue: ')

for x in range(0, 11, 2):
    print(x)
    continue

print('Resuelto con While sin continue: ')

i = 0

while i <= 10:
    print(i)
    i+=2

print('Resuelto con While con continue: ')

i = 0

while i <= 10:
    print(i)
    i+=2
    continue


