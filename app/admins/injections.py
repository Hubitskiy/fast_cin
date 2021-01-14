from admins import usecases
from admins import services


dependencies = {
    # usecases
    usecases.RetrieveUsersUseCase,
    # services
    services.ListRetrieveUserService,
    services.UniqueUserRetrieve
}
