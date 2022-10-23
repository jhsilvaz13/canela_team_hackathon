from types import TracebackType
from config.database import Base
from sqlalchemy import  Column, Integer, LargeBinary, String


class Phones(Base):
    """Table Phones to call registered by the user"""
    __tablename__="phones"

    number=Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)

class Medias(Base):
    """Table Media to the multimedias files regiterd on alert mode"""
    __tablename__="medias"

    #id=Column(Integer,primary_key=True,index=True)
    file=Column(LargeBinary,primary_key=True)
