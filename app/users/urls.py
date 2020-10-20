from fastapi import APIRouter, Depends
from users.presenters import CreateUserPresenter

router = APIRouter()


@router.get(
    path='/users/',
    tags=["Users"]
)
def get_user(create_presenter: CreateUserPresenter = Depends(CreateUserPresenter)):
    return create_presenter()
