from co import errors, user

class UsersService(object):
    def __init__(self, users_repository):
        self._users_repository = users_repository

    def register(self, nickname):
        if self._users_repository.exists(nickname):
            raise errors.UserAlreadyRegisteredError()

        self._users_repository.put(user.User(nickname))

    def is_registered(self, nickname):
        return self._users_repository.exists(nickname)

    def follow_to(self, nickname, target):
        user = self._find_by_nickname(nickname)
        other = self._find_by_nickname(target)

        user.follow_to(other.nickname)

        self._users_repository.put(user)

    def follows_to(self, nickname):
        return self._find_by_nickname(nickname).following

    def _find_by_nickname(self, nickname):
        if not self.is_registered(nickname):
            raise errors.UserDoesNotExistError()

        return self._users_repository.find_by_nickname(nickname)

    def publish_co(self, nickname, content):
        user = self._find_by_nickname(nickname)
        user.publish_co(content)

    def cos_for(self, nickname):
        return self._find_by_nickname(nickname).cos
