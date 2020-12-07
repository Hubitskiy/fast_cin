from attr import attrs

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from core.presenters import (CreatePresenter, RetrievePresenter)
from core.containers import resolve
from core.utils.auth import get_current_user

from users.usecases import AuthenticateUserUseCase
from users.models import UserModel


class AuthenticateUserPresenter(CreatePresenter, OAuth2PasswordRequestForm):

    def create(self, **kwargs):

        access_token = resolve(AuthenticateUserUseCase)

        return access_token(username=self.username, password=self.password)


@attrs(auto_attribs=True)
class AuthorizationUserPresenter(RetrievePresenter):

    current_user: UserModel = Depends(get_current_user)

    def retrieve(self, **kwargs):
        return self.current_user.__dict__
