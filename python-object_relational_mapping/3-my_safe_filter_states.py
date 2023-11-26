#!/usr/bin/python3
"""This module makes a MySQL query using MySQLdb."""


import MySQLdb
import sys


if __name__ == "__main__":
    """This conditional ensures main() function is called when script is run
    directly and not called when imported as a module.
    """

    # Connecting to a MySQL database.
    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    # Making cursor obj for execution.
    cur = cnx.cursor()

    # Executing query with safe parameterization to prevent SQL injection.
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv[4],))

    # Obtaining query results.
    query_rows = cur.fetchall()

    # Printing results.
    for row in query_rows:
        print(row)

    # Close cursor.
    cur.close()

    # Close connection to database.
    cnx.close()
