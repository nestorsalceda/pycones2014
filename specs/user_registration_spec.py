from co import services, errors
from expects import expect, be_true, raise_error

with description('Register user'):

    with before.each:
        self.user = '@foolano'
        self.service = services.UsersService()

    with it('registers a new user'):
        self.service.register(self.user)

        expect(self.service.is_registered(self.user)).to(be_true)

    with context('when user already exists'):
        with it('raises error'):
            self.service.register(self.user)

            expect(lambda: self.service.register(self.user)).to(raise_error(errors.UserAlreadyRegisteredError))

