from collections import defaultdict

from co import errors

class UsersService(object):
    def __init__(self, users_repository):
        self._users_repository = users_repository
        self._follows = defaultdict(list)

    def register(self, user):
        if self._users_repository.exists(user):
            raise errors.UserAlreadyRegisteredError()
        self._users_repository.put(user)

    def is_registered(self, user):
        return self._users_repository.exists(user)

    def follow_to(self, user, target):
        if not self.is_registered(user):
            raise errors.UserDoesNotExist()

        if not self.is_registered(target):
            raise errors.UserDoesNotExist()

        self._follows[user].append(target)

    def follows_to(self, user):
        return self._follows[user]
