'''Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo
de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que
determine la hora de llegada a la ciudad B.'''

import math

hora = int(input('Introduce la hora de salida ')) * 3600
minuto = int(input('Introduce los minutos de salida ')) * 60
segundos = int(input('Introduce los segundos de salida '))
segundos_que_tarda = int(input('Introduce los segundos que tarda en llegar '))
total = hora + minuto + segundos + segundos_que_tarda

hora = math.floor(total / 3600)
total = total % 3600

minuto = math.floor(total / 60)
total = total % 60

segundos = total

print('hora de llegada:',hora,minuto,segundos)


