#!/usr/bin/python3
"""Defines the City class mapped to the cities table."""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City class mapped to the 'cities' table in the database."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
