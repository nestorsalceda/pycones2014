from co import services, errors

from expects import expect, be_true, contain, raise_error

with description('Follow user'):
    with before.each:
        self.user = '@foolano'
        self.other_user = '@da_kewl_guru'
        self.service = services.UsersService()

    with it('returns all users followed by a user'):
        self.service.register(self.user)
        self.service.register(self.other_user)

        self.service.follow_to(self.user, self.other_user)

        expect(self.service.follows_to(self.user)).to(contain(self.other_user))

    with context('when user is not registered'):
        with it('raises an error'):
            self.service.register(self.other_user)

            expect(lambda: self.service.follow_to(self.user, self.other_user)).to(raise_error(errors.UserDoesNotExist))

    with context('when target user is not registered'):
        with it('raises an error'):
            self.service.register(self.user)

            expect(lambda: self.service.follow_to(self.user, self.other_user)).to(raise_error(errors.UserDoesNotExist))
