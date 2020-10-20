from pydantic import BaseModel, Field


class CreateUserSerializer(BaseModel):

    email: str = Field(..., min_length=8)

    hashed_password: str = Field(..., min_length=8)

    first_name: str

    last_name: str