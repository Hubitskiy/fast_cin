from typing import List

from pydantic import BaseModel


class RetrieveUserSerializer(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_admin: bool


class RetrieveListUsersSerializer(BaseModel):

    result: List[RetrieveUserSerializer]
