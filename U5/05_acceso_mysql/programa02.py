import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='ciudades',
        password = 'ciudades',
        database = 'ciudades'
    )

    cursor = conexion.cursor()
    cursor.execute(
        "CREATE TABLE ciudades (" \
        "id INT AUTO_INCREMENT PRIMARY KEY, " \
        "nombre VARCHAR(100) NOT NULL, " \
        "pais VARCHAR(50), " \
        "poblacion_millones FLOAT);"
    )

    cursor.close()
    conexion.close()

    print('Tabla creada correctamente')

except Error as e:
    print(f'Error con MySQL: {e}')