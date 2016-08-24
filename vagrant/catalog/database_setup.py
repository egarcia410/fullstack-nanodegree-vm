##Configuration Code
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

## Class Definitions
class Restaurant(Base):
    ## Table Information
    __tablename__ = 'restaurant'
    ## Mappers
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }

## Class Definitions
class MenuItem(Base):
    ## Table Information
    __tablename__ = 'menu_item'
    ## Mappers
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        ## Returns object data in easily serialized format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }



####### Insert at end of file #######

engine = create_engine(
    'sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
