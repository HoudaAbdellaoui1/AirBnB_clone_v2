#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity
from os import getenv


class Amenity(BaseModel, Base):
    """ Amenity class to store amenities information """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=True)
        place_amenities =  relationship("Place",
                    secondary=place_amenity,backref = "amenity")
    else:
        name = ""
    
    def __init__(self, *args, **kwargs):
        """initializes amenities"""
        super().__init__(*args, **kwargs)
