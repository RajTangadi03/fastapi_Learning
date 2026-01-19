from sqlalchemy import Column, Integer, String
from database import Base

class UserData(Base):
    __tablename__ = "User_Data"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class Cust(Base):
    __tablename__ = "Customer_Data"

    id = Column(Integer, primary_key=True)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    phoneno = Column(String)