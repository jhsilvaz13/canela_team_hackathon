from io import BytesIO
from fastapi import APIRouter,Depends, File,HTTPException

from sqlalchemy.orm import Session

from config.database import SessionLocal

from models import models
from internal import media_internal
from schemas import media as schema
from fastapi import UploadFile


#Dependency of a db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Routers
media=APIRouter()

@media.post("/save_media/")
async def create_phone(file: UploadFile = File(...),db:Session=Depends(get_db)):
    """Return """
    fileSt = await file.read()
    media_internal.create_media(db=db,file=fileSt)


