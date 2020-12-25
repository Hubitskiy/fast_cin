from users import usecases
from users import services
from users import user_managment

dependencies = {
    user_managment.UserDBManagement,
    # services
    services.SendUserRegistrationInvitationService,
    services.CreateAccessTokenService,
    services.CreateUserService,

    # usecases
    usecases.AuthenticateUserUseCase,
    usecases.CreateUserUseCase
}
