'''Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor'''
'''Escribe un programa en Python que muestre un menú que permita al usuario seleccionar
qué operación desea realizar. Las operaciones que puede realizar serán calcular el área
de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será
similar al siguiente:
1. Calcular el área de un círculo
2. Calcular el área de un triángulo
3. Calcular el área de un rectángulo
4. Salir
Introduce una opción (1-4):
El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4.
Hay que diseñar y definir la siguientes funciones: :
• calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y
retorna su área.
• calcular_area_triangulo: recibe como parámetros de entrada la base y la altura
del triangulo y retorna su área.
• calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura
del rectángulo y retorna su área.
• mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles.
• main(): lee por teclado la opción seleccionada por el usuario, valida que la opción
está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función
correspondiente en función de la opción seleccionada.
• opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre
sea mayor que 0 y una vez que ha validado el radio llamará a la función
calcular_area_circulo.
• opcion2: descripción: lee por teclado el valor de la base y la altura del triángulo,
valida que los dos datos son mayores que 0 y una vez que los ha validado llamará
a la función calcular_area_triangulo.
• opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que
los dos datos son mayores que 0 y una vez que los ha validado llamará a la función
calcular_area_rectangulo'''
import math

# --- FUNCIONES ---

def mostrar_menu():
    print('1. Calcular el área del círculo')
    print('2. Calcular el área de un triángulo')
    print('3. Calcular el área de un rectángulo')
    print('4. Salir')
    print('Introduce una opción (1-4): ')

def calcular_area_circulo(radio):
    return math.pi*pow(radio,2)

def calcular_area_triangulo(base, altura):
    return base*altura/2

def calcular_area_rectangulo(base, altura):
    return base*altura

# --- MAIN ---
eleccion = 0

while (eleccion != 4):
    mostrar_menu()
    eleccion = int(input(''))

    match (eleccion):

        case 1:
            radio = 0
            while (radio <= 0):
                radio = float(input('Introduce el radio: '))

                if radio <= 0:
                    print('No se puede introducir numeros negativos ni 0')
            
            print(f"El area del circulo de radio {radio} es de",calcular_area_circulo(radio))

        case 2:
            base = 0
            altura = 0
            while (base <= 0 or altura <= 0):
                base = float(input('Introduce la base: '))
                altura = float(input('Introduce la altura: '))

                if base <= 0 or altura <= 0:
                    print('No se puede introducir valores negativos ni 0')
            
            print(f"El area del triangulo de base {base} y de altura {altura} es de", calcular_area_triangulo(base,altura))

        case 3:
            base = 0
            altura = 0
            while (base <= 0 or altura <= 0):
                base = float(input('Introduce la base: '))
                altura = float(input('Introduce la altura: '))

                if base <= 0 or altura <= 0:
                    print('No se puede introducir valores negativos ni 0')
            
            print(f"El area del rectangulo de base {base} y de altura {altura} es de", calcular_area_rectangulo(base,altura))
        
        case 4:
            print('Adios!')

        case _:
            print('Numero no valido')



