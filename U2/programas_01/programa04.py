nota = float(input('Introduce tu nota '))

match nota:
    case nota if (0 <= nota < 5):
        print('Insuficiente')
    case nota if (5 <= nota < 6):
        print('Suficiente')
    case nota if (6 <= nota < 7):
        print('Bien')
    case nota if (7 <= nota < 9):
        print('Notable')
    case nota if (9 <= nota <= 10):
        print('Sobresaliente')
    case _:
        print('Numero no valido')