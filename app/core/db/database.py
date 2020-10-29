from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from pydantic import PostgresDsn

import os


SQLALCHEMY_DATABASE_URL = PostgresDsn.build(
    scheme="postgresql",
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    path=f'/{os.getenv("POSTGRES_DB")}'
)


class Database:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()


Base = declarative_base()
