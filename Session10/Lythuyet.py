from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

SQLAlCHEMY_DATABASE_URL = "mysql+pymysql://root/:Khanh2007@127.0.0.1:3306/db_quan_ly_sinh_vien"
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush = False, autocommit = False, bind= engine)

Base = declarative_base()

def get_db():

    db = SessionLocal()

    try: 
        yield db
    finally:
        db.close()