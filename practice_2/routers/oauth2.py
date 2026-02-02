from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt_tokens

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="checkAuthentication")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return jwt_tokens.verify_token(token, credentials_exception)