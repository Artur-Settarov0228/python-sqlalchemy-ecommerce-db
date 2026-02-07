# main.py

from app.services.auth_menu import auth_menu


def main():
    user = auth_menu()

    if user:
        print(f"\n🔐 Login bo‘ldi: {user.username}")
        # keyin order menu, product menu va hokazo
    else:
        print("\nDastur yopildi")


if __name__ == "__main__":
    main()
