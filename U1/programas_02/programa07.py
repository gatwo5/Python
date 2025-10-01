import math

minutos = int(input('Introduce minutos: '))
print(minutos,'minutos son',math.floor((minutos/60)),'hora/s y',(minutos%60),'minuto/s')