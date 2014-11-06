import json

from co import user as u


class UserRepository(object):

    def __init__(self):
        self._users = {}

    def put(self, user):
        self._users[user.nickname] = user

    def exists(self, user):
        return user in self._users.keys()

    def clear(self):
        self._users = {}

    def find_by_nickname(self, nickname):
        return self._users.get(nickname)


class RedisUserRepository(object):

    KEY = 'users'

    def __init__(self, redis_client):
        self._client = redis_client

    def put(self, user):
        self._client.hset(self.KEY, user.nickname, json.dumps({"following": user.following, "cos": user.cos}))

    def exists(self, user):
        return self._client.hexists(self.KEY, user)

    def clear(self):
        return self._client.delete(self.KEY)

    def find_by_nickname(self, nickname):
        user = u.User(nickname)
        raw = json.loads(self._client.hget(self.KEY, nickname))

        for follow in raw['following']:
            user.follow_to(follow)

        for message in raw['cos']:
            user.publish_co(message)

        return user

