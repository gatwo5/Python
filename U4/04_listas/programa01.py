num_usuario = 1
lista_numeros = []

while (num_usuario >= 0):
    num_usuario = int(input("Introduce un numero: "))
    lista_numeros.append(num_usuario)

print('El numero maximo es:', max(lista_numeros))

print('Numeros pares: ')

for numero in lista_numeros:

    if (numero % 2 == 0):
        print(numero, end= ' ')

