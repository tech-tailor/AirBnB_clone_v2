#!/usr/bin/python3
""" db storage
""" 

from sqlalchemy import create_engine
import os
from models.base_model import Base
from models import base_model
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = self.__create_engine()
        if os.getenv('HBNB_ENV') == 'test':
            self.Base.metadata.drop_all(self.__engine)
         
    def __create_engine(self):
        """ create sqlalchemy engine"""
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        database = os.getenv('HBNB_MYSQL_DB')

        db_url = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
        engine = create_engine(db_url, pool_pre_ping=True)
        return engine
    
    def all(self, cls=None):
        class_to_query = []
        result = []
        if cls == None:
            class_to_query = [
                base_model.User,
                base_model.State,
                base_model.City,
                base_model.Amenity,
                base_model.Place,
                base_model.Review
            ]
        else:
            class_to_query.append(cls)

        for class_obj in class_to_query:
            objects = self.__session.query(class_obj).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        return obj
    
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    def reload(self):
        """create database session"""
        from models import base_model

        base_model.Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        """close the session"""
        self.__session.remove()
