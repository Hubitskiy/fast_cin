from fastapi.exceptions import HTTPException
from fastapi import status
from attr import attrs

from core.usecases import BaseUseCase
from core.utils.auth import authenticate_user

from users.user_managment import UserDBManagement
from users.services import CreateTokensService


@attrs(auto_attribs=True)
class AuthenticateUserUseCase(BaseUseCase):
    _user_db_management: UserDBManagement
    _create_tokens: CreateTokensService

    def validate(self, username: str, password: str):

        auth_user = authenticate_user(username=username, password=password, db_management=self._user_db_management)

        if not auth_user:
            raise HTTPException(
                detail="Incorrect Email or Password", status_code=status.HTTP_401_UNAUTHORIZED
            )

        if not auth_user.is_active:
            raise HTTPException(
                detail="Complete registration", status_code=status.HTTP_403_FORBIDDEN
            )

    def execute(self, username: str, **kwargs) -> str:
        return self._create_tokens(username)
