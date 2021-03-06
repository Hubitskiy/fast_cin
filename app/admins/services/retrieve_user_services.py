from attr import attrs

from typing import Dict, List

from fastapi.exceptions import HTTPException
from fastapi import status

from core.usecases import BaseService
from core.utils.response_handlers import prepare_list_response, prepare_object_to_response

from admins.admins_managment import AdminDBManagement


@attrs(auto_attribs=True)
class UniqueUserRetrieveService(BaseService):
    _admin_management: AdminDBManagement

    def __call__(self, pk: int, *args, **kwargs) -> Dict:

        user = self._admin_management.retrieve_user_by_pk(pk)

        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User wasn`t found")

        return prepare_object_to_response(user)


@attrs(auto_attribs=True)
class ListRetrieveUserService(BaseService):
    _admin_management: AdminDBManagement

    @staticmethod
    def prepare_query(**kwargs) -> Dict:

        if kwargs.get("is_active") is None:
            kwargs.pop("is_active")

        return kwargs

    def __call__(self, *args, **kwargs) -> Dict[str, List[Dict]]:

        query = self.prepare_query(**kwargs)

        users = self._admin_management.retrieve_list_users(**query)

        return prepare_list_response(users, **kwargs)
