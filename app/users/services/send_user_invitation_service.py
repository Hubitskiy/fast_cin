from attr import attrs
from jinja2 import Template

from core.usecases import BaseService
from core.utils.email import send_email
from core.utils import crypt
from core.settings import settings

from users.models import UserModel
from emails.templates_renders import ConfirmTemplate


@attrs(auto_attribs=True)
class SendUserRegistrationInvitationService(BaseService):
    _confirm_template: ConfirmTemplate

    def render_template(self, user: UserModel) -> Template:

        uid = crypt.base64_encode(user.id)

        token = crypt.base64_encode(user.email)

        return self._confirm_template(site_url=settings.SITE_URL, uid=uid, token=token)

    def send_email_invitation(self, user: UserModel, template: Template) -> None:

        send_email.delay(to_email=user.email, content=template)

    def __call__(self, user: UserModel, *args, **kwargs):

        template = self.render_template(user=user)

        self.send_email_invitation(user=user, template=template)

        return None
