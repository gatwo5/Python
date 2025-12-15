from os import strerror

try:
    with open("U5/01_ficheros_texto/ficheros/datos.txt", "r") as fichero:
        texto = fichero.read()

        print(texto)

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)