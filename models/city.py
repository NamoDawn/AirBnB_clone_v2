#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel,  Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """City class handles all application cities"""
    if getenv("HBNB_MYSQL_DB") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship("Place", cascade="all, delete-orphan", 
                              backref="cities")
    else:
        state_id = ""
        name = ""

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
