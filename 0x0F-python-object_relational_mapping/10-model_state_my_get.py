#!/usr/bin/python3
"""
prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Database configuration
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
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

    # Querying the state with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Printing the result
    if state is not None:
        print(state.id)
    else:
        print("Not found")

    # Closing the session
    session.close()
