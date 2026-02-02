from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import model, schema
from fastapi.security import OAuth2PasswordRequestForm
import jwt_tokens
from . import oauth2

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/checkAuthentication')
def checkAuthentication(form_data:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db), get_current_user: schema.canteenOwnerData = Depends(oauth2.get_current_user)):
    qurs = db.query(model.canteenOwners).filter(model.canteenOwners.name == form_data.username).first()
    if not qurs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    access_token = jwt_tokens.create_access_token(data={"sub": qurs.name})
    return {"access_token":access_token, "token_type":"bearer"}