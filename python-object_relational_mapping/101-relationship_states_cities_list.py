#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """
    Lists all State objects and corresponding City objects
    from the database hbtn_0e_101_usa
    """

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating an instance of Session class.
    my_session = Session()

    # Querying and printing all State and City objects
    states = my_session.query(State).order_by(State.id).all()

    if not states:
        print("No record")
    else:
        for state in states:
            print("{}: {}".format(state.id, state.name))
            if state.cities:
                for city in state.cities:
                    print("\t{}: {}".format(city.id, city.name))
            else:
                print("\tNo record")

    # Closing session.
    my_session.close()
