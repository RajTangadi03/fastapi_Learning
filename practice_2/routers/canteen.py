from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import model, schema
from . import oauth2

router = APIRouter(
    prefix="/home/canteen",
    tags=["Canteens"]
)

@router.get('/')
def showCanteens(db: Session = Depends(get_db), get_current_user: schema.canteenOwnerData = Depends(oauth2.get_current_user)):
    qurs = db.query(model.canteens).all()
    return qurs

@router.post('/')
def insertCanteen(msg: schema.canteenData, db: Session = Depends(get_db), get_current_user: schema.canteenOwnerData = Depends(oauth2.get_current_user)):
    new_canteen = model.canteens(name=msg.name)
    db.add(new_canteen)
    db.commit()
    db.refresh(new_canteen)
    return new_canteen