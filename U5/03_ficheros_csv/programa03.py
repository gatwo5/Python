from os import strerror
import csv

cabeceras = ["Ciudad", "País", "Continente"]

data = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"]
]

try:
    with open("U5/03_ficheros_csv/capitales.csv", "w") as fichero:
        writer = csv.writer(fichero)
        writer.writerow(cabeceras)
        writer.writerows(data)

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)
