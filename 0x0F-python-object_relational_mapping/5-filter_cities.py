#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to fetch all cities in the specified state
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s \
             ORDER BY cities.id ASC"

    cursor.execute(query, (state_name,))

    # Fetch all the rows using fetchall() method
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
