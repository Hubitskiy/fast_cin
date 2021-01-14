from attr import attrs

from fastapi import Query
from fastapi import Depends

from core.presenters import RetrievePresenter
from core.utils.auth import check_is_admin_user
from core.containers import resolve

from admins.usecases import RetrieveUsersUseCase

from users.models import UserModel


@attrs(auto_attribs=True)
class RetrieveListUserPresenter(RetrievePresenter):

    check_is_admin: UserModel = Depends(check_is_admin_user)

    offset: int = Query(0)
    limit: int = Query(25)

    is_active: bool = Query(None)

    def retrieve(self, **kwargs):

        retrieve_users = resolve(RetrieveUsersUseCase)

        return retrieve_users(limit=self.limit, offset=self.offset)
