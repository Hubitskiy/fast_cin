from typing import List

from pydantic import BaseModel


class RetrieveUserForAdminSerializer(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_admin: bool


class RetrieveListUsersSerializer(BaseModel):
    offset: int
    limit: int
    result: List[RetrieveUserForAdminSerializer]
