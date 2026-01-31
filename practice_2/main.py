from routers import others, canteen, canteenOwner, authentication
from database import engine
import model
from fastapi import FastAPI

model.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(others.router)
app.include_router(canteen.router)
app.include_router(canteenOwner.router)