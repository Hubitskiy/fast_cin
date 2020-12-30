from typing import Any

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

    def retrieve_user_by(self, **kwargs) -> UserModel:

        with self.db_connect as db:
            user = db.query(UserModel).filter_by(**kwargs).first()

        return user

    def set_attr(self, user_id: int, attr: str, value: Any) -> UserModel:

        with self.db_connect as db:
            user: UserModel = db.query(UserModel).filter_by(id=user_id).first()
            setattr(user, attr, value)
            db.commit()
            db.refresh(user)

        return user
