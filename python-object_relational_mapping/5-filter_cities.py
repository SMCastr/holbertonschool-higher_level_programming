#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to get cities of a specific state
    query = """SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC"""

    # Execute the query with state name as an argument
    cursor.execute(query, (sys.argv[4],))

    # Fetch the result
    result = cursor.fetchall()

    # Display the results
    if results:
        for result in results:
            print(result[0])
    else:
        print("Not found")

    # Close cursor and database connection
    cursor.close()
    db.close()
