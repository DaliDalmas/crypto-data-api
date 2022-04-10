from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Cryptos

app = FastAPI()

db: List[Cryptos] = [
    Cryptos(
        id=uuid4(),
        coin_name="BitCoin",
        coin_value=33000.0,
        date_time='2022-03-01 00:00:00'
    ),
    Cryptos(
        id=uuid4(),
        coin_name="DogeCoin",
        coin_value=300.0,
        date_time='2022-03-10 00:00:00'
    )
]

@app.get('/api/v1/cryptos')
async def fetch_cryptos():
    return db

@app.get('/api/v1/cryptos/stats')
async def fetch_stats():
    return db