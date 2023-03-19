#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """Defines a new class City
    Args:
        __tablename__: table name in a database
        id: represents an id in a table(city)
        name: represents a column in a table(city)
        state_id: represent a column in a table(city)
                  and is a foreign key to states.id
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
