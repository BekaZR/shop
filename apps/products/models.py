from sqlalchemy import (
    Column, ForeignKey, Integer, String, Numeric
    )
from core.database import Base


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), index=True)


class SubCategory(Base):
    __tablename__ = "sub_category"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), index=True)
    category = Column(Integer, ForeignKey("category.id"))


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(60), index=True)
    description = Column(String(1000))
    price = Column(Numeric(1000000, 2))
