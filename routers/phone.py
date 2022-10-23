from fastapi import APIRouter,Depends,HTTPException

from sqlalchemy.orm import Session

from config.database import SessionLocal

from models import models
from internal import phone_internal
from schemas import phone as schema

# Dependency of a db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Routers  
phone=APIRouter()

@phone.post("/phones/", response_model=schema.Phone)
async def create_phone(phone:schema.Phone,db:Session=Depends(get_db)):
    """"""
    return phone_internal.create_phone(db=db,phone=phone)

@phone.get("/phones/")
async def get_phones(skip:int=0, limit:int=100,db:Session=Depends(get_db)):
    """"""
    return phone_internal.get_phones(db, skip, limit)

