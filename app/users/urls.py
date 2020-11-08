from fastapi import APIRouter, Depends
from typing import Dict

from users.presenters import CreateUserPresenter


router = APIRouter()


@router.post(
    path='/users/',
    tags=["Users"],
    status_code=201,
    response_model=Dict
)
def create_user(create_user_presenter: CreateUserPresenter = Depends(CreateUserPresenter)):
    return create_user_presenter()
