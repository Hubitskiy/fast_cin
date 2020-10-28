from fastapi import APIRouter, Depends

from users.presenters import CreateUserPresenter


router = APIRouter()


@router.post(
    path='/users/',
    tags=["Users"],
    status_code=201
)
def create_user(create_user_presenter: CreateUserPresenter = Depends(CreateUserPresenter)):
    create_user_presenter()
