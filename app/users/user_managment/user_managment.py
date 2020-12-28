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

    def retrieve_user_by_id(self, id: int) -> UserModel:

        with self.db_connect as db:
            user = db.query(UserModel).get(id)

        return user

    def set_active(self, user_id: int) -> UserModel:

        with self.db_connect as db:
            user: UserModel = db.query(UserModel).filter_by(id=user_id).first()
            setattr(user, "is_active", True)
            db.commit()
            db.refresh(user)

        return user
