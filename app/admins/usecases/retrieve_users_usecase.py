from typing import Dict
from attr import attrs

from core.usecases import BaseUseCase

from admins.services import UniqueUserRetrieve, ListRetrieveUserService


@attrs(auto_attribs=True)
class RetrieveUsersUseCase(BaseUseCase):
    _unique_user_retrieve: UniqueUserRetrieve
    _list_user_retrieve: ListRetrieveUserService

    def validate(self, *args, **kwargs):
        pass

    def execute(
        self,
        limit: int = None,
        offset: int = None,
        pk: int = None,
        *args,
        **kwargs
    ) -> Dict:

        if pk is not None:
            return self._unique_user_retrieve

        return self._list_user_retrieve
