from pydantic import BaseModel

class Phone(BaseModel):
    number: int
    name:str

    class Config:
        orm_mode = True