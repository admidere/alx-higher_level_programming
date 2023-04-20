#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa
"""

#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the SQL query to fetch all cities
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch all the rows using fetchall() method
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
