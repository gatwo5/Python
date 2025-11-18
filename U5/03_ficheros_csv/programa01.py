from os import strerror
import csv

try:
    with open("U5/03_ficheros_csv/ciudades.csv") as fichero:
        reader = csv.reader(fichero, delimiter=",")
        cabecera = next(reader)
        print(f"Los nombres de las columnas son {", ".join(cabecera)}")

        for fila in reader:
            print(f"{fila[0]} {fila[1]} tiene una población aproximada de {fila[2]} millones.")

except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)