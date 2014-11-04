from expects import expect, be_true, raise_error

class RegistrationService(object):
    def __init__(self):
        self._users = []

    def register(self, user):
        if self.has_user(user):
            raise UserAlreadyRegisteredError()
        self._users.append(user)

    def has_user(self, user):
        return user in self._users


class UserAlreadyRegisteredError(Exception):
    pass


with description('Register user'):

    with before.each:
        self.user = '@foolano'
        self.service = RegistrationService()

    with it('registers a new user'):
        self.service.register(self.user)

        expect(self.service.has_user(self.user)).to(be_true)

    with context('when user already exists'):
        with it('raises error'):
            self.service.register(self.user)

            expect(lambda: self.service.register(self.user)).to(raise_error(UserAlreadyRegisteredError))

