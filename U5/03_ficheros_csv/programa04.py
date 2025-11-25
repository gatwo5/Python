from os import strerror
import csv

cabeceras = ["Ciudad", "País", "Lugar emblemático"]

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    with open("U5/03_ficheros_csv/patrimonios.csv", "w") as fichero:
        writer = csv.DictWriter(fichero, fieldnames=cabeceras, delimiter=";")
        writer.writeheader()
        writer.writerows(patrimonios)
        print("Archivo patrimonios.csv generado correctamente")
except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)