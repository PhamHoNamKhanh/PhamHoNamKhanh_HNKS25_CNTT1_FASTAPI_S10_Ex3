from Lythuyet import Base
from sqlalchemy import Column, INTEGER, String, Boolean, DateTime
from sqlalchemy.sql import func
class Usermodel (Base):

    __talename__ = 'User'
    id = Column(INTEGER, primary_key = True, auto_increment = True)
    name_user = Column(String(100), nullable= False, Index = True)
    phone = Column(String(100), nullable= False, Index = True, unique=  True)
    email = Column(String(100), nullable= False, Index = True, unique=  True)
    is_active = Column(Boolean, default= True)
    create_at = Column()