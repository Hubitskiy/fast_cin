from attr import attrs

from fastapi.exceptions import HTTPException
from fastapi import status

from core.usecases import BaseUseCase
from core.utils import crypt

from users.user_managment import UserDBManagement
from users.models import UserModel
from users.services import ActivateUserService


@attrs(auto_attribs=True)
class ActivateUserUseCase(BaseUseCase):
    _activate_user: ActivateUserService
    _user_management: UserDBManagement

    def validate(self, uid: str, token: str, *args, **kwargs) -> UserModel:

        user_id = int(crypt.base64_decode(uid))

        email = crypt.base64_decode(token)

        user = self._user_management.retrieve_user_by(id=user_id)

        if user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UID or Token")

        elif user.is_active:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invitation was accepted")

        elif user.email != email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UID or Token")

        return user

    def execute(self, uid: str, token: str, *args, **kwargs):

        validated_user = self.validate(uid=uid, token=token)

        return self._activate_user(validated_user)
