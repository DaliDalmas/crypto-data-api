from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy import PrimaryKeyConstraint
from database import Base


class CryptoTable(Base):
    __tablename__ = "todays_crypto"
    __table_args__ = (
        PrimaryKeyConstraint('coin_name', 'coin_value', 'date_time'),
    )

    coin_name = Column(String)
    coin_value = Column(Float)
    date_time = Column(DateTime)

