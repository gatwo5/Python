from os import strerror
import csv

try:
    with open("U5/03_ficheros_csv/ciudades.csv") as fichero:
        reader = csv.DictReader(fichero)
        cabeceras = reader.fieldnames
        print(f"Los nombres de las columnas son {cabeceras}")

        for fila in reader:
            print(f"{fila[cabeceras[0]]} {fila[cabeceras[1]]} tiene una población aproximada de {fila[cabeceras[2]]} millones.")

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)