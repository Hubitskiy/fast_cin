from core.usecases import BaseService
from core.utils import crypt
from core.settings import settings


class CreateAccessTokenService(BaseService):

    def create_access_token(self, username: str):
        token = crypt.encode_jwt(username)

        return {
            "access_token": str(token),
            "token_type": settings.TOKEN_TYPE
        }

    def __call__(self, username: str, *args, **kwargs):
        return self.create_access_token(username)
