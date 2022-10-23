from encodings.utf_8 import encode
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

@media.patch("/save_media/")
async def create_media(file: UploadFile = File(...),db:Session=Depends(get_db)):
    """Endpoint para guardar un archivo"""
    fileSt = await file.read()
    return media_internal.create_media(db=db,fileS=fileSt)

@media.get("/save_media/")
async def get_medias(skip:int=0, limit:int=100,db:Session=Depends(get_db)):
    """"""
    return media_internal.get_medias(db, skip, limit)


