from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import model

router = APIRouter(
    prefix="/home",
    tags=["Others"]
)

@router.get('/')
def showCanteenAndOwners(db: Session = Depends(get_db)):
    qurs = db.query(model.canteensAndOwners).all()
    return qurs
