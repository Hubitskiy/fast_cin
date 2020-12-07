from typing import Dict

from fastapi import APIRouter, Depends, status

from core.settings import settings

from users.presenters import (CreateUserPresenter, AuthenticateUserPresenter, AuthorizationUserPresenter)
from users.serializers import TokenSerializer, RetrieveUserSerializer


router = APIRouter()


TAG = "Users"


@router.post(
    path='/users/',
    tags=[TAG],
    status_code=status.HTTP_204_NO_CONTENT
)
def create_user(create_user_presenter: CreateUserPresenter = Depends()) -> Dict:
    return create_user_presenter()


@router.post(
    path=settings.TOKEN_URL,
    tags=[TAG],
    status_code=status.HTTP_200_OK,
    response_model=TokenSerializer
)
def create_access_token(authenticate_user_presenter: AuthenticateUserPresenter = Depends()):
    return authenticate_user_presenter()


@router.get(
    path='/users/me/',
    tags=[TAG],
    status_code=status.HTTP_200_OK,
    response_model=RetrieveUserSerializer
)
def retrieve_current_user(current_user: AuthorizationUserPresenter = Depends(AuthorizationUserPresenter)):
    return current_user()
