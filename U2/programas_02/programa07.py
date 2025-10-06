'''Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no'''

print('Version sin break: ')

num = 1
total = 0
contador_num = -1

while (num != 0):
    num = int(input('Introduce un numero: '))
    total += num
    contador_num += 1

print(f"Suma: {total} | Media:",(total/contador_num))


print('Version con break: ')

num = 1
total = 0 
contador_num = 0

while (True):
    num = int(input('Introduce un numero: '))

    if (num == 0):
        break
    else:
        total += num
        contador_num += 1

print(f"Suma: {total} | Media:",(total/contador_num))
