from os import strerror

datos = bytearray(range(1, 11))

try:
    with open("U5/02_fichero2_binarios/ficheros/datos.bin", "wb") as fichero:
        bytes_escritos = fichero.write(datos)
        print(f"Se escribieron {bytes_escritos} bytes en el archivo datos.bin")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
