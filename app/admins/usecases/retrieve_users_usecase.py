from typing import Dict
from attr import attrs

from core.usecases import BaseUseCase

from admins.services import UniqueUserRetrieveService, ListRetrieveUserService


@attrs(auto_attribs=True)
class RetrieveUsersUseCase(BaseUseCase):
    _unique_user_retrieve: UniqueUserRetrieveService
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
            return self._unique_user_retrieve(pk=pk)

        return self._list_user_retrieve(limit=limit, offset=offset, **kwargs)
