#!/usr/bin/python3
""" script that takes in arguments and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == '__main__':
    # Get the MySQL username, password, and database name
    # from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_name = sys.argv[4]

    # Connect to the MySQL server running on localhost at port 3306
    conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                           passwd=password, db=database)

    # Prepare a parameterized query with a placeholder for the user input
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Execute the parameterized query with the user input as a tuple
    cursor = conn.cursor()
    cursor.execute(query, (searched_name + '%',))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()
