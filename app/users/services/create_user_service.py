from attr import attrs

from core.usecases import BaseService
from core.utils import password_hasher

from users.user_managment import UserDBManagement
from users.models import UserModel


@attrs(auto_attribs=True)
class CreateUserService(BaseService):
    _user_db_management: UserDBManagement

    def create_user(self, **kwargs) -> UserModel:

        password = kwargs.pop("password")

        hashed_password = password_hasher.hash_password(password=password)

        kwargs.setdefault("hashed_password", hashed_password)

        user = self._user_db_management.create_user(**kwargs)

        return user

    def __call__(self, **kwargs) -> UserModel:
        return self.create_user(**kwargs)
