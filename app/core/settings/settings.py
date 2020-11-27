from datetime import datetime, timedelta


# SECRET_KEY create run command
# openssl rand -hex 32
SECRET_KEY = "cca531f5d64afa46b1b670505313bde0f89145b60748e2d07953ed7a9ccd6ea7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = datetime.utcnow() + timedelta(minutes=30)
TOKEN_TYPE = "Bearer"
