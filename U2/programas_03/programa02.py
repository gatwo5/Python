num = 0

while (num < 1 or num > 10):
    try: 
        num = int(input('Introduce un numero entre 1 y 10: '))
    except ValueError:
        print('Solo se pude introducir numeros enteros')

for x in range(1,num+1):
    print(x)