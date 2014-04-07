from sqlalchemy import (
    Column,
    Integer,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Patch(Base):
    __tablename__ = 'patches'
    id = Column(Integer, primary_key=True)
    genid = Column(Integer)
    routeid = Column(Integer)
    typeid = Column(Integer)
    x1 = Column(Integer)
    y1 = Column(Integer)
    x2 = Column(Integer)
    y2 = Column(Integer)

    def __init__(self, genid, routeid, typeid, x1, y1, x2, y2):
        self.genid = genid
        self.routeid = routeid
        self.typeid = typeid
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
