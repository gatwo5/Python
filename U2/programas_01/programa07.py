anno = int(input('Introduce un año '))
bisiesto = (anno % 4 == 0) and (anno % 100 != 0 or anno % 400 == 0)

if (bisiesto):
    print(anno, 'es bisiesto')
else:
    print(anno, 'no es bisiesto')