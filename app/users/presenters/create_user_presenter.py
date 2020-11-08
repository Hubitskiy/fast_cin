from core.presenters import CreatePresenter

from users.serializers import CreateUserSerializer
from users.user_managment import UserDBManagement


class CreateUserPresenter(CreatePresenter):

    def __init__(self, user_data: CreateUserSerializer):
        self.user_data = user_data

    def create(self, **kwargs):

        user_dict = self.user_data.dict()

        password = user_dict.pop("password")

        user = UserDBManagement()

        user.create(**user_dict, hashed_password=password)

        return {}
