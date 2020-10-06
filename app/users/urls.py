from fastapi import APIRouter


router = APIRouter()


@router.get(
    '/users/',
    tags=["Users"]
)
def get_user():
    return {"message": "Hello, it`s me Real User"}
