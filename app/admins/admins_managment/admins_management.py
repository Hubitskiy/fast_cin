from typing import List, Dict

from core.db.db_managment import DB
from sqlalchemy.exc import InvalidRequestError

from users.models import UserModel


class AdminDBManagement(DB):

    def retrieve_list_users(self, limit: int, offset: int, **filters) -> List[UserModel]:

        with self.db_connect as db:
            list_users = db.query(UserModel).filter_by(**filters).limit(limit).offset(offset)

            return list_users

    def retrieve_user_by_pk(self, pk: int) -> UserModel:

        with self.db_connect as db:
            user = db.query(UserModel).get(pk)

            return user

    def retrieve_user_by(self, **kwargs):

        with self.db_connect as db:
            user = db.query(UserModel).filter_by(**kwargs).first()

            return user

    def update_user(self, pk: int, attrs_and_fields: Dict, **kwargs) -> UserModel:

        with self.db_connect as db:
            try:
                user: UserModel = db.query(UserModel).filter_by(id=pk).first()

                for attr, value in attrs_and_fields.items():
                    setattr(user, attr, value)
                db.commit()

            except Exception:
                db.rollback()
                raise InvalidRequestError("Transaction was not complete")

            db.refresh(user)

        return user
