#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to get cities with state information
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
