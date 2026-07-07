from fastapi import FastAPI,Depends
from Lythuyet import get_db,Base,engine
from sqlalchemy.orm import Session10
import Models
Base.metadata.create_all(bind= engine)
app = FastAPI()

@app.get ("/")
async def home(db: Session10 = Depends(get_db)):
    print(db)
    return {"Message": "Đây là dữ liệu trang home"}


@app.post("/Users")
async def create(user_new : CreateUserRequest,db:Session10 = Depends(get_db))