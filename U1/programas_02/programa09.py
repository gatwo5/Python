'''
Escribe un programa que calcule la calificación de estudiante en un módulo. La
calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3
20%)
'''
ra1 = float(input('Introduce la nota del RA1: '))
ra2 = float(input('Introduce la nota del RA2: '))
ra3 = float(input('Introduce la nota del RA3: '))
print('La nota total es de ',((ra1 * 0.20)) + (ra2 * 0.60) + (ra3 * 0.20))