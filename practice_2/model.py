from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class canteenOwners(Base):
    __tablename__ = "canteen_Owners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phoneNo = Column(String)
    password = Column(String)
    canteen_id = Column(Integer, ForeignKey("canteens.id", ondelete="CASCADE"))

    canteenOwner = relationship("canteensAndOwners", back_populates="relaCanteenOwner", cascade="all, delete")

class canteens(Base):   
    __tablename__ = "canteens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    canteen = relationship("canteensAndOwners", back_populates="relaCanteen", cascade="all, delete")

class canteensAndOwners(Base):
    __tablename__ = "canteens_And_Owners"

    id = Column(Integer, primary_key=True, autoincrement=True)
    canteen_id = Column(Integer, ForeignKey("canteens.id", ondelete="CASCADE"))
    canteen_owner_id = Column(Integer, ForeignKey("canteen_Owners.id", ondelete="CASCADE"))

    relaCanteenOwner = relationship("canteenOwners", back_populates="canteenOwner", cascade="all, delete")
    relaCanteen = relationship("canteens", back_populates="canteen", cascade="all, delete")
