from attr import attrs

from core.usecases import BaseService
from core.utils import crypt
from core.utils.email import send_email

from users.user_managment import UserDBManagement
from users.models import UserModel

from emails.templates_renders import ConfirmTemplate


@attrs(auto_attribs=True)
class CreateUserService(BaseService):
    _user_db_management: UserDBManagement
    _confirm_template: ConfirmTemplate

    def send_email_invitation(self, user: UserModel):

        template = self._confirm_template(link="http://link.com")

        send_email.delay(to_email=user.email, content=template)

    def create_user(self, **kwargs) -> UserModel:

        password = kwargs.pop("password")

        hashed_password = crypt.get_password_hash(password=password)

        kwargs.setdefault("hashed_password", hashed_password)

        user = self._user_db_management.create_user(**kwargs)

        self.send_email_invitation(user=user)

        return user

    def __call__(self, **kwargs) -> UserModel:
        return self.create_user(**kwargs)
