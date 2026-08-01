from datetime import datetime, timedelta

from jose import jwt, JWTError

from fastapi import Depends, HTTPException, status

from fastapi.security import OAuth2PasswordBearer



# ==========================================
# JWT Configuration
# ==========================================

SECRET_KEY = "your-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60





# ==========================================
# OAuth2 Bearer Token
# ==========================================

oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/auth/login"

)





# ==========================================
# Create Access Token
# ==========================================

def create_access_token(

    data: dict

):

    to_encode = data.copy()



    expire = datetime.utcnow() + timedelta(

        minutes=ACCESS_TOKEN_EXPIRE_MINUTES

    )



    to_encode.update(

        {

            "exp": expire

        }

    )



    encoded_jwt = jwt.encode(

        to_encode,

        SECRET_KEY,

        algorithm=ALGORITHM

    )



    return encoded_jwt





# ==========================================
# Decode Token
# ==========================================

def decode_token(

    token: str

):

    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )


        return payload



    except JWTError:


        return None





# ==========================================
# Get Current User Dependency
# ==========================================

def get_current_user(

    token: str = Depends(oauth2_scheme)

):


    payload = decode_token(token)



    if payload is None:


        raise HTTPException(

            status_code=status.HTTP_401_UNAUTHORIZED,

            detail="Invalid authentication token",

            headers={

                "WWW-Authenticate": "Bearer"

            }

        )



    return payload