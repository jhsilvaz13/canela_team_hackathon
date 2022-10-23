import base64
from pydantic import BaseModel
from fastapi import UploadFile

class Media(BaseModel):
    file:UploadFile

    class Config:
        orm_mode = True