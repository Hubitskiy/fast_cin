from typing import Dict
from attr import attrs

from core.presenters import CreatePresenter
from core.containers import resolve

from users.serializers import CreateUserSerializer
from users.usecases import CreateUserUseCase


@attrs(auto_attribs=True)
class CreateUserPresenter(CreatePresenter):
    user_data: CreateUserSerializer

    def create(self, **kwargs) -> Dict:

        create_user = resolve(CreateUserUseCase)

        create_user(**self.user_data.dict())

        return {}
