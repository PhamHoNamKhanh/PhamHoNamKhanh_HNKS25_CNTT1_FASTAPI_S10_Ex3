from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from schemas import InventoryCreate
from user_service import create_inventory

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/inventories", status_code=status.HTTP_201_CREATED)
def create(item: InventoryCreate, db: Session = Depends(get_db)):
    return create_inventory(item, db)