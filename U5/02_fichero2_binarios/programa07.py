from os import strerror

datos = bytearray(10)

for i in range(len(datos)):
    datos[i] = 10 + i
try:
    with open("file.bin", "wb") as fichero_binario:
        fichero_binario.write(datos)
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))