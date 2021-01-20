from attr import attrs

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

from core.presenters import (
    CreatePresenter,
    RetrievePresenter,
    UpdatePresenter
)
from core.containers import resolve
from core.utils.auth import get_current_user, oauth2_scheme
from core.utils.response_handlers import prepare_object_to_response

from users.usecases import AuthenticateUserUseCase, ActivateUserUseCase, RefreshTokenUseCase
from users.models import UserModel

from users.serializers import UidTokenSerializer, RefreshTokenSerializer


class AuthenticateUserPresenter(CreatePresenter, OAuth2PasswordRequestForm):

    def create(self, **kwargs):

        access_token = resolve(AuthenticateUserUseCase)

        return access_token(username=self.username, password=self.password)


@attrs(auto_attribs=True)
class RefreshTokenPresenter(CreatePresenter):

    refresh_token: RefreshTokenSerializer
    access_token: str = Depends(oauth2_scheme)

    def create(self, **kwargs):

        refresh_tokens = resolve(RefreshTokenUseCase)

        return refresh_tokens(access_token=self.access_token, **self.refresh_token.dict())


@attrs(auto_attribs=True)
class AuthorizationUserPresenter(RetrievePresenter):

    current_user: UserModel = Depends(get_current_user)

    def retrieve(self, **kwargs):
        return self.current_user.__dict__


@attrs(auto_attribs=True)
class ActivateUserPresenter(UpdatePresenter):

    activation_data: UidTokenSerializer

    def update(self, *args, **kwargs):

        activate_user = resolve(ActivateUserUseCase)

        user = activate_user(**self.activation_data.dict())

        return prepare_object_to_response(user)
