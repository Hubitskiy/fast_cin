from typing import Dict

from fastapi import APIRouter, Depends, status

from core.settings import settings

from users.presenters import (
    CreateUserPresenter,
    AuthenticateUserPresenter,
    AuthorizationUserPresenter,
    ActivateUserPresenter,
    RefreshTokenPresenter
)
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


@router.post(
    path='/users/token-refresh/',
    tags=[TAG],
    status_code=status.HTTP_200_OK,
    response_model=TokenSerializer,
    description='Send In Headers "Authorization" param with Bearer Token for get refresh and access token'
)
def refresh_token(refresh_token_presenter: RefreshTokenPresenter = Depends(RefreshTokenPresenter)):
    return refresh_token_presenter()


@router.get(
    path='/users/me/',
    tags=[TAG],
    status_code=status.HTTP_200_OK,
    response_model=RetrieveUserSerializer
)
def retrieve_current_user(current_user: AuthorizationUserPresenter = Depends(AuthorizationUserPresenter)):
    return current_user()


@router.patch(
    path='/users/confirms-invitations/',
    tags=[TAG],
    status_code=status.HTTP_200_OK,
    response_model=RetrieveUserSerializer
)
def activate_user(activate_user_presenter: ActivateUserPresenter = Depends(ActivateUserPresenter)):
    return activate_user_presenter()
