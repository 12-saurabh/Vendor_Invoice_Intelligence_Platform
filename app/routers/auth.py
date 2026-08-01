from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import get_db
from app.crud.audit import create_audit_log
from app.schemas.user import (
    UserCreate,
    UserResponse
)
from app.crud.user import authenticate_user
from app.crud.user import (
    create_user,
    get_user_by_email
)

from app.models.user import User   # <-- ADD THIS

from app.auth.password import verify_password
from app.auth.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )


    access_token = create_access_token(
        data={
            "sub": str(user.id),
            "role": user.role
        }
    )


    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()


    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )


    if not verify_password(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    
    create_audit_log(

        db,

        user_id=user.id,

        action="LOGIN",

        entity="User",

        entity_id=user.id,

        new_value="Successful login"

    )

    token = create_access_token(
        {
            "sub": str(user.id),
            "role": user.role
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }