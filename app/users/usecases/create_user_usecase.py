from fastapi.exceptions import HTTPException
from attr import attrs

from core.usecases import BaseUseCase

from users.user_managment import UserDBManagement
from users.services import CreateUserService, SendUserRegistrationInvitationService
from users.models import UserModel


@attrs(auto_attribs=True)
class CreateUserUseCase(BaseUseCase):
    _create_user: CreateUserService
    _send_email_invitation: SendUserRegistrationInvitationService
    _user_db_management: UserDBManagement

    def validate(self, email: str, **kwargs) -> bool:

        user = self._user_db_management.retrieve_user_by(email=email)

        if user:
            raise HTTPException(status_code=409, detail=f"User with given email already exist")

        return True

    def execute(self, *args, **kwargs) -> UserModel:

        created_user = self._create_user(**kwargs)

        self._send_email_invitation(user=created_user)

        return created_user
