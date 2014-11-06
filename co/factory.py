from co import services, repositories
import redis

def create_users_service():
    return services.UsersService(repositories.UserRepository())

def create_redis_user_repository():
    return repositories.RedisUserRepository(redis.StrictRedis())

def create_durable_users_service():
    return services.UsersService(create_redis_user_repository())

