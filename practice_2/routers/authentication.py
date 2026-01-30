from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import model, schema
import jwt_tokens

router = APIRouter(
    prefix="/home/auth",
    tags=["Authentication"]
)

@router.post('/')
def checkAuthentication(msg: schema.auth, db: Session = Depends(get_db)):
    qurs = db.query(model.canteenOwners).filter(model.canteenOwners.name == msg.name).first()
    if not qurs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = jwt_tokens.create_access_token(data={"sub": qurs.name})
    return {"access_token":access_token, "token_type":"bearer"}