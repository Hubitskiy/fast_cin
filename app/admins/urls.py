from fastapi import APIRouter


router = APIRouter()


TAG = "Admins"


@router.get(
    path="/admin/users/",
    tags=[TAG]
)
def retrieve_list_users():
    pass
