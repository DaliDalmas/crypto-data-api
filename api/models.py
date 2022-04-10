from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel # helps with validating the data
from datetime import datetime

class Cryptos(BaseModel):
    id:Optional[UUID] = uuid4()
    coin_name:str
    coin_value:float
    date_time:datetime
    