#!/usr/bin/python3
"""This module lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Set up the connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database
    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Display the results
    for state in query.all():
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
