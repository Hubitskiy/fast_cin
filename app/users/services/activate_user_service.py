from attr import attrs

from core.usecases import BaseService

from users.user_managment import UserDBManagement
from users.models import UserModel


@attrs(auto_attribs=True)
class ActivateUserService(BaseService):
    _user_management: UserDBManagement

    def activate_user(self, user: UserModel) -> UserModel:

        active_user = self._user_management.set_active(user_id=user.id)

        return active_user

    def __call__(self, user: UserModel, *args, **kwargs) -> UserModel:

        return self.activate_user(user=user)
