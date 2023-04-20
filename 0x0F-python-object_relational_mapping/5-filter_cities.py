#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """ The code should not be executed when imported"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name)
    cur = db.cursor()

    cur.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') from states, \
                 cities WHERE states.id = cities.state_id AND states.name = \
                 '{}' ORDER BY cities.id ASC".format(state_name))

    result = cur.fetchone()[0]  # Extracting the first element of the tuple
    if result is not None:
        print(result)
    else:
        print()

    cur.close()
    db.close()
