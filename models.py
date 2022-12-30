from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

class Dataset(BaseModel):
        file:str