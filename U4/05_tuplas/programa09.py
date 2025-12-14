tupla_numeros = (
    (1,2,3), 
    (4,5,6), 
    (7,8,9)
)

for fila in tupla_numeros:
    for num in fila:
        print(num, end=' ')
    print()

tupla_listas = (
    [1,2,3],
    [4,5,6],
    [7,8,9]
)

tupla_listas[0][0] = 200

print(tupla_listas[0][0])