#!/usr/bin/python3
"""
Script que lista todos los estados de la base de datos hbtn_0e_0_usa
"""


import MySQLdb
import sys

def connect_db(username, password, database):
    """
    Conectar a la base de datos MySQL
    """
    # Parámetros de conexión a la base de datos
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': username,
        'passwd': password,
        'db': database,
        'charset': 'utf8'
    }

    # Crear una conexión
    conn = MySQLdb.connect(**db_config)

    return conn

def get_states(username, password, database):
    """
    Recuperar y mostrar todos los estados de la tabla 'states'
    """
    # Conectar a la base de datos
    conn = connect_db(username, password, database)

    # Crear un cursor
    cur = conn.cursor()

    # Ejecutar la consulta SELECT para obtener todos los estados, ordenados por id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Obtener todas las filas
    query_rows = cur.fetchall()

    # Imprimir los resultados
    for row in query_rows:
        print(row)

    # Cerrar el cursor y la conexión a la base de datos
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Verificar si el script se está ejecutando directamente
    if len(sys.argv) != 4:
        print("Uso: {} <nombre de usuario> <contraseña> <base de datos>".format(sys.argv[0]))
        sys.exit(1)

    # Obtener el nombre de usuario, la contraseña y la base de datos de MySQL de los argumentos de la línea de comandos
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Llamar a la función para obtener y mostrar los estados
    get_states(username, password, database)