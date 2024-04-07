#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
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
