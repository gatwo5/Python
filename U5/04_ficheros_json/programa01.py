from os import strerror
import json

try:
    with open("U5/04_ficheros_json/paises.json", "r", encoding="utf-8") as fichero:
        datos = json.load(fichero)
        
        for dato in datos:
            print(f"{dato['nombre']} está en {dato['continente']} y tiene {dato['poblacion']} millones de habitantes")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)