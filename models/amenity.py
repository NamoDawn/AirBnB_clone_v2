#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
# from models.place_amenity import PlaceAmenity


class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    name = Column(String(128), nullable=False)
    __tablename__ = 'amenities'
#    place_amenities = relationship("PlaceAmenity", cascade="all",
#                                   backref="amenities")

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
