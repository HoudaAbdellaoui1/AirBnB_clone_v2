#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
 

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable= False)
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            from models import storage
            cities_list=[]
            for city in storage.all(models.City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
