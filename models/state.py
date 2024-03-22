#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
 

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable= False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",backref="states", cascade="all, delete-orphan")             # <-----------------------

    elif getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            from models import storage
            cities_list=[]
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
