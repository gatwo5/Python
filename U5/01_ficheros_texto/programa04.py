from os import strerror

try:
    with(open("U5/01_ficheros_texto/ficheros/saludo.txt", "a") as fichero):
        fichero.write("When I'm away from you\n")
        fichero.write("I'm happier than ever\n")
        fichero.write("Wish I could explain it better\n")
        fichero.write("I wish it wasn't true\n")

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)