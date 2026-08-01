from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.crud.user import get_user_by_username


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

SECRET_KEY="vendor_invoice_secret"
ALGORITHM = "HS256"



def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid authentication credentials",
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )


    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )


        username = payload.get("sub")


        if username is None:
            raise credentials_exception


    except JWTError:
        raise credentials_exception



    user = get_user_by_username(
        db,
        username
    )


    if user is None:
        raise credentials_exception


    return user