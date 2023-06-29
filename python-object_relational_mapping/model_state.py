"""
python file: contains a class definition of state and an instance of Base = declarative_base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_03_5_usa')
    
    Base.metadata.create_all(engine)
