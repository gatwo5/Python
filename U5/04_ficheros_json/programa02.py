from os import strerror
import json

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
]

try:
    with open("U5/04_ficheros_json/capitales.json", "w") as fichero:
        json.dump(capitales, fichero, ensure_ascii=False, indent=4)
        print("Archivo 'capitales.json' creado correctamente.")
except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)