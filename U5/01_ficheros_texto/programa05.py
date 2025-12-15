from os import strerror

nombres = ["Ana", "Pedro", "Lucia", "Eva"]

try:
    with(open("U5/01_ficheros_texto/ficheros/alumnos.txt", "w") as fichero):

        for nombre in nombres:

            fichero.write(f'{nombre}\n')

    with(open("U5/01_ficheros_texto/ficheros/alumnos.txt", "r") as fichero):

        print(fichero.read().upper())

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)