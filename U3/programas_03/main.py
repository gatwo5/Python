import operaciones

def main():
    num1 = float(input('Introduce num1 '))
    num2 = float(input('Introduce num2 '))

    print('suma:',operaciones.suma(num1,num2))
    print('Resta:',operaciones.resta(num1,num2))
    print('Multiplicacion:',operaciones.multiplicacion(num1,num2))
    print('Division:',operaciones.division(num1,num2))

if __name__ == "__main__":
    main()
    