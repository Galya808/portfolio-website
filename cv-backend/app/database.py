from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL) # creates a connection to the database

# creates a session - the way of interacting with the DB
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# creates the base class that all other model will inherit from
Base = declarative_base() 