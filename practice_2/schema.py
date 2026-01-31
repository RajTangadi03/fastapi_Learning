from pydantic import BaseModel

class canteenOwnerData(BaseModel):
    name: str
    phoneNo: str
    canteen_id: int

class canteenData(BaseModel):
    name: str

class canteensAndOwners(BaseModel):
    canteen_id: int
    canteen_owner_id: int
    
class auth(BaseModel):
    name: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []