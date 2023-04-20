#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_14_usa """
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    # Database configuration
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306

    # Engine creation
    engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'
                           .format(mysql_username, mysql_password,
                                   host, port, database_name),
                           pool_pre_ping=True)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all City objects sorted by id
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id.asc()):
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
