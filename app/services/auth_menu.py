# app/menus/auth_menu.py

from app.core.database import SessionLocal
from app.services.auth_service import AuthService


def auth_menu():
    """
    1 - Register
    2 - Login
    3 - Exit
    """
    db = SessionLocal()

    while True:
        print("\n===== AUTH MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Chiqish")

        choice = input("Tanlang (1/2/3): ").strip()

        try:
            if choice == "1":
                print("\n--- REGISTRATION ---")
                username = input("Username: ")
                password = input("Password: ")
                first_name = input("First name: ")
                last_name = input("Last name: ")

                user = AuthService.register(
                    db=db,
                    username=username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )

                print(f"\n✅ User yaratildi! ID={user.id}")

            elif choice == "2":
                print("\n--- LOGIN ---")
                username = input("Username: ")
                password = input("Password: ")

                user = AuthService.login(
                    db=db,
                    username=username,
                    password=password
                )

                print(f"\n✅ Xush kelibsiz, {user.first_name}!")

                return user  # 👈 MUHIM: login bo‘lsa user qaytaradi

            elif choice == "3":
                print("\n👋 Dasturdan chiqildi")
                return None

            else:
                print("\n❌ Noto‘g‘ri tanlov")

        except Exception as e:
            print("\n❌ Xato:", e)

        db.close()
