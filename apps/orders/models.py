import datetime

from sqlalchemy import (
    Column, ForeignKey, Integer, String, Numeric, DateTime
    )
from core.database import Base


class Order(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id"))
    created_at = Column(
        DateTime, default = lambda: datetime.datetime.now(datetime.timezone.utc).replace(tzinfo=None)
        )


class OrderItem(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    order = Column(Integer, ForeignKey("order.id"))
    product = Column(Integer, ForeignKey("product.id"))

