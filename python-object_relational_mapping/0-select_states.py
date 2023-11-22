#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

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

def get_states(username, password, database):
    """
    Retrieve and display all states from the 'states' table
    """
    # Connect to the database
    conn = connect_db(username, password, database)

    # Create a cursor
    cur = conn.cursor()

    # Execute the SELECT query to get all states, ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

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
    # Check if the script is being run directly
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve MySQL username, password, and database from command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to get and print states
    get_states(username, password, database)