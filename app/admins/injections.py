from admins import usecases
from admins import services
from admins import admins_managment


dependencies = {
    # db management
    admins_managment.AdminDBManagement,
    # usecases
    usecases.RetrieveUsersUseCase,
    # services
    services.ListRetrieveUserService,
    services.UniqueUserRetrieveService
}
