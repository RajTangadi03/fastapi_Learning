from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import model, schema
from . import oauth2

router = APIRouter(
    prefix="/home",
    tags=["Others"]
)

@router.get('/')
def showCanteenAndOwners(db: Session = Depends(get_db), get_current_user: schema.canteenOwnerData = Depends(oauth2.get_current_user)):
    qurs = db.query(model.canteensAndOwners).all()
    return qurs
