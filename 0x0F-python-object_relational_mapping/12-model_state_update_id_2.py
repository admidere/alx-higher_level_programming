#!/usr/bin/python3
""" Changes the name of a State object from the database hbtn_0e_6_usa """

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

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and updating the name of the state with id=2
    state_to_update = session.query(State).get(2)
    state_to_update.name = 'New Mexico'
    session.commit()

    # Printing the updated state id
    print(state_to_update.id)

    # Closing the session
    session.close()
