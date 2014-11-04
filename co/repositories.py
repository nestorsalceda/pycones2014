class UserRepository(object):

    def __init__(self):
        self._users = []

    def put(self, user):
        self._users.append(user)

    def exists(self, user):
        return user in self._users

    def clear(self):
        self._users = []


class RedisUserRepository(object):

    KEY = 'users'

    def __init__(self, redis_client):
        self._client = redis_client

    def put(self, user):
        self._client.sadd(self.KEY, user)

    def exists(self, user):
        return self._client.sismember(self.KEY, user)

    def clear(self):
        return self._client.delete(self.KEY)
