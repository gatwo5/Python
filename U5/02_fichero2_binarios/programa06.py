from os import strerror
# Solicita al usuario el nombre del archivo fuente
nombre_fichero_origen = input("Ingresa el nombre del archivo fuente: ")
# Solicita al usuario el nombre del archivo destino
nombre_fichero_destino = input("Ingresa el nombre del archivo destino: ")
# Prepara un búfer de 64 kilobytes
buffer = bytearray(65536)
total = 0
# Copia los datos del archivo fuente al archivo destino usando context managers
try:
    with open(nombre_fichero_origen, 'rb') as fichero_origen, \
        open(nombre_fichero_destino, 'wb') as fichero_destino:

        bytes_leidos = fichero_origen.readinto(buffer)

        while bytes_leidos > 0:

            bytes_escritos = fichero_destino.write(buffer[:bytes_leidos])
            total += bytes_escritos
            bytes_leidos = fichero_origen.readinto(buffer)
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
# Imprime el número total de bytes escritos
print(total, 'byte(s) escritos con éxito')