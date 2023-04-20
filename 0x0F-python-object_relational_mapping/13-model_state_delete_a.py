#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


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

    # Creates all tables stored in this metadata.
    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying states that contain the letter 'a'
    states = session.query(State).filter(State.name.like('%a%'))

    # Deleting states with 'a'
    for state in states:
        session.delete(state)

    # Committing the changes
    session.commit()

    # Closing the session
    session.close()
