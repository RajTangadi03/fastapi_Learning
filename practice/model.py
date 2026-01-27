from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class UserData(Base):
    __tablename__ = "User_Data"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    user = relationship("UC", back_populates="user", cascade="all, delete")

class Cust(Base):
    __tablename__ = "Customer_Data"

    id = Column(Integer, primary_key=True)
    password = Column(String)
    name = Column(String)
    email = Column(String)
    phoneno = Column(String)

    custm = relationship("UC", back_populates="customer", cascade="all, delete")

class UC(Base):
    __tablename__ = "userCust"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User_Data.id", ondelete="CASCADE"))   
    cust_id = Column(Integer, ForeignKey("Customer_Data.id", ondelete="CASCADE"))

    user = relationship("UserData", back_populates="userCust")
    customer = relationship("Cust", back_populates="userCust")