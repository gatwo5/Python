from os import strerror

try:
    with(open("U5/01_ficheros_texto/ficheros/lectura_y_escritura.txt", "r+") as fichero):

        print(fichero.read())

        fichero.write("Archivo actualizado correctamente\n")

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)
