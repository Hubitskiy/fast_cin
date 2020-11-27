from core.db.db_managment import DB

from users.models import UserModel


class UserDBManagement(DB):

    def create_user(self, **kwargs) -> UserModel:

        with self.db_connect as db:
            user = UserModel(**kwargs)
            db.add(user)
            db.commit()
            db.refresh(user)

        return user

    def retrieve_by_email(self, email: str) -> UserModel:

        with self.db_connect as db:
            user = db.query(UserModel).filter(UserModel.email == email).first()

        return user
