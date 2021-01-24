from users import usecases
from users import services
from users import user_managment

dependencies = {
    # db management
    user_managment.UserDBManagement,
    # services
    services.ActivateUserService,
    services.SendUserRegistrationInvitationService,
    services.CreateTokensService,
    services.CreateUserService,

    # usecases
    usecases.RefreshTokenUseCase,
    usecases.ActivateUserUseCase,
    usecases.AuthenticateUserUseCase,
    usecases.CreateUserUseCase
}
