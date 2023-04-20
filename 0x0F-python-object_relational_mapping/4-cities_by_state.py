#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get the MySQL username, password, and database name
    # from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)

    # Prepare a query to retrieve all cities sorted by id in ascending order
    query = "SELECT * FROM cities ORDER BY id ASC"

    # Execute the query and fetch all the rows returned by the query
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()
