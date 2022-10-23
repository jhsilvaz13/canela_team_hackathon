from config.database import Base

from sqlalchemy import  Column, Integer, String


class Phones(Base):
    """Table Phones to call registered by the user"""
    __tablename__="phones"

    number=Column(Integer, primary_key=True, index=True)
    name=Column(String,nullable=False)