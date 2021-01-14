from fastapi import APIRouter
from fastapi import Depends

from admins.presenters import RetrieveListUserPresenter


router = APIRouter()


TAG = "Admins"


@router.get(
    path="/admins/users/",
    tags=[TAG]
)
def retrieve_list_users(retrieve_list_user_presenter: RetrieveListUserPresenter = Depends(RetrieveListUserPresenter)):
    return retrieve_list_user_presenter()
