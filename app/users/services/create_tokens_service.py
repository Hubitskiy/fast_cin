from core.usecases import BaseService
from core.utils import crypt
from core.settings import settings


class CreateTokensService(BaseService):

    def create_access_token(self, username: str):

        access_token = crypt.encode_jwt(username)
        refresh_token = crypt.encode_jwt(is_access_token=False)

        return {
            "refresh_token": str(refresh_token),
            "access_token": str(access_token),
            "token_type": settings.TOKEN_TYPE
        }

    def __call__(self, username: str, *args, **kwargs):
        return self.create_access_token(username)
