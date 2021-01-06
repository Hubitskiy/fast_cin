from attr import attrs
from datetime import datetime
from typing import Dict

from fastapi.exceptions import HTTPException
from fastapi import status

from core.usecases import BaseUseCase
from core.utils import crypt

from users.services import CreateTokensService
from users.user_managment import UserDBManagement


@attrs(auto_attribs=True)
class RefreshTokenUseCase(BaseUseCase):
    _users_management: UserDBManagement
    _create_tokens: CreateTokensService

    def validate(self, access_token: str, refresh_token: str, *args, **kwargs) -> str:

        decoded_refresh_token = crypt.decode_jwt(token=refresh_token)

        expire_date = decoded_refresh_token.get("exp")

        if expire_date and datetime.fromtimestamp(expire_date) < datetime.utcnow():

            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token Has Expire")

        decoded_access_token = crypt.decode_jwt(token=access_token)

        username = decoded_access_token.get("sub")

        user = self._users_management.retrieve_user_by(email=username)

        if user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid date")

        return username

    def execute(self, username, *args, **kwargs) -> Dict:
        return self._create_tokens(username=username)

    def __call__(self, access_token, refresh_token):

        username = self.validate(access_token=access_token, refresh_token=refresh_token)

        return self.execute(username=username)
