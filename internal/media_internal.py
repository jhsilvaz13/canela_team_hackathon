from base64 import encode
from io import BytesIO
from sqlalchemy.orm import Session
from fastapi import UploadFile,File
from models import models
from schemas.media import Media

def create_media(db:Session,fileS: UploadFile = File(...)):
    """Crear un registro en la BD de cualquier tipo de archivo que el usuario haya grabado
    retorna el registro que se realizó"""
    media_db=models.Medias(file=BytesIO(fileS).read())
    db.add(media_db)
    db.commit()
    db.refresh(media_db)
    return "Archivo almacenado"

def get_medias(db:Session,skip:int=0,limit:int=100):
    db.query(models.Medias).offset(skip).limit(limit).all()
