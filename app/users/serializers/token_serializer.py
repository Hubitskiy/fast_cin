from pydantic import BaseModel


class TokenSerializer(BaseModel):
    refresh_token: str
    access_token: str
    token_type: str


class UidTokenSerializer(BaseModel):
    uid: str
    token: str
