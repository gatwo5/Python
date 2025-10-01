import math

#Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
#cuantas horas y minutos corresponde

minutos = int(input('Introduce minutos: '))
print(minutos,'minutos son',math.floor((minutos/60)),'hora/s y',(minutos%60),'minuto/s')