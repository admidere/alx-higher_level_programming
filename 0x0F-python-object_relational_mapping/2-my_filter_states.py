#!/usr/bin/python3
"""script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa"""
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

    # Execute a SELECT queryto retrieve all states with a namestarting with 'N'
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'  ORDER \
                 BY id ASC".format(searched_name))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    conn.close()
