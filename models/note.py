from pydantic import BaseModel
from typing import Optional
class Note(BaseModel):
    title:str
    desc:str
    important:Optional[bool]=True