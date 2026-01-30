from database import engine, localSession
import schema, model
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, HTTPException, Response

model.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.get('/home/canteenOwner', tags=["Canteen Owner"])
def showOwners(db: Session = Depends(get_db)):
    qurs = db.query(model.canteenOwners).all()
    return qurs

@app.get('/home', tags=["Others"])
def showCanteenAndOwners(db: Session = Depends(get_db)):
    qurs = db.query(model.canteensAndOwners).all()
    return qurs

@app.get('/home/canteen', tags=["Canteens"])
def showCanteens(db: Session = Depends(get_db)):
    qurs = db.query(model.canteens).all()
    return qurs

@app.post('/home/canteenOwner', tags=["Canteen Owner"])
def insertCanteenOwner(msg: schema.canteenOwnerData, db: Session = Depends(get_db)):
    new_canteenOwner = model.canteenOwners(name=msg.name, phoneNo=msg.phoneNo, canteen_id=msg.canteen_id)
    db.add(new_canteenOwner)
    db.commit()
    db.refresh(new_canteenOwner)
    new_canteenOwnerAndCanteenRelation = model.canteensAndOwners(canteen_id=msg.canteen_id, canteen_owner_id=new_canteenOwner.id)
    db.add(new_canteenOwnerAndCanteenRelation)
    db.commit()
    return new_canteenOwner

@app.post('/home/canteen', tags=["Canteens"])
def insertCanteen(msg: schema.canteenData, db: Session = Depends(get_db)):
    new_canteen = model.canteens(name=msg.name)
    db.add(new_canteen)
    db.commit()
    db.refresh(new_canteen)
    return new_canteen