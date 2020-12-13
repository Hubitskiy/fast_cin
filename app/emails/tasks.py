import ssl

from celery_tasks import app
from core.utils.email import EmailSender
from core.settings.settings import (SMTP_SERVER, PORT, SENDER_EMAIL)


@app.task
def send_email(to_email: str):

    context = ssl.create_default_context()

    with EmailSender(host=SMTP_SERVER, port=PORT, context=context) as sender:
        sender.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=to_email,
            msg="Test Content"
        )
