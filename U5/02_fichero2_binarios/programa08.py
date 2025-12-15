import os
from os import strerror

TAM_BLOQUE = 64 * 1024      # 64 KB
AVISO_MB = 1 * 1024 * 1024 # 1 MB

try:
    origen = input("Introduce el archivo de origen: ")
    destino = input("Introduce el archivo de destino: ")

    # Comprobar que el archivo de origen existe
    if not os.path.isfile(origen):
        print("Error: el archivo de origen no existe.")
        exit(1)

    total_bytes = 0
    bytes_desde_aviso = 0

    with open(origen, "rb") as f_origen, open(destino, "wb") as f_destino:

        buffer = bytearray(TAM_BLOQUE)
        leidos = f_origen.readinto(buffer)

        while leidos > 0:
            f_destino.write(buffer[:leidos])

            total_bytes += leidos
            bytes_desde_aviso += leidos

            if bytes_desde_aviso >= AVISO_MB:
                print(f"Copiados {total_bytes} bytes...")
                bytes_desde_aviso = 0

            leidos = f_origen.readinto(buffer)

    print(f"Copia finalizada correctamente.")
    print(f"Total de bytes escritos: {total_bytes}")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
