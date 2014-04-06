from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()

class Patch(Base):
    def __init__(self, routeid, typeid, x1, y1, x2, y2):
        self.routeid = routeid
        self.typeid = typeid
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    __tablename__ = 'patches'
    id = Column(Integer, primary_key=True)
    routeid = Column(Integer)
    typeid = Column(Integer)
    x1 = Column(Integer)
    y1 = Column(Integer)
    x2 = Column(Integer)
    y2 = Column(Integer)

