from co import services, repositories

def create_users_service():
    return services.UsersService(repositories.UserRepository())
