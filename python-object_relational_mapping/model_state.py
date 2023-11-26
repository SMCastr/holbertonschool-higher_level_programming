#!/usr/bin/python3
"""
Module that contains the class definition of
a State and an instance Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create an instance of the declarative base
Base = declarative_base()


class State(Base):
    """Class definition of a State"""
    __tablename__ = 'states'

    # Column representing an auto-generated, unique integer,
    # can’t be null, and is a primary key
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Column representing a string with maximum 128 characters, can’t be null
    name = Column(String(128), nullable=False)
