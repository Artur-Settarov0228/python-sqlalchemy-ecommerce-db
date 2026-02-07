from app.core.database import SessionLocal
from app.services.product_service import ProductService
from app.services.order_service import OrderService
from app.services.order_item_service import OrderItemService


def user_menu(current_user):
    """
    Login bolgan user uchun menyu
    """
    db = SessionLocal()

    try:
        while True:
            print(f"\n===== USER MENU ({current_user.username}) =====")
            print("1. Productlarni korish")
            print("2. Logout")

            choice = input("Tanlang (1/2): ").strip()

            if choice == "1":
                products = ProductService.list_products(db)

                if not products:
                    print(" Product yoq")
                    continue

                print("\n--- PRODUCTLAR ---")
                for p in products:
                    print(f"{p.id}. {p.name} — {p.price}")

                try:
                    product_id = int(input("Product ID tanlang: "))
                    quantity = int(input("Miqdor (quantity): "))
                except ValueError:
                    print(" Notogri raqam kiritildi")
                    continue

                order = OrderService.get_or_create_order(
                    db=db,
                    user_id=current_user.id
                )

                OrderItemService.add_product_to_order(
                    db=db,
                    order_id=order.id,
                    product_id=product_id,
                    quantity=quantity
                )

                print("Product orderga qoshildi")

            elif choice == "2":
                print("Logout qilindi")
                break

            else:
                print("Notogri tanlov")

    finally:
        db.close()
