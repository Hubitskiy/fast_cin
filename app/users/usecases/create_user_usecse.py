from fastapi.exceptions import HTTPException
from attr import attrs
from typing import Dict

from core.usecases import BaseUseCase

from users.user_managment import UserDBManagement
from users.services import CreateUserService


@attrs(auto_attribs=True)
class CreateUserUseCase(BaseUseCase):
    _create_user: CreateUserService

    def validate(self, user_data: Dict, **kwargs) -> bool:

        user = UserDBManagement()
        user = user.retrieve(email=user_data['email'])

        if user:
            raise HTTPException(status_code=409, detail="User with given email already exist")

        return True

    def execute(self, user_data: Dict, *args, **kwargs):

        create_user = self._create_user(user_data=user_data)

        return create_user
