from datetime import datetime, timedelta


# SERVER SETTINGS
SITE_NAME = "CIN"
SITE_URL = "0.0.0.0"

# AUTHORIZATION SETTINGS
# SECRET_KEY create run command
# openssl rand -hex 32
SECRET_KEY = "cca531f5d64afa46b1b670505313bde0f89145b60748e2d07953ed7a9ccd6ea7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = datetime.utcnow() + timedelta(hours=24)
REFRESH_EXPIRE_TIME = datetime.utcnow() + timedelta(days=5)
TOKEN_TYPE = "Bearer"
TOKEN_URL = "/users/token/"

# EMAIL SETTINGS
SMTP_SERVER = "smtp.gmail.com"
PORT = 465
SENDER_EMAIL = "contactcus2@gmail.com"
SENDER_PASSWORD = "cota-1111"

# TEMPLATES SETTINGS
TEMPLATE_PACKAGE = "emails"
