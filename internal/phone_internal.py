import sched
from sqlalchemy.orm import Session

from models import models
from schemas.phone import Phone

def create_phone(db:Session,phone:Phone):
    """Create phone in the DB"""
    phone_db=models.Phones(number=phone.number,name=phone.name)
    db.add(phone_db)
    db.commit()
    db.refresh(phone_db)
    return phone_db

def get_phones(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Phones).offset(skip).limit(limit).all()



def post_me(db:Session,id:int):
    pass

