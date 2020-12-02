from typing import Optional, Any, Dict

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi import status

from core.utils import crypt
from core.db.database import Database
from core.db.utils import DBConnection


from users.models import UserModel
from users.user_managment import UserDBManagement


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token/")


def authenticate_user(
        db_management: Any,
        username: str,
        password: str
) -> Optional[UserModel or bool]:

    user = db_management.retrieve_by_email(email=username)

    if user is None:
        return False

    if user.hashed_password == crypt.get_password_hash(password):
        return False

    return user


def get_current_user(token: str = Depends(oauth2_scheme)) -> UserModel:

    encoded_data: Dict = crypt.decode_jwt(token=token)

    username: str = encoded_data.get("sub")

    user_db = UserDBManagement(DBConnection(Database()))
    user = user_db.retrieve_by_email(email=username)

    if not user.is_active:
        raise HTTPException(
            detail="User isn`t active",
            status_code=status.HTTP_401_UNAUTHORIZED
        )

    return user
