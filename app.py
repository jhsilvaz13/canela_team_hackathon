from fastapi import FastAPI

from models import models
from config.database import engine
from routers.phone import phone
from routers.media import media
import uvicorn

app=FastAPI()
app.include_router(phone)
app.include_router(media)

#Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return("The server is running")
