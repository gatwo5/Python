from os import strerror

nombre_fichero = input("Introduce el nombre del fichero (sin .txt): ")

try:
    #Abrir el fichero a leer

    with(open(f"examen/2ev/RA5/ficheros/{nombre_fichero}.txt", "r") as fichero):
        fichero_completo = ''

        #Leer el fichero línea por línea y pasar a mayúsculas para tratar todas las letras por igual

        for linea in fichero:
            fichero_completo += linea
        
        fichero_completo = fichero_completo.upper()

        # Crea el diccionario

        # Clave: letra
        # Valor: count(letra)
        # Y por cada letra creara un par de Clave valor
        #Ejemplo: {A: 4, B: 3, ...}

        frecuencia = {letra: fichero_completo.count(letra) for letra in fichero_completo if letra not in (' ', '\n', ',', "'")}

    print(frecuencia)

    #Abrir el fichero donde se escribirá el resultado final

    with(open(f"examen/2ev/RA5/ficheros/{nombre_fichero}.hist", "w") as fichero):

        # Escribe cada par de Clave: valor del diccionario

        for key, value in frecuencia.items():

            fichero.write(f'{key}: {value}\n')

# Gestión de errores
except IOError as e:
    print("Error durante la operacion de archivos:", strerror(e.errno))
    exit(e.errno)
