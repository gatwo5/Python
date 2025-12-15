from os import strerror

try:
    with(open("U5/01_ficheros_texto/ficheros/datos.txt", "r") as fichero):
        
        for i in range(1,3):
            print(fichero.readline())

        fichero.seek(0)

        for i in range(1,3):
            print(fichero.readline())

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)
