
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:12345678@localhost:5432/Amritha_db"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit= False, autoflush = False, bind = engine)

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/Amritha_db"

# engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base = declarative_base()