#!/usr/bin/python3
"""
python file
contains class def of a state and an instance:
Base = declarative_base()
State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated, unique integer, cant be null and is a primary key
class attribute name that represents a column of a string with maximum 128 characters and cant be null
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import sys


Base = declarative_base()


class State(Base):
    """
    state class
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
