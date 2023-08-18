# these are the sqlalchemy import needed to start working with sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# this is our postgres connection url 
SQLALCHEMY_DATABASE_URL = 'postgresql:// postgres:ima12546@localhost/fastapi'
# engine is the thing that establishes the connections 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#session we know use it to talk to the database now
sessionlocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)
Base = declarative_base()