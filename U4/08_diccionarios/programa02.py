nombre = 'ejemplo'
alumnos = {}


while (nombre != ''):

    nombre = input('Introduzca su nombre: ')

    if (nombre != ''):

        calificacion = int(input('Introduce la calificación: '))

        if(nombre not in alumnos):
            alumnos[nombre] = [calificacion]
        else:
            alumnos[nombre].append(calificacion)

for nombre, calificaciones in alumnos.items():
    media = sum(calificaciones) / len(calificaciones)

    print(f'Nombre: {nombre} | Media: {media}')
