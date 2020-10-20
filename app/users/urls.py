from fastapi import APIRouter, Depends
from users.presenters import CreateUserPresenter

router = APIRouter()


@router.post(
    path='/users/',
    tags=["Users"],
    status_code=200
)
def get_user(create_presenter: CreateUserPresenter = Depends(CreateUserPresenter)):
    create_presenter()
