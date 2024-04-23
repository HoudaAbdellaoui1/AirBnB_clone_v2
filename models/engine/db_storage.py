#!/usr/bin/python3
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine


class DBStorage:
    """This class manages database of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                       pool_pre_ping=True)
        if (getenv('HBNB_ENV')) == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls= None):
        obj_dict = {}
        classes = [BaseModel, User, State, City, Amenity, Place, Review]
        if cls:
            classes = [cls]

        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj

        return obj_dict

    def new(self, obj):
        """Adds an object to the current db session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Save changes to db sessions"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete an object from the current db session if it exists"""
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        """Creates all tables in db + create current db session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        self.__session.close()