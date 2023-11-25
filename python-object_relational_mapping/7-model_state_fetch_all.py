#!/usr/bin/python3
"""This module lists all State objects from
the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an SQLAlchemy Engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
                           pool_pre_ping=True)

    # Create an SQLAlchemy ORM session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and display the results
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
