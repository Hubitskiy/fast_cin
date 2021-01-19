from attr import attrs

from typing import Dict, List

from core.usecases import BaseService
from core.utils.response_handlers import prepare_list_response

from admins.admins_managment import AdminDBManagement


class UniqueUserRetrieveService(BaseService):

    def __call__(self, pk, *args, **kwargs) -> Dict:
        pass


@attrs(auto_attribs=True)
class ListRetrieveUserService(BaseService):
    _admin_management: AdminDBManagement

    def __call__(self, *args, **kwargs) -> Dict[str, List[Dict]]:

        users = self._admin_management.retrieve_list_users(**kwargs)

        return prepare_list_response(users)

