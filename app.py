from fastapi import FastAPI

from models import models
from config.database import engine
from routers.phone import phone
from routers.media import media
import uvicorn



from fastapi.middleware.cors import CORSMiddleware


origins = ["*"]

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(phone)
app.include_router(media)

#Create tables
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def home():
    return("The server is running")
