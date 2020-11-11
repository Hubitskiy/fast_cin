from core.usecases import BaseService
from core.utils import password_hasher

from users.user_managment import UserDBManagement


class CreateUserService(BaseService):

    def create_user(self, *args, **kwargs) -> UserDBManagement:

        password = kwargs.pop("password")

        hashed_password = password_hasher.hash_password(password=password)

        kwargs.setdefault("hashed_password", hashed_password)

        user = UserDBManagement()
        user.create_user(**kwargs)

        return user

    def __call__(self, **kwargs) -> UserDBManagement:
        return self.create_user(**kwargs)
