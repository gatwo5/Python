from os import strerror

nombre_fichero = input("Introduce el nombre del fichero (sin .txt): ")

try:
    with(open(f"U5/01_ficheros_texto/ficheros/{nombre_fichero}.txt", "r") as fichero):

        fichero_completo = fichero.read().upper()

        frecuencia = {letra: fichero_completo.count(letra) for letra in fichero_completo if letra not in (' ', '\n', ',', "'")}

    # Ordenar por valor

    frecuencia = {k: v for k, v in sorted(frecuencia.items(), key=lambda item: item[1], reverse = True)}
    print(frecuencia)

    with(open(f"U5/01_ficheros_texto/ficheros/{nombre_fichero}.hist", "w") as fichero):

        for key, value in frecuencia.items():

            fichero.write(f'{key}: {value}\n')

    

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)
