from typing import Dict

from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordBearer

from users.presenters import (CreateUserPresenter, AuthenticateUserPresenter)
from users.serializers import TokenSerializer

router = APIRouter()


TAG = "Users"


@router.post(
    path='/users/',
    tags=[TAG],
    status_code=status.HTTP_204_NO_CONTENT
)
def create_user(create_user_presenter: CreateUserPresenter = Depends(CreateUserPresenter)) -> Dict:
    return create_user_presenter()


@router.post(
    path='/jwt/create/',
    tags=[TAG],
    status_code=status.HTTP_200_OK,
)
def create_access_token(authenticate_user_presenter: AuthenticateUserPresenter = Depends()):
    return authenticate_user_presenter()
