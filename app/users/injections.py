from users import usecases
from users import services


dependencies = {
    # services
    services.CreateUserService,

    # usecases
    usecases.CreateUserUseCase
}
