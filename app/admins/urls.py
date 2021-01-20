from fastapi import APIRouter
from fastapi import Depends

from admins.presenters import RetrieveListUserPresenter, RetrieveUniqueUserPresenter
from admins.serializers import RetrieveListUsersSerializer, RetrieveUserForAdminSerializer


router = APIRouter()


TAG = "Admins"


@router.get(
    path="/admins/users/",
    tags=[TAG],
    response_model=RetrieveListUsersSerializer
)
def retrieve_list_users(retrieve_list_user_presenter: RetrieveListUserPresenter = Depends(RetrieveListUserPresenter)):
    return retrieve_list_user_presenter()


@router.get(
    path="/admins/users/{pk}/",
    tags=[TAG],
    response_model=RetrieveUserForAdminSerializer
)
def retrieve_unique_user(retrieve_unique_user: RetrieveUniqueUserPresenter = Depends(RetrieveUniqueUserPresenter)):
    return retrieve_unique_user()
