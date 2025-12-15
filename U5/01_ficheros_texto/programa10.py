from os import strerror

numero_total_lineas = 0
numeo_total_palabras = 0
numero_total_caracteres = 0

try:
    with(open("U5/01_ficheros_texto/ficheros/origen.txt", "r") as origen):

        with(open("U5/01_ficheros_texto/ficheros/copia.txt", "w") as copia):

            for linea in origen:

                #Linea

                copia.write(linea)
                numero_total_lineas += 1

                #Palabras

                frase = linea.strip().split()
                numeo_total_palabras += len(frase)

                #Caracteres

                numero_total_caracteres += len(linea)

    print(f'Numero total de lineas: {numero_total_lineas}')
    print(f'Numero total de palabras: {numeo_total_palabras}')
    print(f'Numero total de caracteres: {numero_total_caracteres}')
    
except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)
