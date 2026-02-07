from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password


class AuthService:

    @staticmethod
    def register(
        db: Session,
        username: str,
        password: str,
        first_name: str,
        last_name: str
    ):

        existing_user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if existing_user:
            raise ValueError("Bunday user mavjud")

        new_user = User(
            username=username,
            password=hash_password(password),
            first_name=first_name,
            last_name=last_name
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)    

        return new_user          
    @staticmethod
    def login(
        db: Session,
        username: str,
        password: str
    ) -> User:

        user = (
            db.query(User)
            .filter(User.username == username)
            .first()
        )

        if not user:
            raise ValueError("User topilmadi")

        if not verify_password(password, user.password):
            raise ValueError("Parol notogri")

        return user