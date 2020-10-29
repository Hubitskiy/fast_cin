from core.db.db_managment import BaseCRUDDBManagement

from users.models import UserModel


class UserDBManagement(metaclass=BaseCRUDDBManagement):

    def create(self, **kwargs):

        with self.db as db:
            user = UserModel(**kwargs)
            db.add(user)
            db.commit()
            db.refresh(user)

        return user
