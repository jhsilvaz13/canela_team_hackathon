from fastapi import FastAPI

from models import models
from config.database import engine
from routers.phone import phone

import uvicorn

app=FastAPI()
app.include_router(phone)

#Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return("The server is running")
