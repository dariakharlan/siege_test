from database import Base
from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship


class AnimalType(Base):
    __tablename__ = 'animal_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    deposit_cost = Column(Numeric())
    min_food_cost = Column(Numeric())
    max_food_cost = Column(Numeric())


class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True)
    animal_type_id = Column(Integer, ForeignKey('animal_type.id'))
    name = Column(String(50), unique=True)
    weight = Column(Numeric())
    age = Column(Integer())
    animal_type = relationship('AnimalType', lazy='joined')
