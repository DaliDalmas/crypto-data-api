from pydantic import BaseModel
from datetime import datetime

class CryptoTableBase(BaseModel):
    coin_name: str
    coin_value: float
    date_time: datetime

    class Config:
        orm_mode = True

class CryptoTable(CryptoTableBase):
    coin_name: str
    coin_value: float
    date_time: datetime
