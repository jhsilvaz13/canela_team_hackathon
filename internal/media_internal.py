from io import BytesIO
from sqlalchemy.orm import Session
from fastapi import UploadFile,File
from models import models
from schemas.media import Media

def create_media(db:Session,file: UploadFile = File(...)):
    """Create media file in the DB"""
    media_db=models.Medias(file=BytesIO(file).read())
    db.add(media_db)
    db.commit()
    db.refresh(media_db)
    