from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.user import User
from app.auth.jwt import decode_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# ============================================
# Database Dependency
# ============================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# ============================================
# Current Logged-in User
# ============================================

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    payload = decode_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )

    user_id = payload.get("sub")

    if user_id is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )

    user = (
        db.query(User)
        .filter(User.id == int(user_id))
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# ============================================
# Role Based Permission
# ============================================

def require_role(*roles):

    def role_checker(
        current_user: User = Depends(get_current_user)
    ):

        if current_user.role not in roles:

            raise HTTPException(
                status_code=403,
                detail="Permission Denied"
            )

        return current_user

    return role_checker