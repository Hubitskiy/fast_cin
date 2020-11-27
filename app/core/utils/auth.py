from typing import Optional, Any

from core.utils import crypt

from users.models import UserModel
from logging import warning

def authenticate_user(
        db_management: Any,
        username: str,
        password: str
) -> Optional[UserModel or bool]:

    user = db_management.retrieve_by_email(email=username)

    if user is None:
        return False

    if crypt.verify_password(inc_password=password, hashed_password=user.hashed_password):
        return False

    return user
