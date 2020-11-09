from core.presenters import CreatePresenter
from core.containers import resolve

from users.serializers import CreateUserSerializer
from users.usecases import CreateUserUseCase


class CreateUserPresenter(CreatePresenter):

    def __init__(self, user_data: CreateUserSerializer):
        self.user_data = user_data

    def create(self, **kwargs):

        create_user = resolve(CreateUserUseCase)

        create_user(user_data=self.user_data.dict())

        return {}
