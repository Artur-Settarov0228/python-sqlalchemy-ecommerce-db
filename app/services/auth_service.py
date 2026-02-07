from app.models.user import User
from sqlalchemy.orm import Session
from app.core.security import hash_password, verify_password


class AuthService:

    @staticmethod
    def register(db:Session, username:str, password:str, last_name:str, first_name: str) :

        user =db.query(User).filter(User.username == username).first()

        if user:
            raise ValueError("Bunday user mavjut")
        
        hashed_password = hash_password(password)

        creat_user =User(
            username = username,
            password = hashed_password,
            last_name = last_name,
            first_name = first_name

        )

        db.add(creat_user)
        db.commit()
        db.refresh(user)

        return creat_user()




    @staticmethod
    def login(db:Session, username:str, password:str):

        user = db.query(User).filter(User.username == username).first()

        if not user:
            raise ValueError("Bunday user yoq registratsiyadan utmagan ")
        if not verify_password(password, user.password):
            raise ValueError(" password xato ")
        
        return user
    


