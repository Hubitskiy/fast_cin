from core.db.db_managment import BaseCRUDDBManagement
from users.models import UserModel


class UserDBManagement(metaclass=BaseCRUDDBManagement):

    def create(self, **kwargs):

        user = UserModel(**kwargs)

        return user
