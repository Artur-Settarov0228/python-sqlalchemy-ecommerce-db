from app.menu.auth_menu import auth_menu
from app.menu.user_menu import user_menu


def main():
    while True:
        user = auth_menu()

        if user is None:
            break

        user_menu(user)


if __name__ == "__main__":
    main()
