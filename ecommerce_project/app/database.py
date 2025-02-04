import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import environ

env = environ.Env()
environ.Env.read_env()

# Update this to your PostgreSQL database URL
SQLALCHEMY_DATABASE_URL = env("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
