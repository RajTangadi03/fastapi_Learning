from fastapi import FastAPI, Depends, status, HTTPException, Response
from database import engine, localSession
import schema, model
from sqlalchemy.orm import Session

model.Base.metadata.create_all(engine)

app = FastAPI()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.post('/home', tags=["User"])
def tupleInsertion(msg: schema.Data, db: Session = Depends(get_db), status_code = status.HTTP_201_CREATED):
    new_student = model.UserData(name=msg.name, age=msg.age)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)   
    return new_student

@app.get('/home', tags=["User"])
def showAll(db: Session = Depends(get_db)):
    qurs = db.query(model.UserData).all()
    return qurs

@app.get('/home/{id}', tags=["User"])
def showOne(id, db: Session = Depends(get_db), response = Response):
    qurs = db.query(model.UserData).filter(model.UserData.id == id).first()
    if not qurs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User having id: {id} is not available.")

    return qurs

@app.delete('/home/delete/{id}', tags=["User"])
def deleteTuple(id, db: Session = Depends(get_db)):
    db.query(model.UserData).filter(model.UserData.id == id).delete(synchronize_session=False)
    db.commit()
    return f'User having id: {id} have been deleted.'

@app.put('/home/update/{id}', tags=["User"])
def update(id, details: schema.Data, db: Session = Depends(get_db)):
    db.query(model.UserData).filter(model.UserData.id == id).update({'age' : details.age}, synchronize_session=False)
    db.commit()
    return f'User having id: {id} is updated his age: {details.age}'


@app.get('/home/titleAge/{id}', response_model=schema.showUserData, tags=["User"])
def getOnlyTitleAge(id, db: Session = Depends(get_db)):
    user = db.query(model.UserData).filter(model.UserData.id == id).first()
    if not user:
        return f'User with id: {id} is not found.'
    return user


# ------------------------------------------------------------------------------------------------------------
# Creating customer requests
# ------------------------------------------------------------------------------------------------------------

@app.put('/home/cust/{id}', tags=["Customer"])
def updateCust(id, detail: schema.Cust, db: Session = Depends(get_db)):
    db.query(schema.Cust).filter(schema.Cust.id == id).update({'password' : detail.password}, synchronize_session=False)
    db.commit()
    return 'Updated'

@app.post('/home/cust', tags=["Customer"])
def createUser( detail: schema.Cust, db: Session = Depends(get_db)):
    new_cust = model.Cust(name=detail.name, password = detail.password, email=detail.email, phoneno=detail.phoneno)
    db.add(new_cust)
    db.commit()
    db.refresh(new_cust)
    return new_cust
