import sys
import json

my_settings = open('../my_settings.json')
settings = json.load(my_settings)
sys.path.append(settings["BASE_PATH"])

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/all_cryptos/", response_model=list[schemas.CryptoTable])
def read_cryptos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cryptos = crud.get_cryptos(db, skip=skip, limit=limit)
    return cryptos
