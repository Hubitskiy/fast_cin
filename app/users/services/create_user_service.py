from typing import Dict
from core.usecases import BaseService

from users.user_managment import UserDBManagement


class CreateUserService(BaseService):

    def create_user(self, user_data: Dict, *args, **kwargs) -> UserDBManagement:

        user = UserDBManagement()
        user.create(**user_data)

        return user

    def __call__(self, user_data: Dict, **kwargs):
        return self.create_user(**user_data)
