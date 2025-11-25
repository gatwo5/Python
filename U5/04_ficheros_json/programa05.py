from os import strerror
import json

continente = input("Introduce un continente: ")

try:
    with open("U5/04_ficheros_json/paises.json", "r", encoding="utf-8") as fichero_lectura:
        datos = json.load(fichero_lectura)
        with open("U5/04_ficheros_json/paises_filtrados.json", "w") as fichero_escritura:

            for dato in datos:
                if (dato['continente'] == continente):
                    print(f"{dato['nombre']} está en {dato['continente']}")
                    json.dump(dato, fichero_escritura, ensure_ascii=False, indent=4)

            print("Fichero paises_filtrados creado correctamente")

except IOError as e:
    print("Error durante la operación de archivos:", strerror(e.errno))
    exit(e.errno)