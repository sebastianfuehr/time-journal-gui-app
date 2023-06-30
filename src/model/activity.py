from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .orm_base import Base


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project')

    def __init__(self, name):
        self.name = name
