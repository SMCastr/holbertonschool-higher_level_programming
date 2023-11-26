#!/usr/bin/python3
"""This module filters and prints the states
starting with n from the database"""


import MySQLdb
import sys


def connect_db(username, password, database):
    """
    Connect to the MySQL database
    """
    # Database connection parameters
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'user': username,
        'passwd': password,
        'db': database,
        'charset': 'utf8'
    }

    # Create a connection
    conn = MySQLdb.connect(**db_config)

    return conn


def filter_states_starting_with_n(username, password, database):
    """
    Retrieve and display all states with
    a name starting with n from the 'states' table
    """
    # Connect to the database
    conn = connect_db(username, password, database)

    # Create a cursor
    cur = conn.cursor()

    # Execute the SELECT query to get states starting with n, ordered by id
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    query_rows = cur.fetchall()

    # Print the results
    for row in query_rows:
        print(row)


    # Close the cursor and the database connection
    cur.close()
    conn.close()


if __name__ == "__main__":


    # Check if the script is being run directly
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".
              format(sys.argv[0]))
