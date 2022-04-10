from pydantic import BaseModel


class CryptoTableBase(BaseModel):
    coin_name: str
    coin_value: float
    date_time: str

    class Config:
        orm_mode = True

class CryptoTableCreate(CryptoTableBase):
    pass


class CryptoTable(CryptoTableBase):
    coin_name: str
    coin_value: float
    date_time: str
