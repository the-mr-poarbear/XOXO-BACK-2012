from typing import Union
from pydantic import BaseModel



class User(BaseModel):
    name : str 
    score : int

class Result(BaseModel):
    name: str
    status : str
    