from os import strerror


try:
    with open("U5/02_fichero2_binarios/ficheros/datos.bin", "rb") as fichero:
        contenido = fichero.read()

    contenido = bytearray(contenido)

    for e in contenido:
        print(hex(e))

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
