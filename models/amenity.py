#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel,Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
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


#!/usr/bin/python3
""" Review module for the HBNB project """
from models.place import Place
from models.user import User

class Review(BaseModel, Base):
    """ Review class to store review information """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey(Place.id), nullable=False)
        user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
