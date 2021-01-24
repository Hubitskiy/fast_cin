from attr import attrs

from core.usecases import BaseService
from core.utils.response_handlers import prepare_object_to_response

from admins.admins_managment import AdminDBManagement


@attrs(auto_attribs=True)
class UpdateUserService(BaseService):
    _admin_management: AdminDBManagement

    def __call__(self, *args, **kwargs):

        pk = kwargs.pop("pk")

        updated_user = self._admin_management.update_user(pk=pk, attrs_and_fields=kwargs)

        return prepare_object_to_response(updated_user)
