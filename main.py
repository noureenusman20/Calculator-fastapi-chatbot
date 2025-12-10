from fastapi import FastAPI
from database import engine, Base
from endpoints import router as calc_router
import models

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(calc_router)