from users import usecases
from users import services
from users import user_managment

dependencies = {
    user_managment.UserDBManagement,
    # services
    services.CreateUserService,

    # usecases
    usecases.CreateUserUseCase
}
