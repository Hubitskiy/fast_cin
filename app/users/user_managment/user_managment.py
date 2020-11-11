from core.db.db_managment import BaseCRUDDBManagement

from users.models import UserModel


class UserDBManagement(metaclass=BaseCRUDDBManagement):

    def create_user(self, **kwargs) -> UserModel:

        with self.db as db:
            user = UserModel(**kwargs)
            db.add(user)
            db.commit()
            db.refresh(user)

        return user

    def retrieve_by_email(self, email: str) -> UserModel:

        with self.db as db:
            user = db.query(UserModel).filter(UserModel.email == email).all()

        return user
