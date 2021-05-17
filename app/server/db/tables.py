from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .connection import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(20), unique=True, index=True)
    hashed_password = Column(String(20))
    is_active = Column(Boolean, default=True)


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    description = Column(String(20))
