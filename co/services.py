from collections import defaultdict

from co import errors

class UsersService(object):
    def __init__(self):
        self._users = []
        self._follows = defaultdict(list)

    def register(self, user):
        if self.is_registered(user):
            raise errors.UserAlreadyRegisteredError()
        self._users.append(user)

    def is_registered(self, user):
        return user in self._users

    def follow_to(self, user, target):
        self._follows[user].append(target)

    def is_following_to(self, user, other):
        return other in self._follows[user]

    def follows_to(self, user):
        return self._follows[user]

