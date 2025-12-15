from os import strerror

contador_caracteres = 0

try:
    with(open("U5/01_ficheros_texto/ficheros/texto.txt", "r") as fichero):
        c = fichero.read(1)

        while c:
            print(c, end="")
            c = fichero.read(1)
            contador_caracteres += 1
            
    print(f'\nTotal de caracteres: {contador_caracteres}')

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)