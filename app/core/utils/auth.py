from typing import Optional, Any

from core.utils import crypt

from users.models import UserModel


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
