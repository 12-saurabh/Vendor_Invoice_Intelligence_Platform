from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse
)

from app.crud.user import (
    create_user,
    get_user_by_email,
    authenticate_user
)

from app.crud.audit import create_audit_log

from app.auth.jwt import create_access_token


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# ==========================
# Register
# ==========================

@router.post("/register", response_model=UserResponse)
def register(
    user: UserCreate,
    db = Depends(get_db)
):

    existing = get_user_by_email(
        db,
        user.email
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    return create_user(db, user)



# ==========================
# Login
# ==========================

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db = Depends(get_db)
):

    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )


    create_audit_log(
        db=db,
        user_id=user.id,
        action="LOGIN",
        entity="User",
        entity_id=user.id,
        new_value="Successful login"
    )


    access_token = create_access_token(
        {
            "sub": str(user.id),
            "role": user.role
        }
    )


    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": user.username,
        "role": user.role
    }