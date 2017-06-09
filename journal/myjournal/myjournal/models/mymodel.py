from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base


class Model_Entry(Base):
    __tablename__ = 'entry'
    id = Column(Integer, primary_key=True)
    title  = Column(Unicode)
    text = Column(Unicode)
    date = Column(Unicode)

