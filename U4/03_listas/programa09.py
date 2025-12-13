lista = [[i for i in range(0,201,2) if i % 2 == 0], [i for i in range(1,201,2)]]

for i in lista:
    for j in i:
        print(j, end=' ')
    print()