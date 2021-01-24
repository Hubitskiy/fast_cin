from attr import attrs

from fastapi import status
from fastapi.exceptions import HTTPException

from core.usecases import BaseUseCase
from admins.admins_managment import AdminDBManagement

from admins.services import UpdateUserService


@attrs(auto_attribs=True)
class UpdateUserUseCase(BaseUseCase):
    _admin_management: AdminDBManagement
    _update_user: UpdateUserService

    def validate(self, email: str, pk: int, *args, **kwargs) -> None:

        user = self._admin_management.retrieve_user_by(email=email)

        if user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with given email already exist"
            )

        user = self._admin_management.retrieve_user_by_pk(pk=pk)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User wasn`t found")

    def execute(self, *args, **kwargs):
        return self._update_user(**kwargs)
