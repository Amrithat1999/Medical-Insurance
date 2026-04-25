from sqlalchemy import Integer, Float, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class InsuranceData(Base):
    __tablename__ = "Insurance_Data"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    sex = Column(String)
    bmi = Column(Float)
    children = Column(Integer)
    smoker = Column(String)
    region = Column(String)
    charges = Column(Float)


# from sqlalchemy import Column, Integer, Float, String
# from db_config import Base

# class InsuranceData(Base):
#     __tablename__ = "insurance_data"

#     id = Column(Integer, primary_key=True, index=True)
#     age = Column(Integer)
#     sex = Column(String)
#     bmi = Column(Float)
#     children = Column(Integer)
#     smoker = Column(String)
#     region = Column(String)
#     charges = Column(Float)
    