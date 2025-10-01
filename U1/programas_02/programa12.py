'''Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los
resultados deben estar redondeados a 2 decimales.'''

millas = float(input('Introduce las milas: '))
kilometros = float(input('Introduce los kilometros: '))
print('millas en kilometros:',round((millas*1.61),2))
print('kilometros en millas:',round((kilometros/1.61),2))
