import matematicas.operaciones, matematicas.figuras, matematicas.conversiones

def main():
    eleccion = int(input('1: Operaciones\n2: Areas\n3: Conversiones: '))
    eleccion2 = 0
    num1 = 0
    num2 = 0

    match eleccion:
        case 1:
            num1 = float(input('Introduce num1 '))
            num2 = float(input('Introduce num2 '))

            print('suma:',matematicas.operaciones.suma(num1,num2))
            print('Resta:',matematicas.operaciones.resta(num1,num2))
            print('Multiplicacion:',matematicas.operaciones.multiplicacion(num1,num2))
            print('Division:',matematicas.operaciones.division(num1,num2))
        case 2:
            eleccion2 = int(input('1: Area rectangulo\n2: Area triangulo\n3: Area circulo'))
            match eleccion2:
                case 1:
                    num1 = float(input('Introduce la base: '))
                    num2 = float(input('Introduce la altura: '))

                    print(matematicas.figuras.area_rectangulo(num1,num2))
                case 2:
                    num1 = float(input('Introduce la base: '))
                    num2 = float(input('Introduce la altura: '))

                    print(matematicas.figuras.area_triangulo(num1,num2))
                case 3:
                    num1 = float(input('Introduce el radio: '))
                    print(matematicas.figuras.area_circulo(num1))
                case _:
                    print('Numero no valido')
        case 3:
            eleccion2 = int(input('1: Binario\n2: Hexadecimal\n3: Circulo: '))

            match eleccion2:
                case 1:
                    num1 = int(input('Introduce numero: '))
                    print(matematicas.conversiones.a_binario(num1))
                case 2:
                    num1 = int(input('Introduce numero: '))
                    print(matematicas.conversiones.a_hexadecimal(num1))
                case 3:
                    num1 = int(input('Introduce texto: '))
                    print(matematicas.conversiones.a_entero(num1))
                case _:
                    print('Numero no valido')
        case _:
            print('Numero no valido')
if __name__ == "__main__":
    main()