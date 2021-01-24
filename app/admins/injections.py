from admins import usecases
from admins import services
from admins import admins_managment


dependencies = {
    # db management
    admins_managment.AdminDBManagement,
    # usecases
    usecases.UpdateUserUseCase,
    usecases.RetrieveUsersUseCase,
    # services
    services.UpdateUserService,
    services.ListRetrieveUserService,
    services.UniqueUserRetrieveService
}
