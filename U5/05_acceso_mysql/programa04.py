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

    cursor.execute("SELECT * FROM ciudades WHERE poblacion_millones > 25")

    resultado = cursor.fetchall()

    for ciudad in resultado:
        print(f'{ciudad[1]}, que se encuentra en {ciudad[2]} tiene una poblacion de {ciudad[3]}')

except Error as e:
    print(f'Error con MySQL: {e}')