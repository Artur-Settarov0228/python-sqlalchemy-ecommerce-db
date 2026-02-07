from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.product import Product

class ProductService:

    @staticmethod
    def show_product():

        db = SessionLocal()
        products = db.query(Product).all()

        for product in products:
            print(
        f"""
        id :{product.id}
        name : {product.name},
        price: {product.price},
        quantity:{product.quantity}
        """
        )
        