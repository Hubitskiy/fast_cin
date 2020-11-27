from fastapi.security import OAuth2PasswordRequestForm

from core.presenters import CreatePresenter
from core.containers import resolve

from users.usecases import AuthenticateUserUseCase


class AuthenticateUserPresenter(CreatePresenter, OAuth2PasswordRequestForm):

    def create(self, **kwargs):

        access_token = resolve(AuthenticateUserUseCase)

        return access_token(username=self.username, password=self.password)
