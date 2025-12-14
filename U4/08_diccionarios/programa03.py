agenda = {
    'michael': 666333222,
    'eddy': 616989121,
    'dani': 666555444
}

# =====================

def agregar_contacto():
    nombre = input('Introduce el nombre: ')
    numero = int(input('Introduce el numero de telefono: '))
    agenda[nombre] = numero

def modificar_contacto():
    antiguo_nombre = input('Introduce el nombre del contacto a modificar: ')

    if(antiguo_nombre in agenda):
        nuevo_nombre = input('Introduce el nuevo nombre: ')
        agenda[nuevo_nombre] = agenda.pop(antiguo_nombre)
    else:
        print("No existe")


def eliminar_contacto():
    nombre = input('Introduce el nombre del contacto a eliminar: ')

    if(nombre in agenda):
        agenda.pop(nombre)
    else:
        print('No existe')

def mostrar_contactos():
    agenda_ordenada = sorted(agenda)
    print(agenda_ordenada)

def buscar_contacto():
    nombre = input("Introduce su nombre: ")

    if (nombre in agenda):
        print('Su numero es', agenda[nombre])
    else:
        print('No existe')

def imprimir_menu():
    print("1: Agregar contacto\n2: Modificar contacto\n3: Eliminar contacto\n4: Mostrar agenda ordenada\n5: Buscar contacto:")

# =====================

eleccion = 1

while (eleccion > 0 and eleccion < 6):
    imprimir_menu()
    eleccion = int(input())

    match eleccion:
        case 1:
            agregar_contacto()
        case 2:
            modificar_contacto()
        case 3:
            eliminar_contacto()
        case 4:
            mostrar_contactos()
        case 5:
            buscar_contacto()



