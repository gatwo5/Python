temperatura_dias = []

for i in range (0,5):
    
    maxima = int(input(f'Introduce la temperatura maxima del dia {i+1}: '))
    minima = int(input(f'Introduce la temperatura minima del dia {i+1}: '))

    temperatura_dias.append([maxima,minima])

print(min(temperatura_dias))