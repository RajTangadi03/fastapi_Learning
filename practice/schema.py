from pydantic import BaseModel

class Data(BaseModel):
    name: str
    age: int

class showUserData(Data):
    class Config():
        orm_mode = True
    # This will extend Data class and show its variables

class Cust(BaseModel):
    name:str
    password:str
    email:str
    phoneno:str