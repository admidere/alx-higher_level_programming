#!/usr/bin/python3
""" Module that defines the City class """

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    """ Definition of the City class """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
