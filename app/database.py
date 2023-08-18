from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define your PostgreSQL connection URL correctly
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:ima12546@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from sqlalchemy.orm import Session as DBSession
def get_db() -> DBSession:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()