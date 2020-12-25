import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from core.settings import settings
from celery_tasks import app
from core.settings.settings import (SMTP_SERVER, PORT, SENDER_EMAIL)


class EmailSender(smtplib.SMTP_SSL):

    def __enter__(self):
        self.login(user=settings.SENDER_EMAIL, password=settings.SENDER_PASSWORD)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()


def prepare_email_content(to_email: str, content: str) -> MIMEMultipart:

    message = MIMEMultipart("alternative")

    message["To"] = to_email
    message["From"] = settings.SENDER_EMAIL
    message["Subject"] = settings.SITE_NAME

    html = MIMEText(content, "html")

    message.attach(html)

    return message


@app.task
def send_email(to_email: str, content: str) -> None:

    context = ssl.create_default_context()

    content = prepare_email_content(to_email=to_email, content=content)

    with EmailSender(host=SMTP_SERVER, port=PORT, context=context) as sender:
        sender.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=to_email,
            msg=content.as_string()
        )
