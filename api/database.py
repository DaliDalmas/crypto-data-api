from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbschema='crypto_data'
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://airflow:airflow@localhost:5432/crypto"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.schema = 'crypto_data'