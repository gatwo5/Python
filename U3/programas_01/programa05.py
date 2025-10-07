'''Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).'''

# LOCALES

print('Locales:')

a = 3

def locales():
    a = 6
    print(a)

locales()

print(a)

# GLOBALES

print('Globales:')


def globales():
    print(b)

b = 20
globales()

# NO LOCALES

print('No locales: ')

def no_local():
    def sub_no_local():
        print(c)
        return

    c = 40
    sub_no_local()
    print(c)
    return

c = 30
no_local()
print(c)