from attr import attrs

from fastapi import Depends, Path

from core.presenters import UpdatePresenter
from core.utils.auth import check_is_admin_user

from core.containers import resolve

from admins.serializers import UpdateUserByAdminSerializer
from users.models import UserModel
from admins.usecases import UpdateUserUseCase


@attrs(auto_attribs=True)
class UpdateUserPresenter(UpdatePresenter):
    user_payload: UpdateUserByAdminSerializer

    pk: int = Path(...)

    is_admin_user: UserModel = Depends(check_is_admin_user)

    def update(self, *args, **kwargs):
        update_user = resolve(UpdateUserUseCase)
        return update_user(**self.user_payload.dict(exclude_unset=True), pk=self.pk)
