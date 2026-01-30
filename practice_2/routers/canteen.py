from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import model, schema

router = APIRouter()

@router.get('/home/canteen', tags=["Canteens"])
def showCanteens(db: Session = Depends(get_db)):
    qurs = db.query(model.canteens).all()
    return qurs

@router.post('/home/canteen', tags=["Canteens"])
def insertCanteen(msg: schema.canteenData, db: Session = Depends(get_db)):
    new_canteen = model.canteens(name=msg.name)
    db.add(new_canteen)
    db.commit()
    db.refresh(new_canteen)
    return new_canteen