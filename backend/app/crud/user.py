
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

from app.auth.password import (
    hash_password,
    verify_password
)



def authenticate_user(
    db: Session,
    email: str,
    password: str
):

    user = (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


    if not user:
        return None


    if not verify_password(
        password,
        user.hashed_password
    ):
        return None


    return user



def get_user_by_email(
    db: Session,
    email: str
):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )



def get_user_by_username(
    db: Session,
    username: str
):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )



def create_user(
    db: Session,
    user: UserCreate
):

    hashed_password = hash_password(
        user.password
    )


    db_user = User(

        username=user.username,

        email=user.email,

        password_hash=hashed_password,

        role=user.role
    )


    db.add(db_user)

    db.commit()

    db.refresh(db_user)


    return db_user