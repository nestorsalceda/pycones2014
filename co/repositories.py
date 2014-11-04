class UserRepository(object):

    def __init__(self):
        self._users = []

    def put(self, user):
        self._users.append(user)

    def exists(self, user):
        return user in self._users
