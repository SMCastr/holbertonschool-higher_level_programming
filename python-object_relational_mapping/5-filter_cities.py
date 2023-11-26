#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def print_cities(cities):
    """
    Prints cities with proper formatting.
    """
    print(", ".join(city[1] for city in cities))


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))


    # Connect to a MySQL database based on command line arguments
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to get cities of a specific state
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query with state name as an argument
    try:
        cursor.execute(query, (sys.argv[4],))
        result = cursor.fetchall()

        # Display the results
        if result:
            print_cities(result)
        else:
            print("Not found")
    except MySQLdb.Error as e:
        print("Error executing the query:", e)

    # Close cursor and database connection
    cursor.close()
    db.close()
