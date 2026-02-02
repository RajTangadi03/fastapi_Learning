from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import model, schema
from . import oauth2

router = APIRouter(
    prefix="/home/canteenOwner",
    tags=["Canteen Owner"]
)

@router.get('/')
def showOwners(db: Session = Depends(get_db), get_current_user: schema.canteenOwnerData = Depends(oauth2.get_current_user)):
    qurs = db.query(model.canteenOwners).all()
    return qurs

@router.post('/')
def insertCanteenOwner(msg: schema.canteenOwnerData, db: Session = Depends(get_db), get_current_user: schema.canteenOwnerData = Depends(oauth2.get_current_user)):
    new_canteenOwner = model.canteenOwners(name=msg.name, phoneNo=msg.phoneNo, canteen_id=msg.canteen_id, password=msg.password)
    db.add(new_canteenOwner)
    db.commit()
    db.refresh(new_canteenOwner)
    new_canteenOwnerAndCanteenRelation = model.canteensAndOwners(canteen_id=msg.canteen_id, canteen_owner_id=new_canteenOwner.id)
    db.add(new_canteenOwnerAndCanteenRelation)
    db.commit()
    return new_canteenOwner
