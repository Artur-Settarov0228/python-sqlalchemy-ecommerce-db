from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.order import Order


from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(200), nullable=False)
    password = Column(String(120), nullable=False)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)

    orders = relationship("Order", back_populates="user")

