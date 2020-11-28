from passlib.context import CryptContext
from jose import jwt

from core.settings import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(inc_password: str, hashed_password: str):
    return pwd_context.verify(inc_password, hashed_password)


def encode_jwt(username: str) -> str:

    to_encode = {}
    to_encode.update({"sub": username})
    to_encode.update({"exp": settings.ACCESS_TOKEN_EXPIRE_MINUTES})

    enc_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return enc_jwt
