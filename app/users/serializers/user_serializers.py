from pydantic import BaseModel, Field


class CreateUserSerializer(BaseModel):

    email: str = Field(..., min_length=8, regex='[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')

    password: str = Field(..., min_length=8)

    first_name: str = Field(..., min_length=2, max_length=40)

    last_name: str = Field(..., min_length=2, max_length=40)

    class Config:
        schema_extra = {
            "example": {
                "email": "example@mm.com",
                "password": "12345678",
                "first_name": "Foo",
                "last_name": "Bar"
                }
            }


class RetrieveUserSerializer(BaseModel):

    id: int

    email: str

    first_name: str

    last_name: str

    is_active: bool
