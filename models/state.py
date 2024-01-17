#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os




class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    #state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    
    if  os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', back_populates='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """getter attributes
            """
            from models import storage
            cities_dict = storage.all(City)
            cities_list = []
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

