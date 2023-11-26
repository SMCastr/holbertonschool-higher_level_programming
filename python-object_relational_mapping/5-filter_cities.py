#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to get cities of a specific state
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (sys.argv[4],))

    # Fetch all the rows in a list of lists
    rows = cursor.fetchall()

    # Print elements
    print(", ".join([row[0] for row in rows]))

    # Close cursor object
    cursor.close()

    # Close connection to MySQL server
    db.close()

    # Exit program
    sys.exit(0)
