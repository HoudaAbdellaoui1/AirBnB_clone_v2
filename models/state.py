#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

 
class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable= False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""


    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            l = [
                v for k, v in models.storage.all(models.City).items()
                if v.state_id == self.id
            ]
            return (l)

    def __init__(self, *args, **kwargs):
        """Initialize State object"""
        super().__init__(*args, **kwargs)
