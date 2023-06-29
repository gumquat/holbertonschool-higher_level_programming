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

"""
import all classes who inherit from base before calling Base.metadata.create_all(engine)??
"""

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    engine = create_engine(f'mysql://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}', pool_pre_ping=True)

    Base.metadata.create_all(engine)
