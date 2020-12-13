import smtplib
import ssl


from core.settings import settings
from celery_tasks import app
from core.settings.settings import (SMTP_SERVER, PORT, SENDER_EMAIL)


class EmailSender(smtplib.SMTP_SSL):

    def __enter__(self):
        self.login(user=settings.SENDER_EMAIL, password=settings.SENDER_PASSWORD)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()


@app.task
def send_email(to_email: str):

    context = ssl.create_default_context()

    with EmailSender(host=SMTP_SERVER, port=PORT, context=context) as sender:
        sender.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=to_email,
            msg="Test Content"
        )
