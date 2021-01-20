from typing import List

from core.db.db_managment import DB

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
