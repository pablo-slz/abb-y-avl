from pydantic import BaseModel

class Pet(BaseModel):
    id:int
    name:str
    age: int
    breed : str
    gender : str