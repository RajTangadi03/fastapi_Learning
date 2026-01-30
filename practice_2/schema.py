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
    