from fastapi.exceptions import HTTPException
from attr import attrs

from core.usecases import BaseUseCase
from users.user_managment import UserDBManagement


@attrs(auto_attribs=True)
class CreateUserUseCase(BaseUseCase):
    _create_user: None

    def validate(self, email: str,*args, **kwargs):

        user = UserDBManagement()
        list_users = user.retrieve(email=email)

        if list_users:
            raise HTTPException(status_code=409, detail="User already exist")

    def execute(self, *args, **kwargs):
        pass
