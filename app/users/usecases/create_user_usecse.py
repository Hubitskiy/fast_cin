from fastapi.exceptions import HTTPException
from attr import attrs

from core.usecases import BaseUseCase

from users.user_managment import UserDBManagement
from users.services import CreateUserService


@attrs(auto_attribs=True)
class CreateUserUseCase(BaseUseCase):
    _create_user: CreateUserService
    _user_db_management: UserDBManagement

    def validate(self, email: str, **kwargs) -> bool:

        user = self._user_db_management.retrieve_by_email(email=email)

        if user:
            raise HTTPException(status_code=409, detail=f"User with given email already exist")

        return True

    def execute(self, *args, **kwargs) -> UserDBManagement:

        create_user = self._create_user(**kwargs)

        return create_user
