#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_101_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
import sys

if __name__ == '__main__':
    """Command line arguments"""

    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(mysql_username, mysql_passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
