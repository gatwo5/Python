'''Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta'''
dia = int(input('Introduce el dia '))
mes = int(input('Introduce el mes '))
anno = int(input('Introduce el año '))
esValida = ((dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12))


if (esValida):
    match mes:
        case 4 | 6 | 9 | 11:
            if (dia == 31):
                esValida = False
        case 2:
            if (anno % 4 == 0) and (anno % 100 != 0 or anno % 400 == 0):
                if (dia > 29):
                    esValida = False
            else:
                if (dia > 28):
                    esValida = False

if (esValida):
    print('La fecha es valida')
else:
    print('La fecha no es valida')