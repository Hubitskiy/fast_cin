import smtplib

from core.settings import settings


class EmailSender(smtplib.SMTP_SSL):

    def __enter__(self):
        self.login(user=settings.SENDER_EMAIL, password=settings.SENDER_PASSWORD)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()
