from sqlalchemy import Integer, Column, String,ForeignKey, Float
from app.models.base import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)

    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)


    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    