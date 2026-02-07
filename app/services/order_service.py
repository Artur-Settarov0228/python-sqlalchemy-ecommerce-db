from sqlalchemy.orm import Session
from app.models.order import Order


class OrderService:

    @staticmethod
    def get_or_create_order(db: Session, user_id: int) -> Order:
        order = (
            db.query(Order)
            .filter(Order.user_id == user_id, Order.status == "pending")
            .first()
        )

        if order:
            return order

        order = Order(user_id=user_id)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
