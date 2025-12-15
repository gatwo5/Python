from os import strerror

byte_array = bytearray(10)

try:
    with open("U5/02_fichero2_binarios/ficheros/datos.bin", "rb") as fichero:
        numero_bytes_leidos = fichero.readinto(byte_array)

        for b in byte_array:
            print(hex(b), end=' ')
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)