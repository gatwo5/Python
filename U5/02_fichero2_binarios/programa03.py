from os import strerror

try:
    with open("U5/02_fichero2_binarios/ficheros/20bytes.bin", "rb") as fichero:

        datos = 's'

        while (datos):
            datos = fichero.read(5)
            byte_data = bytearray(datos)

            for b in byte_data:
                print(hex(b), end=' ')
            
            print()

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
