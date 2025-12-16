import mysql.connector
from mysql.connector import Error

planetas = [
    ("Tierra", 'Terrestre', 1),
    ("Venus", 'Acido', 3)
]

try:
    # Conexión con la base de datos

    conexion = mysql.connector.connect(
        host='localhost',
        user='planetas',
        password = 'planetas',
        database = 'planetas'
    )

    # Crear tabla

    cursor = conexion.cursor()
    cursor.execute(
        "CREATE TABLE planetas (" \
        "id INT AUTO_INCREMENT PRIMARY KEY," \
        "nombre VARCHAR(100) NOT NULL," \
        "tipo VARCHAR(50)," \
        "lunas INT);"
    )

    # Insertar planetas

    sql = "INSERT INTO planetas (nombre, tipo, lunas) VALUES (%s, %s, %s)"
    cursor.executemany(sql, planetas)

    conexion.commit()

    print(cursor.rowcount, "fila insertada.")

    # Consultar planeta id = 1

    cursor.execute("SELECT * FROM planetas WHERE id = 1")
    resultado = cursor.fetchall()

    print(resultado)

# Gestion de errores

except Error as e:
    print("Error durante la transacción:", e)
    if 'conexion' in locals() and conexion.is_connected():
        conexion.rollback()
        print("Transacción revertida por error")

# Cerrar conexiones y cursor

finally:
    if 'cursor' in locals() and cursor:
        cursor.close()  
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()