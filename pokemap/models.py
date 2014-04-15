import os

from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    Integer,
    Unicode
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref
    )

from zope.sqlalchemy import ZopeTransactionExtension

import pokedex.db.tables as t

Base = declarative_base()

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

class Patch(Base):
    __tablename__ = 'patches'
    id = Column(Integer, primary_key=True)
    generation_id = Column(Integer)
    location_id = Column(Integer)
    patch_type_id = Column(Integer, ForeignKey('patch_types.id'))
    x1 = Column(Integer)
    y1 = Column(Integer)
    x2 = Column(Integer)
    y2 = Column(Integer)

    def __init__(self,\
                    generation_id,\
                    location_id,\
                    patch_type_id,\
                    x1,\
                    y1,\
                    x2,\
                    y2):
        self.generation_id = generation_id
        self.location_id = location_id
        self.patch_type_id = patch_type_id
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __repr__(self):
        return u'<Patch(x1={0.x1}, y1={0.y1}, x2={0.x2}, y2={0.y2})>'\
                .format(self)

class PatchType(Base):
    __tablename__ = 'patch_types'
    id = Column(Integer, primary_key=True)
    encounter_method_id = Column(Integer)
    name = Column(Unicode(32))

    def __init__(self,\
                    encounter_method_id,\
                    name):
        self.encounter_method_id = encounter_method_id
        self.name = name

Patch.patch_type = relationship(PatchType, lazy='joined')
