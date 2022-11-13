from sqlalchemy import (
    Boolean, Column, ForeignKey, Integer, String
    )
from core.database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), index=True)
    password = Column(String(5000))
    is_active = Column(Boolean, default=False)

