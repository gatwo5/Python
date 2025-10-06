'''Escribe un programa que realice las siguientes operaciones:
• Leer por teclado un número comprendido entre 1 y 10. Se vuelve a pedir hasta que
no se introduzca el número correcto.
• Una vez que ha leído el número se tiene que mostrar su tabla de multiplicar.
• Después de mostrar la tabla de multiplicar se tiene que preguntar al usuario si
desea introducir otro número o no. Si el usuario selecciona que quiere continuar el
programa tendrá que volver a ejecutarse y repetir los mismos pasos. Si el usuario
indica que no quiere continuar el programa finaliza'''

continuar = True

while (continuar):
    num = 0

    while (num < 1 or num > 10):
        num = int(input('Introduce un numero del 1 al 10: '))

    for x in range(1,11):
        print(f"{num} x {x} =",num*x)

    continuar = input('Repetir proceso? (s/n): ').lower().startswith('s')