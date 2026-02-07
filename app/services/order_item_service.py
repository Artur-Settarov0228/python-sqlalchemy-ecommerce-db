# app/services/order_item_service.py

from sqlalchemy.orm import Session
from app.models.order_item import OrderItem
from app.models.product import Product


class OrderItemService:

    @staticmethod
    def add_product_to_order(
        db: Session,
        order_id: int,
        product_id: int,
        quantity: int
    ):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise ValueError("Product topilmadi")

        item = OrderItem(
            order_id=order_id,
            product_id=product.id,
            quantity=quantity,
            price=product.price
        )

        db.add(item)
        db.commit()
        return item
