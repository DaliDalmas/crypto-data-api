from sqlalchemy.orm import Session

import models


def get_cryptos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CryptoTable).offset(skip).limit(limit).all()
