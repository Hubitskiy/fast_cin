from typing import Dict, Optional
from passlib.context import CryptContext

import base64

from jose import jwt, JWTError

from fastapi.exceptions import HTTPException
from fastapi import status

from core.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(inc_password: str, hashed_password: str):
    return pwd_context.verify(inc_password, hashed_password)


def encode_jwt(username: str = None,  is_access_token: bool = True) -> str:

    if username is None and is_access_token is None:
        raise KeyError("Username or Token Expire Time must be added")

    to_encode = {}

    if username is not None:
        to_encode.update({"sub": username})

    if is_access_token:
        to_encode.update({"exp": settings.ACCESS_TOKEN_EXPIRE_TIME})
    else:
        to_encode.update({"exp": settings.REFRESH_EXPIRE_TIME})

    enc_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return enc_jwt


def decode_jwt(token: str) -> Dict:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        decoded_data: Dict = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise credentials_exception

    return decoded_data


def base64_encode(enc_data: Optional[str or int]) -> str:

    encode_data = None

    if type(enc_data) is int:
        encode_data = str(enc_data).encode()

    elif type(enc_data) is str:
        encode_data = enc_data.encode()

    encoded_data = base64.b64encode(encode_data)

    return encoded_data.decode()


def base64_decode(dec_data: str) -> str:

    decode_data = dec_data.encode('ascii')

    decoded_data = base64.b64decode(decode_data)

    return decoded_data.decode('ascii')
