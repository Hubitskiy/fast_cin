from typing import Dict

from fastapi import APIRouter, Depends, status

from users.presenters import CreateUserPresenter


router = APIRouter()


@router.post(
    path='/users/',
    tags=["Users"],
    status_code=status.HTTP_204_NO_CONTENT
)
def create_user(create_user_presenter: CreateUserPresenter = Depends(CreateUserPresenter)) -> Dict:
    return create_user_presenter()
