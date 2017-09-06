#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """State class handles all application states"""

    if 'HBNB_TYPE_STORAGE' in environ and environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """getter method cities returns list of City objects"""
            city_list = models.storage.all("City").values()
            filtered_list = []
            for item in city_list:
                if city.state_id is self.id:
                    filtered_list.append(city)
            return city_list

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
