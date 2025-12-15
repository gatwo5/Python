import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='ciudades',
        password = 'ciudades',
        database = 'ciudades'
    )

    # Agregar Madrid

    cursor = conexion.cursor()

    sql = "INSERT INTO ciudades (nombre, pais, poblacion_millones) VALUES ('Madrid', 'España', '6.8')"
    cursor.execute(sql)

    print(cursor.rowcount, "fila insertada.")

    sql = "DELETE FROM ciudades WHERE poblacion_millones < 10"
    cursor.execute(sql)

    print(cursor.rowcount,"fila/s eliminada/s.")

    conexion.commit()

except Error as e:
    print("Error durante la transacción:", e)
    if 'conexion' in locals() and conexion.is_connected():
        conexion.rollback()
        print("Transacción revertida por error")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()  
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
