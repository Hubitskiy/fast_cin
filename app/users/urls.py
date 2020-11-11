from typing import Dict

from fastapi import APIRouter, Depends

from users.presenters import CreateUserPresenter


router = APIRouter()


@router.post(
    path='/users/',
    tags=["Users"],
    status_code=201,
    response_model=Dict
)
def create_user(create_user_presenter: CreateUserPresenter = Depends(CreateUserPresenter)) -> Dict:
    return create_user_presenter()
