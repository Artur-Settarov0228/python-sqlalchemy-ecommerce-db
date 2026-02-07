from sqlalchemy import Integer, Float, Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.models.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column( Integer, primary_key=True)
    name = Column(String(230), nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    items = relationship(
        "OrderItem",
        back_populates="product",
        cascade="all, delete-orphan"
    )