from fastapi import APIRouter
from fastapi import Depends

from admins.presenters import RetrieveListUserPresenter
from admins.serializers import RetrieveListUsersSerializer


router = APIRouter()


TAG = "Admins"


@router.get(
    path="/admins/users/",
    tags=[TAG],
    response_model=RetrieveListUsersSerializer
)
def retrieve_list_users(retrieve_list_user_presenter: RetrieveListUserPresenter = Depends(RetrieveListUserPresenter)):
    return retrieve_list_user_presenter()
