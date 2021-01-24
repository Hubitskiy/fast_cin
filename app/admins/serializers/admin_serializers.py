from typing import List, Optional

from pydantic import BaseModel
from fastapi import Body


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


class UpdateUserByAdminSerializer(BaseModel):
    email: str = Body(None, regex="^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
    first_name: str = Body(None, min_length=8, max_length=40)
    last_name: Optional[str] = Body(None, min_length=8, max_length=40)
    is_active: bool = Body(None)
