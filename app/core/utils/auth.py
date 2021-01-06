from typing import Optional, Any, Dict
from datetime import datetime

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi.exceptions import HTTPException

from core.utils import crypt
from core.db.database import Database
from core.db.utils import DBConnection
from core.settings import settings

from users.models import UserModel
from users.user_managment import UserDBManagement


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=settings.TOKEN_URL)


def authenticate_user(
        db_management: Any,
        username: str,
        password: str
) -> Optional[UserModel or bool]:

    user = db_management.retrieve_user_by(email=username)

    if user is None:
        return False

    if user.hashed_password == crypt.get_password_hash(password):
        return False

    return user


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModel:

    encoded_data: Dict = crypt.decode_jwt(token=token)

    username: str = encoded_data.get("sub")

    user_db = UserDBManagement(DBConnection(Database()))
    user = user_db.retrieve_user_by(email=username)

    if not user.is_active:
        raise HTTPException(
            detail="User isn`t active",
            status_code=status.HTTP_403_FORBIDDEN
        )

    expires_date:  datetime.timestamp = encoded_data.get("exp")

    if datetime.fromtimestamp(expires_date) <= datetime.utcnow():
        raise HTTPException(
            detail="Token has expire",
            headers={"WWW-Authenticate": "Bearer"},
            status_code=status.HTTP_410_GONE
        )

    return user
