#!/usr/bin/python3
"""A module that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    """The code should not be executed when imported"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states hbtn_0e_0_usa ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
