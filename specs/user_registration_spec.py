from co import factory, errors

from expects import expect, be_true, raise_error

with description('Register user'):

    with before.each:
        self.nickname = '@foolano'
        self.service = factory.create_users_service()

    with it('registers a new user'):
        self.service.register(self.nickname)

        expect(self.service.is_registered(self.nickname)).to(be_true)

    with context('when user already exists'):
        with it('raises error'):
            self.service.register(self.nickname)

            expect(lambda: self.service.register(self.nickname)).to(raise_error(errors.UserAlreadyRegisteredError))

