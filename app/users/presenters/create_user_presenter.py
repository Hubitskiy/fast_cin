from core.presenters import CreatePresenter

from users.serializers import CreateUserSerializer


class CreateUserPresenter(CreatePresenter):

    def __init__(self, body: CreateUserSerializer):
        self.body = body

    def create(self, **kwargs):
        pass
