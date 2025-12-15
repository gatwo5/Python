from os import strerror

try:
    with open("inexistente.txt", "r") as fichero:

        print(fichero.read())

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)
