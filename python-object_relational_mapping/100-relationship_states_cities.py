#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco”"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    """Create California with San Francisco"""
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Connecting to a MySQL database.
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    # Creating tables in the database.
    Base.metadata.create_all(engine)

    # Creating a premade "Session" class.
    Session = sessionmaker(bind=engine)

    # Creating an instance of Session class.
    my_session = Session()

    # Creating California with San Francisco
    new_state = State(name='California', cities=[City(name='San Francisco')])
    
    # Adding the new state to the session
    my_session.add(new_state)
    
    # Committing the session
    my_session.commit()

    # Closing session.
    my_session.close()
